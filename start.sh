#!/bin/bash
set -e

echo "=== Freedom Speech Partner Dashboard ==="
cd "$(dirname "$0")/backend"

if ! command -v python3 &>/dev/null; then
  echo "Python3 не найден. Установите Python 3.9+"
  exit 1
fi

if [ ! -d ".venv" ]; then
  echo "Создаём виртуальное окружение..."
  python3 -m venv .venv
fi

source .venv/bin/activate
echo "Устанавливаем зависимости..."
pip install -q -r requirements.txt

echo ""
echo "✅ Запускаем сервер: http://localhost:8000"
echo "   Нажмите Ctrl+C для остановки"
echo ""

python main.py
