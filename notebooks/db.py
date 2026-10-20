
import os
import re
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, URL

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SQL_DIR = PROJECT_ROOT / "sql"

# Load environment variables
load_dotenv(PROJECT_ROOT / ".env")

DB_SERVER = os.getenv("DB_SERVER", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "1433"))
DB_NAME = os.getenv("DB_NAME", "BankAnalyticsDB")

ADMIN_USER = "sa"
ADMIN_PASSWORD = os.environ["MSSQL_SA_PASSWORD"]

APP_USER = os.getenv("DB_APP_USER", "bank_analytics")
APP_PASSWORD = os.environ["DB_APP_PASSWORD"]


def get_engine(database=None, admin=False):
    """Create a SQL Server connection engine."""
    user = ADMIN_USER if admin else APP_USER
    password = ADMIN_PASSWORD if admin else APP_PASSWORD

    url = URL.create(
        "mssql+pymssql",
        username=user,
        password=password,
        host=DB_SERVER,
        port=DB_PORT,
        database=database or DB_NAME
    )

    return create_engine(url, pool_pre_ping=True)


def run_sql_file(path, engine):
    """Execute a SQL file containing GO separators."""
    sql = Path(path).read_text(encoding="utf-8")

    batches = [
        batch.strip()
        for batch in re.split(
            r"^\s*GO\s*$",
            sql,
            flags=re.MULTILINE | re.IGNORECASE
        )
        if batch.strip()
    ]

    with engine.connect().execution_options(
        isolation_level="AUTOCOMMIT"
    ) as conn:
        for batch in batches:
            if batch.upper().startswith("USE "):
                continue
            conn.execute(text(batch))


def setup_database():
    """Create database, schemas and application login."""

    # Create database
    with get_engine("master", admin=True).connect().execution_options(
        isolation_level="AUTOCOMMIT"
    ) as conn:
        conn.execute(text(
            f"IF DB_ID('{DB_NAME}') IS NULL "
            f"CREATE DATABASE [{DB_NAME}]"
        ))

    # Create schemas
    admin_engine = get_engine(admin=True)

    run_sql_file(
        SQL_DIR / "01_setup_database.sql",
        admin_engine
    )

    # Create application login
    safe_password = APP_PASSWORD.replace("'", "''")

    with get_engine("master", admin=True).connect().execution_options(
        isolation_level="AUTOCOMMIT"
    ) as conn:
        conn.execute(text(f"""
            IF NOT EXISTS (
                SELECT 1 FROM sys.server_principals
                WHERE name = '{APP_USER}'
            )
            CREATE LOGIN [{APP_USER}]
            WITH PASSWORD = '{safe_password}',
            DEFAULT_DATABASE = [{DB_NAME}],
            CHECK_EXPIRATION = OFF
        """))

    # Create database user
    with admin_engine.connect().execution_options(
        isolation_level="AUTOCOMMIT"
    ) as conn:
        conn.execute(text(f"""
            IF USER_ID('{APP_USER}') IS NULL
                CREATE USER [{APP_USER}]
                FOR LOGIN [{APP_USER}]
        """))

        # Course project: database-level permissions
        conn.execute(text(f"""
            IF IS_ROLEMEMBER('db_owner', '{APP_USER}') = 0
                ALTER ROLE db_owner ADD MEMBER [{APP_USER}]
        """))

    # Verify connection
    with get_engine().connect() as conn:
        print("Connected as:",
              conn.execute(text("SELECT SUSER_SNAME()")).scalar())

        schemas = pd.read_sql(
            "SELECT name FROM sys.schemas "
            "WHERE name IN ('bronze', 'silver', 'gold')",
            conn
        )

        print(schemas)


if __name__ == "__main__":
    setup_database()
