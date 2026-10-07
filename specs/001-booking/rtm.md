# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md SPEC-BKG-001 Draft v2 (หมวด "หน้าจอ (UI)" เขียนว่าเพิ่มใน v3 แต่หัวไฟล์ยังเป็น Draft v2) | tasks.md | test-cases.md | mockups/UI-BKG-01, UI-BKG-02
สร้างด้วย /verify เมื่อ 2569-10-07 16.11 (รอบที่ 2) | test: 10 ผ่าน 1 ไม่ผ่าน (1 todo)

ผล test ที่รัน
- หลังบ้าน `cd backend && pytest -v`: 7 passed
  - test_AC_BKG_01, test_TC_BKG_01_1_booking_success_and_seats_zero, test_TC_BKG_01_2_full_slot_rejects_booking, test_TC_BKG_01_3_not_verified, test_AC_BKG_05, test_T01_tables_created, test_T01_no_national_id
- หน้าจอ `cd frontend && npm test`: 3 passed, 1 failed, 1 todo
  - ผ่าน: AC-BKG-03.test.jsx, SlotPicker.test.jsx, setup.test.jsx
  - todo: TC-BKG-01-1.test.jsx (รอ Q-02)
  - ไม่ผ่าน: TC-BKG-01-2.test.jsx (TypeError อ่าน slot_date ของ undefined) ดู F-19
- ไม่มีโฟลเดอร์ specs/000-shared จึงไม่มี Constraint ที่ใช้ร่วม
- plan.md ยังไม่มีตาราง "ค่าที่ตั้งได้" จึงตรวจชนิด "ตัวเลขฝังในโค้ด" เทียบกับตารางไม่ได้ (ตัวเลขที่เจอใส่ไว้ใน F-04, F-14)

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 (ตรวจแค่ความเร็ว) | T-02 เสร็จ, T-10 เสร็จ รอทีมตรวจ, T-12 พร้อมทำ | slots/router.py: get_slots, slots/service.py: list_available_slots, frontend/src/pages/SlotPicker.jsx | test_AC_BKG_05 (ผ่าน) ไม่ตรวจช่วง 30 วัน, ที่นั่งคงเหลือ หรือการแสดงรายวัน | ช่องโหว่ (F-04, F-06, F-10, F-17, F-18, F-22) |
| FR-BKG-02 | AC-BKG-02 | T-04 พร้อมทำ | ไม่มี | ไม่มี | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05 พร้อมทำ (หลังบ้าน), T-11 เสร็จ รอทีมตรวจ (หน้าจอ), T-12 พร้อมทำ | frontend/src/pages/ConfirmBooking.jsx: แสดง "ช่วงเวลาเต็ม" + 3 ตัวเลือก; หลังบ้านตอบ 409 แต่ยังไม่ส่งช่วงใกล้เคียง | AC-BKG-03.test.jsx (ผ่าน) ไม่ตรวจวันและเวลาของตัวเลือก; test_TC_BKG_01_2 (ผ่าน) | ช่องโหว่ (F-20) |
| FR-BKG-04 | AC-BKG-01 | T-03 เสร็จ, T-06 รอ Q-02 | booking/router.py: create_booking, booking/service.py: create_booking, next_queue_no, ConfirmBooking.jsx (สถานะจองสำเร็จ) | test_AC_BKG_01, test_TC_BKG_01_1, _2, _3 (ผ่าน); TC-BKG-01-1.test.jsx (todo รอ Q-02); TC-BKG-01-2.test.jsx (ไม่ผ่าน) | ช่องโหว่ (F-05, F-08, F-11, F-14, F-16, F-19) |
| FR-BKG-05 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มี | ไม่มี | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-02 เสร็จ, T-10 เสร็จ รอทีมตรวจ | slots/service.py (กรอง package_code), SlotPicker.jsx: useEffect โหลดใหม่เมื่อเปลี่ยนแพ็กเกจ | SlotPicker.test.jsx (ผ่าน) | ช่องโหว่ (F-09, F-21) |
| NFR-PERF-01 | AC-BKG-05 | T-02 เสร็จ | slots/router.py: get_slots | test_AC_BKG_05 (ผ่าน) เรียกทีละครั้ง ไม่ใช่พร้อมกัน | ช่องโหว่ (F-07) |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่มี | ไม่มี | ช่องโหว่ (F-12) |
| NFR-REL-02 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มี | ไม่มี | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่มี | ไม่มี | ช่องโหว่ (F-13) |
| CON-TECH-01 | ไม่มี AC (Constraint) | T-01 เสร็จ | config.py: DATABASE_URL, db/session.py, requirements.txt มี psycopg | test_T01_tables_created (ผ่าน บน SQLite) | ครบ |
| DOM-PDPA-01 | AC-BKG-06 | T-01 เสร็จ (ตาราง), T-08 พร้อมทำ | db/models.py: AuditLog (มีตาราง ยังไม่มีการบันทึก) | ไม่มี | ยังไม่ถึง |
| IF-IDP-01 | ไม่มี AC ตรง (อยู่ใน Given ของ AC-BKG-01) | T-03 เสร็จ | auth/idp.py: get_verified_hn | test_TC_BKG_01_3_not_verified (ผ่าน) | ช่องโหว่ (F-02) |
| IF-HIS-01 | ไม่มี AC | T-01 เสร็จ, T-09 พร้อมทำ | db/models.py: Booking (ไม่มี national_id) | test_T01_no_national_id (ผ่าน) | ช่องโหว่ (F-01) |
| IF-NOT-01 | ไม่มี AC ตรง (AC-BKG-04) | T-07 พร้อมทำ | ไม่มี | ไม่มี | ยังไม่ถึง |

