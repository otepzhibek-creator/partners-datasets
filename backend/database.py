from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./partners.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Partner(Base):
    __tablename__ = "partners"

    id = Column(Integer, primary_key=True, index=True)
    partner_type = Column(String, default="b2b")  # "b2b" or "dataset"
    company_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(Text)
    use_case = Column(Text)
    website = Column(String)

    # Contact details (decision maker preferred)
    contact_name = Column(String)
    contact_position = Column(String)
    contact_email = Column(String)
    contact_phone = Column(String)
    contact_linkedin = Column(String)
    contact_telegram = Column(String)
    contact_whatsapp = Column(String)

    # Status tracking
    status = Column(String, default="new")       # new / contacted / in_progress / closed / rejected
    priority = Column(String, default="medium")  # high / medium / low
    notes = Column(Text)

    # Auto-generated outreach message
    generated_message = Column(Text)

    # Dataset-specific fields
    dataset_types = Column(String)        # e.g. "audio,text,video"
    dataset_language = Column(String)     # e.g. "kz,ru"
    collaboration_type = Column(String)   # "paid" / "free" / "partnership"

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    Base.metadata.create_all(bind=engine)
