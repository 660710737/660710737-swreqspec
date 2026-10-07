# test ของ T-03: จองคิวสำเร็จ
# AC-BKG-01 (FR-BKG-04)
from tests.conftest import AUTH


def test_AC_BKG_01(client, make_slot):
    """AC-BKG-01: ยืนยันตัวตนแล้ว และช่วง 09.00 น. มีที่นั่งว่าง จองแล้วต้องสำเร็จ"""
    slot = make_slot(start="09:00", remaining=1)

    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    assert res.status_code == 201


def test_TC_BKG_01_1_booking_success_and_seats_zero(client, db, make_slot):
    """TC-BKG-01-1 (AC-BKG-01, ทางปกติ)"""
    from sqlalchemy import func, select

    from app.db.models import Booking

    # Given ยืนยันตัวตนแล้ว และช่วง 09.00 น. มีที่นั่งว่าง 1 ที่
    slot = make_slot(start="09:00", remaining=1)

    # When ยืนยันการจอง
    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    # Then 1) บันทึกสำเร็จ มีการจอง 1 รายการ
    assert res.status_code == 201
    count = db.scalar(select(func.count()).select_from(Booking).where(Booking.slot_id == slot.id))
    assert count == 1

    # Then 2) ที่นั่งว่างของช่วงนั้นเป็น 0
    db.refresh(slot)
    assert slot.remaining == 0

    # Then 3) แสดงหมายเลขคิว — ยังไม่ตรวจ เพราะรอ Q-02 (รูปแบบและวิธีออกเลขคิวยังไม่ได้ตัดสิน)


def test_TC_BKG_01_2_full_slot_rejects_booking(client, db, make_slot):
    """TC-BKG-01-2 (AC-BKG-01, ขอบ)"""
    from sqlalchemy import func, select

    from app.db.models import Booking

    # Given ยืนยันตัวตนแล้ว และช่วง 09.00 น. เหลือ 0 ที่ (มีคนจองที่สุดท้ายไปแล้ว)
    slot = make_slot(start="09:00", remaining=0, capacity=1)

    # When ยืนยันการจองช่วง 09.00 น.
    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    # Then 1) ไม่สร้างรายการจอง (ตาม FR-BKG-03)
    count = db.scalar(select(func.count()).select_from(Booking).where(Booking.slot_id == slot.id))
    assert count == 0

    # Then 2) แจ้ง "ช่วงเวลาเต็ม" พร้อมช่วงใกล้เคียง (ตาม FR-BKG-03 / AC-BKG-03, plan.md ข้อ 4: 409)
    assert res.status_code == 409
    assert "ช่วงเวลาเต็ม" in res.text
    # ช่วงใกล้เคียง: ยังไม่ assert เพราะ plan.md ข้อ 4 ไม่ได้กำหนดชื่อฟิลด์ใน response


def test_TC_BKG_01_3_not_verified(client, db, make_slot):
    """TC-BKG-01-3 (AC-BKG-01, ทางผิด)"""
    from sqlalchemy import func, select

    from app.db.models import Booking

    # Given ช่วง 09.00 น. มีที่นั่งว่าง 1 ที่ แต่ยังไม่ยืนยันตัวตน
    slot = make_slot(start="09:00", remaining=1)

    # When ยืนยันการจอง (ไม่ส่งผลยืนยันตัวตน)
    res = client.post("/bookings", json={"slot_id": slot.id})

    # Then ปฏิเสธการจอง (ตาม IF-IDP-01)
    assert not res.is_success
    count = db.scalar(select(func.count()).select_from(Booking).where(Booking.slot_id == slot.id))
    assert count == 0

    # Then ไม่ตัดที่นั่ง
    db.refresh(slot)
    assert slot.remaining == 1

    # Then รูปแบบ response/ข้อความที่แสดง: ไม่ assert เพราะ spec ไม่ได้บอก