สรุป: ครบ 1 / ยังไม่ถึง 5 / รอ 0 / ช่องโหว่ 9 (รวม 15 ID)

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| GET /slots (slots/router.py: get_slots) | FR-BKG-01, FR-BKG-06 | ตรงบางส่วน | อยู่ใน plan.md ข้อ 4 แต่แสดงล่วงหน้าแค่ 14 วัน (F-04) response ใช้ชื่อ `slot_id` |
| slots/service.py: DAYS_AHEAD = 14 | FR-BKG-01 | ไม่ตรง | FR-BKG-01 กำหนด 30 วัน (F-04) |
| slots/service.py: date.today() | FR-BKG-01 | ไม่ระบุเขตเวลา | ASM-02 กำหนด Asia/Bangkok (F-10) |
| POST /bookings (booking/router.py: create_booking) | FR-BKG-04, IF-IDP-01 | ตรง ยกเว้นฟิลด์ national_id | อยู่ใน plan.md ข้อ 4 ซึ่ง input มีแค่ slot_id (F-01) |
| BookingRequest.national_id + logger.info(... national_id) | ไม่มี | ขัด IF-HIS-01 | รับเลขบัตรแล้วเขียนลง log (F-01) |
| response queue_no | FR-BKG-04 | เดา Q-02 | (F-05) |
| booking/service.py: create_booking | FR-BKG-04 | ตรง (บันทึก ตัดที่นั่ง ปฏิเสธเมื่อเหลือ 0) | ยังไม่ส่งคำขอส่งข้อความยืนยัน (รอ T-07); ไม่ล็อกแถว slot ถ้าสองคนยืนยันพร้อมกันอาจจองเกินได้ ควรตรวจตอนทำ T-05 / AC-BKG-03 |
| booking/service.py: next_queue_no (A001 รีเซ็ตรายวัน) | FR-BKG-04 | เดา Q-02 | (F-05) |
| auth/idp.py: get_verified_hn | IF-IDP-01 | ไม่ตรง | เชื่อ token จาก client โดยไม่ถามระบบยืนยันตัวตน (F-02) |
| config.py: DATABASE_URL ค่าเริ่มต้น sqlite:///./dev.db | CON-TECH-01 | ตรงถ้าตั้งตัวแปร | ถ้าลืมตั้ง DATABASE_URL ในระบบจริง จะใช้ SQLite โดยไม่มีอะไรเตือน |
| db/models.py: Slot, Booking, AuditLog | FR-BKG-01, FR-BKG-04, DOM-PDPA-01, IF-HIS-01 | ตรง | ตรงกับ plan.md ข้อ 3 |
| main.py: lifespan create_all | CON-TECH-01 | ตรง | |
| frontend/src/App.jsx: เส้นทาง SlotPicker -> ConfirmBooking | T-10, T-11 | ไม่ตรง | onNext สร้าง slot ปลอม `slot_date: today, start_time: '09:00'` (F-14); today เป็นวันที่ UTC (F-22) |
| frontend/src/pages/SlotPicker.jsx (UI-BKG-01) | FR-BKG-01, FR-BKG-06 | ตรงบางส่วน | มีช่องแพ็กเกจบนสุดและแถบ 3 ขั้น ตรง; ข้อความ "ว่าง N" ไม่ใช่ "เหลือ N ที่" (F-18); ไม่มีการเลือกวันหรือแสดงวัน (F-17); รายการแพ็กเกจฝังในโค้ด (F-21); ใช้ `s.id` แต่หลังบ้านส่ง `slot_id` ต้องแก้ตอน T-12 |
| SlotPicker.jsx ปุ่ม "ถัดไป" | ปุ่มนำทาง | ตรง | spec หมวด UI ระบุว่าไม่ต้องมี FR |
| frontend/src/pages/ConfirmBooking.jsx (UI-BKG-02) สถานะปกติและสถานะเต็ม | FR-BKG-03, FR-BKG-04 | ตรง | ปุ่ม "ยืนยันการจอง" ข้อความ "ช่วงเวลาเต็ม" และ 3 ตัวเลือกพร้อมวันและเวลา ตรงหมวด UI แล้ว (ปุ่มยกเลิกถูกลบใน working copy ยังไม่ commit) |
| ConfirmBooking.jsx สถานะจองสำเร็จ: "หมายเลขคิว {queue_no}" | FR-BKG-04 | เดา Q-02 | เป็นงานของ T-06 (รอ Q-02) (F-16) |
| ConfirmBooking.jsx ปุ่ม "กลับไปเลือกเวลา", "เลือกช่วงนี้" | ปุ่มนำทาง / FR-BKG-03 | ตรง | |
| ConfirmBooking.jsx สถานะ "มีคิวในวันเดียวกันแล้ว" ใน mockup | FR-BKG-02 | ยังไม่ถึง | T-04 ยังไม่ได้ทำ |
| frontend/src/api/client.js: getSlots, createBooking | FR-BKG-01, FR-BKG-04 | ยังไม่ถึง | createBooking ไม่ส่ง Authorization จะได้ 401 เสมอ ต้องทำใน T-12 |
| frontend/src/api/client.js: cancelBooking | ไม่มี | ไม่ตรง | **อยู่ใน Out of scope** (UC-02) และเรียก endpoint ที่หลังบ้านลบไปแล้ว (F-15) |
| mockups/UI-BKG-01: "แจ้งเตือนก่อนวันตรวจ 1 วัน" | ไม่มี | mockup เกิน spec | โค้ดไม่ได้ทำ ถูกต้อง (F-23) |
| โฟลเดอร์ซ้ำใน backend/ (backend/frontend/src, backend/specs, backend/docs, backend/.claude) | ไม่มี | ไม่ใช่โค้ดที่รันจริง | ถูก commit มาใน 9065260 "ui lab start" backend/frontend/src/pages/ConfirmBooking.jsx ยังมีปุ่มยกเลิกและ slice(0, 2) ทำให้ grep จากโฟลเดอร์ backend เจอผลซ้ำหรือผลเก่า ทีมควรตรวจว่าตั้งใจหรือไม่ |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / ตัวเลขฝังในโค้ด / อ้าง ID ผิดเรื่อง / ไม่ตรง mockup / mockup เกิน spec
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-01 | ละเมิด Constraint | backend/app/booking/router.py:19, 25 | IF-HIS-01 (และหลัก PDPA) | POST /bookings รับฟิลด์ `national_id` แล้วเขียนเลขบัตรประชาชนลง log ทุกคำขอ ทั้งที่ IF-HIS-01 ให้ใช้เลขบัตรแค่ค้น HN และไม่เก็บ ส่วน plan.md ข้อ 4 กำหนด input ของ POST /bookings เป็นแค่ slot_id (เลขบัตรไปทาง GET /patients/lookup) แนวทาง: ลบฟิลด์และลบออกจาก log | |
| F-02 | ละเมิด Constraint | backend/app/auth/idp.py:13-15 | IF-IDP-01 | ไม่ได้รับผลจากระบบยืนยันตัวตนจริง แค่เชื่อ header `Bearer verified:<HN>` ที่ client ส่งมา ใครก็พิมพ์ HN คนอื่นแล้วจองแทนได้ คอมเมนต์ในโค้ดบอกเองว่าเป็นตัวจำลอง แต่ T-03 ถูกปิดเป็น "เสร็จ" ทีมต้องตัดสินว่ายอมรับตัวจำลองในเฟสนี้ หรือเพิ่ม task เชื่อมระบบจริง | |
| F-14 | ตัวเลขฝังในโค้ด | frontend/src/App.jsx:17 | FR-BKG-04, UI-BKG-02 | เมื่อกด "ถัดไป" App สร้างข้อมูลช่วงเวลาเองเป็น `{ id, slot_date: today, start_time: '09:00' }` หน้ายืนยันจึงแสดง "วันนี้ 09.00 น." เสมอ ไม่ว่าผู้ใช้เลือกช่วงไหน แต่ส่ง id ของช่วงที่เลือกไปจองจริง ผู้ใช้จะยืนยันโดยเห็นวันเวลาที่ไม่ตรงกับที่จอง แนวทาง: ส่ง slot ทั้งก้อนจาก SlotPicker แทน id | |
| F-15 | โค้ดไม่มี FR | frontend/src/api/client.js:20-24 | Out of scope (UC-02) | `cancelBooking` เรียก `DELETE /bookings/{id}` **อยู่ใน Out of scope** ("ยกเลิก / เลื่อนคิว (UC-02)") ไม่อยู่ใน plan.md ข้อ 4 ไม่มี task และหลังบ้านลบ endpoint นี้ไปแล้ว (F-03) คอมเมนต์บอกว่าเพิ่มตอน T-11 เพื่อปุ่มยกเลิก ซึ่งถูกลบออกจาก ConfirmBooking.jsx แล้วใน working copy (ยังไม่ commit) | |
| F-04 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py:10 | FR-BKG-01 | `DAYS_AHEAD = 14` แต่ FR-BKG-01 กำหนดให้แสดง "ภายใน 30 วันข้างหน้า" ผู้ใช้จะไม่เห็นช่วงเวลาวันที่ 15-30 ไม่มี test ไหนจับได้ (ดู F-06) mockup UI-BKG-01 ก็เขียนว่า "ภายใน 30 วันข้างหน้า" | |
| F-05 | เดา Q-02 | backend/app/booking/service.py:13-18, 34 | Q-02, plan.md ข้อ 3 และ 8 | `next_queue_no` ออกเลขรูปแบบ A001 และนับใหม่ทุกวัน ซึ่งคือการหยิบ "ตัวอย่าง" ในวงเล็บของ Q-02 มาใช้เป็นคำตอบ ทั้งที่ Q-02 ยังไม่ได้คำตอบ และ plan.md บอกว่ายังไม่กำหนดวิธีออกเลข POST /bookings ก็ส่ง queue_no นี้ออกไปแล้ว | |
| F-16 | เดา Q-02 | frontend/src/pages/ConfirmBooking.jsx:14-21 | Q-02, spec หมวด UI, plan.md ข้อ 8, T-06 | หน้ายืนยันแสดงสถานะ "จองสำเร็จ หมายเลขคิว {queue_no}" ซึ่งจะแสดงเลขรูปแบบ A001 จาก F-05 spec หมวด UI เขียนว่า "รูปแบบหมายเลขคิวยังรอ Q-02 ... ห้ามเดารูปแบบ" และ plan.md ข้อ 8 บอกว่าการแสดงเลขคิวยังไม่สร้างจนกว่าจะได้คำตอบ หน้าผลการจองเป็นงานของ T-06 (รอ Q-02) | |
| F-17 | ไม่ตรง mockup | frontend/src/pages/SlotPicker.jsx:38-50 | FR-BKG-01, UI-BKG-01 | FR-BKG-01 ให้แสดงช่วงว่าง "ของแต่ละวัน" ภายใน 30 วัน mockup มีส่วนเลือกวัน แต่หน้าจอไม่มีการเลือกวัน และรายการแสดงแค่เวลา ไม่มีวันที่ ถ้าหลังบ้านส่งช่วงของหลายวันมา ผู้ใช้จะแยกไม่ออกว่าเป็นวันไหน (หน้าตาปุ่มเลือกวันยืดหยุ่นได้ แต่ต้องรู้ว่าช่วงเป็นของวันไหน) | |
| F-18 | ไม่ตรง mockup | frontend/src/pages/SlotPicker.jsx:46 | UI-BKG-01 (ต้องตรง) | แสดง `ว่าง {s.remaining}` แต่ spec หมวด UI ระบุว่าต้องตรง "เหลือ N ที่" SlotPicker.test.jsx ไม่ได้ตรวจข้อความนี้จึงหลุดมาได้ | |
| F-06 | FR ไม่มี AC | spec.md FR-BKG-01, AC-BKG-05 | FR-BKG-01 | AC เดียวที่อ้าง FR-BKG-01 (ผ่านตาราง Traceability) คือ AC-BKG-05 ซึ่งตรวจแค่ความเร็ว ไม่มี AC ตรวจว่า "แสดงช่วงเวลาภายใน 30 วัน พร้อมที่นั่งคงเหลือ" F-04, F-17, F-18 จึงหลุดมาได้ ควรเสนอ AC ใหม่ (เป็นคำถามต่อทีม) | |
| F-19 | AC ไม่มี test | frontend/src/__tests__/TC-BKG-01-2.test.jsx:12 | AC-BKG-01 (TC-BKG-01-2 ส่วนหน้าจอ) | test ส่ง props `client`, `slotId` แต่หน้าจอจริงรับ `api`, `slot` จึงล้มด้วย TypeError ก่อนถึง assert แถว TC-BKG-01-2 ที่ "ใช้ได้" จึงยังไม่มี test หน้าจอที่ทำงานจริง (test เขียนก่อนมีหน้าจอ โดยสมมติชื่อ props ไว้ ต้องแก้ test ให้ตรงหน้าจอ ไม่ใช่แก้หน้าจอ) | |
| F-07 | test อ่อน | backend/tests/test_AC_BKG_05.py:11-14 | AC-BKG-05 | Given คือ "ผู้ใช้พร้อมกัน 200 คน" แต่ test เรียก GET /slots ทีละครั้ง 200 ครั้งต่อกัน ไม่มีการเรียกพร้อมกัน และมีข้อมูลแค่ 10 ช่วงบน SQLite ผลจึงบอกไม่ได้ว่า p95 ≤ 2 วินาที ตอนมีคนใช้พร้อมกัน (plan.md ข้อ 6 ระบุว่าผลจริงต้องวัดบนเครื่องทดสอบ ยังไม่มีบันทึกว่าวัดแล้ว) | |
| F-20 | test อ่อน | frontend/src/__tests__/AC-BKG-03.test.jsx:18-20 | AC-BKG-03, UI-BKG-02 (ต้องตรง "3 ตัวเลือกพร้อมวันและเวลา") | test ตรวจข้อความ "ช่วงเวลาเต็ม" และจำนวนปุ่ม 3 ปุ่ม แต่ไม่ได้ตรวจว่าแต่ละตัวเลือกแสดงวันและเวลา ถ้าลบ `{a.slot_date}` ที่ ConfirmBooking.jsx:40 ออก test ก็ยังผ่าน หมายเหตุ: ฉบับที่ commit ไว้ (9065260) assert แค่ "เต็ม" และจำนวน > 0 ฉบับที่ assert "ช่วงเวลาเต็ม" และ 3 ยังอยู่ใน working copy ยังไม่ commit | |
| F-08 | AC ไม่มี test | specs/001-booking/test-cases.md แถว TC-BKG-01-1, TC-BKG-01-2 | AC-BKG-01 | แถว "ใช้ได้" ระบุชื่อ test `test_TC_BKG_01_1_last_seat` และ `test_TC_BKG_01_2_no_seat_left` แต่ในโค้ดไม่มีชื่อนี้ (test ที่ตรวจเรื่องเดียวกันมีอยู่ในชื่อเดิม `..._booking_success_and_seats_zero` และ `..._full_slot_rejects_booking`) ตามรอยด้วยชื่อไม่ได้ ต้องทำให้ชื่อตรงกัน | |
| F-09 | FR ไม่มี AC | spec.md FR-BKG-06 | FR-BKG-06 | FR-BKG-06 (เปลี่ยนแพ็กเกจแล้วคำนวณช่วงว่างใหม่) ไม่มี AC เลย (plan.md ข้อ 6 ก็ระบุไว้) รอบนี้มี SlotPicker.test.jsx ตรวจฝั่งหน้าจอแล้ว แต่หลังบ้านยังไม่มี test ที่เปลี่ยนแพ็กเกจ และไม่มี AC ให้ตรวจเทียบ | |
| F-21 | ตัวเลขไม่ตรง spec | frontend/src/pages/SlotPicker.jsx:4-7 | FR-BKG-06, spec หมวด UI ("ข้อมูลตัวอย่างทั้งหมด" ยืดหยุ่นได้) | รายการแพ็กเกจฝังในโค้ด (GEN "ตรวจสุขภาพทั่วไป", PRE "ตรวจสุขภาพก่อนเข้าทำงาน") ซึ่งคัดมาจากข้อมูลตัวอย่างใน mockup spec และ plan ไม่ได้บอกว่ามีแพ็กเกจอะไร หรือดึงมาจากไหน (test หลังบ้านใช้ "BASIC") จึงเป็นการตัดสินใจแทนทีม ควรถามว่ารายการแพ็กเกจมาจากที่ใด | |
| F-10 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py:15 | ASM-02 | ใช้ `date.today()` ตามเขตเวลาของเครื่อง ไม่ใช่ Asia/Bangkok ถ้าเครื่องเป็น UTC ช่วง 00.00-07.00 น. ไทย "วันนี้" จะเป็นวันก่อนหน้า ทำให้ช่วง 30 วันเลื่อนไป 1 วัน | |
| F-22 | ตัวเลขไม่ตรง spec | frontend/src/App.jsx:10 | ASM-02 | `new Date().toISOString().slice(0, 10)` เป็นวันที่ตาม UTC ไม่ใช่ Asia/Bangkok ช่วง 00.00-07.00 น. ไทย dateFrom ที่ส่งไป GET /slots จะเป็นเมื่อวาน (เรื่องเดียวกับ F-10 แต่ฝั่งหน้าจอ) | |
| F-11 | test อ่อน | backend/tests/test_AC_BKG_01.py:6-12 | AC-BKG-01 | `test_AC_BKG_01` assert แค่ `status_code == 201` ไม่ดูว่าบันทึกจริงหรือที่นั่งเหลือ 0 (ตอนนี้ TC-BKG-01-1 ตรวจส่วนนี้แทนแล้ว ถ้ามีแค่ test นี้ ลบบรรทัด `slot.remaining -= 1` ไปก็ยังผ่าน) | |
| F-12 | FR ไม่มี AC | spec.md NFR-SEC-01 | NFR-SEC-01 | TLS 1.2 ขึ้นไป ไม่มี AC ไม่มี task และไม่มีอะไรใน plan.md ไม่มีใครรับผิดชอบ | |
| F-13 | FR ไม่มี AC | spec.md NFR-USE-01 | NFR-USE-01 | การทดสอบกับอาสาสมัคร 10 คน (8/10 จองสำเร็จใน 3 นาที) ไม่มี AC และไม่มี task ต้องเป็นการทดสอบโดย "คน" | |
| F-23 | mockup เกิน spec | specs/001-booking/mockups/UI-BKG-01-select-slot.html ("แจ้งเตือนก่อนวันตรวจ 1 วัน") | ไม่มี FR | mockup มีตัวเลือกแจ้งเตือนก่อนวันตรวจ 1 วัน แต่ไม่มี FR หรือ AC ใดสั่ง (IF-NOT-01 พูดถึงข้อความยืนยันการจองเท่านั้น) โค้ดไม่ได้ทำ ซึ่งถูกต้อง ทีมควรถามผู้ใช้ว่าต้องการไหม ถ้าต้องการให้เพิ่ม FR ก่อน | |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| F-03 | ลบ `DELETE /bookings/{booking_id}` ใน backend/app/booking/router.py และ `cancel_booking` ใน backend/app/booking/service.py (commit c7020a2 "verify v1") | `grep -rn "@router\." backend/app` เหลือแค่ GET /slots และ POST /bookings; `grep cancel_booking backend/app` ไม่เจอ (ส่วนที่ยังเหลือฝั่งหน้าจอแยกเป็น F-15) |
| (ก่อน /verify รอบที่ 1) | บั๊กจองได้เมื่อเหลือ 0 ที่ ถูกแก้ (service.py:26 เป็น `<= 0`) | test_TC_BKG_01_2_full_slot_rejects_booking ผ่าน (commit db7c9f1) |
