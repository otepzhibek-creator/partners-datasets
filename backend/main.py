import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from database import get_db, init_db, Partner
from message_generator import generate_message
from seed_data import get_all_seed_data

app = FastAPI(title="Freedom Speech — Partner Dashboard")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

FRONTEND = os.path.join(os.path.dirname(__file__), "..", "frontend")


@app.on_event("startup")
def startup():
    init_db()
    from sqlalchemy.orm import Session
    from database import SessionLocal
    db = SessionLocal()
    if db.query(Partner).count() == 0:
        for row in get_all_seed_data():
            db.add(Partner(**{k: v for k, v in row.items() if hasattr(Partner, k)}))
        db.commit()
    db.close()


# ── Pydantic schemas ──────────────────────────────────────────────────────────

class PartnerUpdate(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None
    notes: Optional[str] = None
    contact_name: Optional[str] = None
    contact_position: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_linkedin: Optional[str] = None
    contact_telegram: Optional[str] = None
    contact_whatsapp: Optional[str] = None


class PartnerCreate(BaseModel):
    partner_type: str = "b2b"
    company_name: str
    category: str
    description: Optional[str] = None
    use_case: Optional[str] = None
    website: Optional[str] = None
    contact_name: Optional[str] = None
    contact_position: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_linkedin: Optional[str] = None
    contact_telegram: Optional[str] = None
    contact_whatsapp: Optional[str] = None
    priority: str = "medium"
    dataset_types: Optional[str] = None
    dataset_language: Optional[str] = None
    collaboration_type: Optional[str] = None


# ── API routes ────────────────────────────────────────────────────────────────

@app.get("/api/partners")
def list_partners(
    partner_type: Optional[str] = None,
    category: Optional[str] = None,
    status: Optional[str] = None,
    priority: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    q = db.query(Partner).filter(Partner.is_active == True)
    if partner_type:
        q = q.filter(Partner.partner_type == partner_type)
    if category:
        q = q.filter(Partner.category == category)
    if status:
        q = q.filter(Partner.status == status)
    if priority:
        q = q.filter(Partner.priority == priority)
    if search:
        q = q.filter(Partner.company_name.ilike(f"%{search}%"))
    return [_to_dict(p) for p in q.order_by(Partner.priority.desc(), Partner.id).all()]


@app.get("/api/partners/{pid}")
def get_partner(pid: int, db: Session = Depends(get_db)):
    p = db.query(Partner).filter(Partner.id == pid).first()
    if not p:
        raise HTTPException(404)
    return _to_dict(p)


@app.patch("/api/partners/{pid}")
def update_partner(pid: int, body: PartnerUpdate, db: Session = Depends(get_db)):
    p = db.query(Partner).filter(Partner.id == pid).first()
    if not p:
        raise HTTPException(404)
    for k, v in body.model_dump(exclude_none=True).items():
        setattr(p, k, v)
    db.commit()
    return _to_dict(p)


@app.post("/api/partners")
def create_partner(body: PartnerCreate, db: Session = Depends(get_db)):
    data = body.model_dump()
    msg = generate_message(data["company_name"], data["category"], data.get("contact_name"), data.get("use_case") or "")
    p = Partner(**data, generated_message=msg, status="new")
    db.add(p)
    db.commit()
    db.refresh(p)
    return _to_dict(p)


@app.delete("/api/partners/{pid}")
def delete_partner(pid: int, db: Session = Depends(get_db)):
    p = db.query(Partner).filter(Partner.id == pid).first()
    if not p:
        raise HTTPException(404)
    p.is_active = False
    db.commit()
    return {"ok": True}


@app.post("/api/partners/{pid}/regenerate")
def regen_message(pid: int, db: Session = Depends(get_db)):
    p = db.query(Partner).filter(Partner.id == pid).first()
    if not p:
        raise HTTPException(404)
    p.generated_message = generate_message(p.company_name, p.category, p.contact_name, p.use_case or "")
    db.commit()
    return {"message": p.generated_message}


@app.get("/api/stats")
def stats(db: Session = Depends(get_db)):
    all_p = db.query(Partner).filter(Partner.is_active == True).all()
    return {
        "total": len(all_p),
        "b2b": sum(1 for p in all_p if p.partner_type == "b2b"),
        "dataset": sum(1 for p in all_p if p.partner_type == "dataset"),
        "new": sum(1 for p in all_p if p.status == "new"),
        "contacted": sum(1 for p in all_p if p.status == "contacted"),
        "in_progress": sum(1 for p in all_p if p.status == "in_progress"),
        "high": sum(1 for p in all_p if p.priority == "high"),
    }


@app.get("/api/categories")
def categories(partner_type: Optional[str] = None, db: Session = Depends(get_db)):
    q = db.query(Partner.category).filter(Partner.is_active == True)
    if partner_type:
        q = q.filter(Partner.partner_type == partner_type)
    return sorted(set(r[0] for r in q.distinct().all()))


# ── Static frontend ───────────────────────────────────────────────────────────

@app.get("/")
def root():
    return FileResponse(os.path.join(FRONTEND, "index.html"))


def _to_dict(p: Partner):
    return {c.name: getattr(p, c.name) for c in p.__table__.columns}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
