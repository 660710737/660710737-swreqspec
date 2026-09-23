import datetime

from sqlalchemy import Date, DateTime, ForeignKey, String, Time
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Slot(Base):
    """ช่วงเวลาตรวจของแต่ละแพ็กเกจในแต่ละวัน รองรับ FR-BKG-01, FR-BKG-06, ASM-01"""

    __tablename__ = "slots"

    id: Mapped[int] = mapped_column(primary_key=True)
    slot_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    start_time: Mapped[datetime.time] = mapped_column(Time, nullable=False)
    package_code: Mapped[str] = mapped_column(String, nullable=False)
    capacity: Mapped[int] = mapped_column(nullable=False)
    remaining: Mapped[int] = mapped_column(nullable=False)


class Booking(Base):
    """การจองของผู้รับบริการ 1 รายการ รองรับ FR-BKG-02, FR-BKG-04
    เก็บเฉพาะ hn ไม่มีคอลัมน์เลขบัตรประชาชน ตาม IF-HIS-01
    """

    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    hn: Mapped[str] = mapped_column(String, nullable=False)
    slot_id: Mapped[int] = mapped_column(ForeignKey("slots.id"), nullable=False)
    booking_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    queue_no: Mapped[str | None] = mapped_column(String, nullable=True)
    status: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)


class AuditLog(Base):
    """บันทึกทุกครั้งที่เข้าถึงข้อมูลการจอง/สุขภาพ รองรับ DOM-PDPA-01"""

    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    actor_id: Mapped[str] = mapped_column(String, nullable=False)
    action: Mapped[str] = mapped_column(String, nullable=False)
    hn: Mapped[str] = mapped_column(String, nullable=False)
    accessed_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
