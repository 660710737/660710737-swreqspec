# Tasks: จองคิวตรวจสุขภาพ (Booking)

Feature: จองคิวตรวจสุขภาพ (Booking) | Spec ID: SPEC-BKG-001
อ้างอิง: plan.md (plan v1, ทีมตรวจแล้ว) | สร้างด้วย /tasks | วันที่: 2569-09-23

สรุป: ทั้งหมด 15 task | 1 task รอ Q-02 (T-10)

## รายการ task

### T-01 สร้างตารางและ migration
- รองรับ: CON-TECH-01, DOM-PDPA-01, IF-HIS-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-01
- ไฟล์ที่แตะ: backend/requirements.txt, backend/pytest.ini, backend/app/config.py, backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py, backend/tests/conftest.py
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: รัน migration แล้วสร้างตาราง slots, bookings (ไม่มีคอลัมน์เลขบัตรประชาชน), audit_logs ได้ และ fixture ฐานข้อมูล SQLite ในหน่วยความจำใน conftest.py ใช้งานได้
- สถานะ: พร้อมทำ

### T-02 สร้างการตรวจสอบผลยืนยันตัวตนก่อนเข้าถึง API
- รองรับ: IF-IDP-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-02
- ไฟล์ที่แตะ: backend/app/auth/idp.py, backend/tests/test_auth_idp.py
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: request ที่ไม่มีผลยืนยันตัวตนจากระบบยืนยันตัวตนถูกปฏิเสธ และ request ที่มีผลยืนยันตัวตนแล้วผ่านการตรวจได้
- สถานะ: พร้อมทำ

### T-03 สร้าง GET /slots คำนวณช่วงว่างตามแพ็กเกจ
- รองรับ: FR-BKG-01, FR-BKG-06
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-03 (AC-BKG-05 วัด performance แยกอยู่ที่ T-11)
- ไฟล์ที่แตะ: backend/app/main.py, backend/app/slots/router.py, backend/app/slots/service.py, backend/tests/test_slots.py
- ต้องทำหลัง: T-01, T-02
- เสร็จเมื่อ: เรียก GET /slots ได้รายการช่วงเวลาว่างภายใน 30 วันข้างหน้าพร้อมที่นั่งคงเหลือ และเปลี่ยน package_code แล้วผลลัพธ์เปลี่ยนตามแพ็กเกจ
- สถานะ: พร้อมทำ

### T-04 สร้าง POST /bookings พื้นฐาน ตัดที่นั่งและบันทึก
- รองรับ: FR-BKG-04
- ตรวจด้วย: AC-BKG-01
- ไฟล์ที่แตะ: backend/app/main.py, backend/app/booking/router.py, backend/app/booking/service.py, backend/tests/test_AC_BKG_01.py
- ต้องทำหลัง: T-01, T-02, T-03
- เสร็จเมื่อ: test_AC_BKG_01 ผ่าน
- สถานะ: พร้อมทำ

### T-05 กันจองซ้ำในวันเดียวกัน
- รองรับ: FR-BKG-02
- ตรวจด้วย: AC-BKG-02
- ไฟล์ที่แตะ: backend/app/booking/service.py, backend/tests/test_AC_BKG_02.py
- ต้องทำหลัง: T-04
- เสร็จเมื่อ: test_AC_BKG_02 ผ่าน
- สถานะ: พร้อมทำ

### T-06 เสนอช่วงเวลาใกล้เคียงเมื่อช่วงที่เลือกเต็ม
- รองรับ: FR-BKG-03
- ตรวจด้วย: AC-BKG-03
- ไฟล์ที่แตะ: backend/app/booking/router.py, backend/app/booking/service.py, backend/tests/test_AC_BKG_03.py
- ต้องทำหลัง: T-05
- เสร็จเมื่อ: test_AC_BKG_03 ผ่าน
- สถานะ: พร้อมทำ

### T-07 คิวส่งข้อความยืนยันและการส่งซ้ำ
- รองรับ: FR-BKG-05, IF-NOT-01, NFR-REL-02
- ตรวจด้วย: AC-BKG-04
- ไฟล์ที่แตะ: backend/app/notify/queue.py, backend/app/booking/service.py, backend/tests/test_AC_BKG_04.py
- ต้องทำหลัง: T-04
- เสร็จเมื่อ: test_AC_BKG_04 ผ่าน
- สถานะ: พร้อมทำ

### T-08 บันทึก audit log เมื่อเข้าถึงข้อมูลการจอง
- รองรับ: DOM-PDPA-01
- ตรวจด้วย: AC-BKG-06
- ไฟล์ที่แตะ: backend/app/audit/middleware.py, backend/app/main.py, backend/tests/test_AC_BKG_06.py
- ต้องทำหลัง: T-01, T-02
- เสร็จเมื่อ: test_AC_BKG_06 ผ่าน
- สถานะ: พร้อมทำ

### T-09 ค้น HN จาก HIS ด้วยเลขบัตรประชาชน
- รองรับ: IF-HIS-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-09
- ไฟล์ที่แตะ: backend/app/his/client.py, backend/app/main.py, backend/tests/test_his_lookup.py
- ต้องทำหลัง: T-01, T-02
- เสร็จเมื่อ: GET /patients/lookup รับเลขบัตรประชาชนแล้วคืน hn กลับมา โดยไม่มีการบันทึกเลขบัตรประชาชนลงฐานข้อมูลของระบบนี้
- สถานะ: พร้อมทำ

