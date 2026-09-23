import importlib
import os

os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")

import pytest

from app.db.models import Base
from app.db.session import SessionLocal, engine

_init_migration = importlib.import_module("app.db.migrations.001_init")


@pytest.fixture()
def db_session():
    """เตรียมฐานข้อมูล SQLite ในหน่วยความจำให้ทุก test ตาม plan.md (ไม่ต้องมี PostgreSQL จริงตอน test)"""
    _init_migration.upgrade(engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)
