#!/bin/bash
set -e

echo "=== Freedom Speech Partner Dashboard ==="
cd "$(dirname "$0")/backend"

# Check Python
if command -v python3 &>/dev/null; then
  PY=python3
elif command -v python &>/dev/null; then
  PY=python
else
  echo "❌ Python не найден. Установите Python 3.10+ с https://python.org"
  exit 1
fi

# Check version >= 3.10
PY_VER=$($PY -c "import sys; print(sys.version_info.major * 10 + sys.version_info.minor)")
if [ "$PY_VER" -lt 310 ]; then
  echo "❌ Нужен Python 3.10+. У вас: $($PY --version)"
  exit 1
fi
echo "✅ Python: $($PY --version)"

# Create venv
if [ ! -d ".venv" ]; then
  echo "Создаём виртуальное окружение..."
  $PY -m venv .venv
fi

# Activate
source .venv/bin/activate

# Install deps
echo "Устанавливаем зависимости..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

echo ""
echo "✅ Открывайте в браузере: http://localhost:8000"
echo "   Ctrl+C — остановить"
echo ""

python main.py