### T-10 ออกหมายเลขคิวตามรูปแบบที่กำหนด
- รองรับ: FR-BKG-04
- ตรวจด้วย: ไม่มี AC ตรง ๆ ที่ตรวจรูปแบบเลขคิว (ต้องรอ Q-02 ก่อนจึงจะกำหนด AC/test ได้)
- ไฟล์ที่แตะ: backend/app/booking/service.py
- ต้องทำหลัง: T-04
- เสร็จเมื่อ: -
- สถานะ: รอ Q-02

### T-11 ทดสอบประสิทธิภาพการค้นหาช่วงเวลาว่าง (ย่อส่วน)
- รองรับ: NFR-PERF-01
- ตรวจด้วย: AC-BKG-05
- ไฟล์ที่แตะ: backend/tests/test_AC_BKG_05.py
- ต้องทำหลัง: T-03
- เสร็จเมื่อ: test_AC_BKG_05 รันแล้วรายงานค่า p95 ของการยิง GET /slots พร้อมกันแบบย่อส่วนในสภาพแวดล้อม Codespace (ทีมต้องตัดสินใจภายหลังว่าผลจริงต้องวัดซ้ำบนเครื่องทดสอบที่รองรับผู้ใช้ 200 คน)
- สถานะ: พร้อมทำ

### T-12 หน้าเลือกแพ็กเกจและช่วงเวลา (SlotPicker)
- รองรับ: FR-BKG-01, FR-BKG-06
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-12
- ไฟล์ที่แตะ: frontend/src/pages/SlotPicker.jsx, frontend/src/api/client.js, frontend/src/App.jsx, frontend/src/__tests__/SlotPicker.test.jsx
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: หน้าจอเรียก API จำลอง GET /slots แสดงรายการช่วงเวลาว่างพร้อมที่นั่งคงเหลือ และเปลี่ยนแพ็กเกจแล้วโหลดช่วงเวลาใหม่
- สถานะ: พร้อมทำ

### T-13 หน้ายืนยันการจอง และแจ้ง "ช่วงเวลาเต็ม" พร้อม 3 ตัวเลือก (ConfirmBooking)
- รองรับ: FR-BKG-03, FR-BKG-04
- ตรวจด้วย: AC-BKG-03
- ไฟล์ที่แตะ: frontend/src/pages/ConfirmBooking.jsx, frontend/src/App.jsx, frontend/src/__tests__/AC-BKG-03.test.jsx
- ต้องทำหลัง: T-12
- เสร็จเมื่อ: AC-BKG-03.test.jsx ผ่าน
- สถานะ: พร้อมทำ

### T-14 หน้าแสดงผลการจองและหมายเลขคิว (BookingResult)
- รองรับ: FR-BKG-04, FR-BKG-05
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-14
- ไฟล์ที่แตะ: frontend/src/pages/BookingResult.jsx, frontend/src/App.jsx, frontend/src/__tests__/BookingResult.test.jsx
- ต้องทำหลัง: T-13
- เสร็จเมื่อ: หน้าจอแสดงหมายเลขคิวจากผลการจอง แม้ API จำลองตอบว่าส่งข้อความแจ้งเตือนไม่สำเร็จ
- สถานะ: พร้อมทำ

### T-15 ต่อหน้าจอกับ API จริง
- รองรับ: FR-BKG-01, FR-BKG-03
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-15
- ไฟล์ที่แตะ: frontend/src/api/client.js
- ต้องทำหลัง: T-03, T-06, T-12, T-13
- เสร็จเมื่อ: หน้าจอเรียกหลังบ้านจริงผ่าน /api แทน API จำลอง และแสดงข้อมูลช่วงเวลาว่างและผลการจองถูกต้องเมื่อรันหลังบ้านและหน้าจอพร้อมกัน
- สถานะ: พร้อมทำ

## ตารางตรวจความครบ

### 1. AC ID | task ที่ตรวจ AC นี้
| AC ID | task ที่ตรวจ |
|---|---|
| AC-BKG-01 | T-04 |
| AC-BKG-02 | T-05 |
| AC-BKG-03 | T-06 (หลังบ้าน), T-13 (หน้าจอ) |
| AC-BKG-04 | T-07 |
| AC-BKG-05 | T-11 |
| AC-BKG-06 | T-08 |

### 2. Constraint ID | task ที่ทำให้เป็นจริง
| Constraint ID | task |
|---|---|
| CON-TECH-01 | T-01 |
| DOM-PDPA-01 | T-01, T-08 |
| IF-IDP-01 | T-02 |
| IF-HIS-01 | T-01, T-09 |
| IF-NOT-01 | T-07 |

## สิ่งที่ยังไม่ทำ
- Q-02 หมายเลขคิวรีเซ็ตรายวัน หรือนับต่อเนื่อง และมีรูปแบบอย่างไร (เช่น A001)? -> ถามเจ้าหน้าที่เวชระเบียน (ยังไม่ได้คำตอบ)
  รอที่: T-10 (ออกหมายเลขคิวตามรูปแบบที่กำหนด) ยังทำไม่ได้จนกว่าจะได้คำตอบ
