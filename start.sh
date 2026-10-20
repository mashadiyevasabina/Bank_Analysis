#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

echo "1/3 - SQL Server başladılır..."
docker compose up -d

echo "2/3 - SQL Server-in hazır olması gözlənilir..."

for i in {1..60}; do
    STATUS=$(docker inspect --format='{{.State.Health.Status}}' bank_sqlserver 2>/dev/null || true)

    if [ "$STATUS" = "healthy" ]; then
        echo "SQL Server hazırdır!"
        break
    fi

    if [ "$STATUS" = "unhealthy" ]; then
        echo "SQL Server unhealthy vəziyyətindədir."
        docker compose ps
        exit 1
    fi

    if [ "$i" -eq 60 ]; then
        echo "SQL Server 5 dəqiqə ərzində hazır olmadı."
        docker compose ps
        exit 1
    fi

    sleep 5
done

echo "3/3 - Python və SQL bağlantısı yoxlanılır..."

python - <<'PY'
import sys
from pathlib import Path
from sqlalchemy import text

sys.path.insert(0, str(Path.cwd() / "notebooks"))
from db import get_engine

with get_engine().connect() as conn:
    result = conn.execute(text("SELECT DB_NAME()")).scalar()
    print("Database bağlantısı uğurludur:", result)
PY

echo ""
echo "================================="
echo "BANK ANALYSIS SISTEMI HAZIRDIR!"
echo "================================="