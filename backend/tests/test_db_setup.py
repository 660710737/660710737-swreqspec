from sqlalchemy import inspect

from app.db.session import engine


def test_migration_creates_tables(db_session):
    """T-01 เสร็จเมื่อ: migration สร้างตาราง slots, bookings, audit_logs ได้"""
    table_names = set(inspect(engine).get_table_names())
    assert {"slots", "bookings", "audit_logs"} <= table_names


def test_bookings_table_has_no_national_id_column(db_session):
    """IF-HIS-01: ตาราง bookings ต้องไม่มีคอลัมน์เลขบัตรประชาชน"""
    columns = {col["name"] for col in inspect(engine).get_columns("bookings")}
    assert "hn" in columns
    assert "national_id" not in columns
