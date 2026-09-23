from app.db.models import Base


def upgrade(engine):
    """สร้างตาราง slots, bookings, audit_logs ตามโมเดลใน plan.md ข้อ 3 (CON-TECH-01, DOM-PDPA-01, IF-HIS-01)"""
    Base.metadata.create_all(engine)
