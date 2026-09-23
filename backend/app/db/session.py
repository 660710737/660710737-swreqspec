from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.config import DATABASE_URL

# CON-TECH-01: engine ต่อฐานข้อมูลผ่าน DATABASE_URL (PostgreSQL ในระบบจริง, SQLite ในหน่วยความจำตอน test)
_is_sqlite_memory = DATABASE_URL == "sqlite:///:memory:"
_connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=_connect_args,
    poolclass=StaticPool if _is_sqlite_memory else None,
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
