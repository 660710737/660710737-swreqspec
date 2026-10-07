# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md SPEC-BKG-001 Draft v2 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-07 15.56 | test: 8 ผ่าน 1 ไม่ผ่าน (หลังบ้าน 7/7 ผ่าน, หน้าจอ 1 ผ่าน 1 ไม่ผ่าน 1 todo)

ผล test ที่รัน
- หลังบ้าน `cd backend && pytest -v`: 7 passed
  - test_AC_BKG_01, test_TC_BKG_01_1_booking_success_and_seats_zero, test_TC_BKG_01_2_full_slot_rejects_booking, test_TC_BKG_01_3_not_verified, test_AC_BKG_05, test_T01_tables_created, test_T01_no_national_id
- หน้าจอ `cd frontend && npm test`: setup.test.jsx ผ่าน, TC-BKG-01-1.test.jsx เป็น todo (รอ Q-02), TC-BKG-01-2.test.jsx ไม่ผ่าน เพราะยังไม่มี pages/ConfirmBooking.jsx (T-11 ยังไม่ได้ทำ ไม่ใช่บั๊ก)

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 (ตรวจแค่ความเร็ว) | T-02 เสร็จ, T-10 พร้อมทำ | slots/router.py: get_slots, slots/service.py: list_available_slots | test_AC_BKG_05 (ผ่าน) ไม่ตรวจช่วง 30 วัน และที่นั่งคงเหลือ | ช่องโหว่ (F-04, F-06, F-10) |
| FR-BKG-02 | AC-BKG-02 | T-04 พร้อมทำ | ไม่มี | ไม่มี | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 พร้อมทำ | มีบางส่วน: booking/router.py ตอบ 409 "ช่วงเวลาเต็ม" แต่ยังไม่เสนอ 3 ช่วง | test_TC_BKG_01_2 (ผ่าน) ตรวจเฉพาะ "ไม่สร้างรายการจอง" | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03 เสร็จ, T-06 รอ Q-02 | booking/router.py: create_booking, booking/service.py: create_booking, next_queue_no | test_AC_BKG_01, test_TC_BKG_01_1, _2, _3 (ผ่านทั้งหมด) ส่วน "แสดงหมายเลขคิว" รอ Q-02 | ช่องโหว่ (F-05, F-08, F-11) |
| FR-BKG-05 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มี | ไม่มี | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-02 เสร็จ, T-10 พร้อมทำ | slots/service.py: list_available_slots (กรอง package_code) | ไม่มี test ที่เปลี่ยนแพ็กเกจ | ช่องโหว่ (F-09) |
| NFR-PERF-01 | AC-BKG-05 | T-02 เสร็จ | slots/router.py: get_slots | test_AC_BKG_05 (ผ่าน) เรียกทีละครั้ง ไม่ใช่พร้อมกัน | ช่องโหว่ (F-07) |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่มี | ไม่มี | ช่องโหว่ (F-12) |
| NFR-REL-02 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มี | ไม่มี | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่มี | ไม่มี | ช่องโหว่ (F-13) |
| CON-TECH-01 | ไม่มี AC (Constraint) | T-01 เสร็จ | config.py: DATABASE_URL, db/session.py, requirements.txt มี psycopg | test_T01_tables_created (ผ่าน บน SQLite) | ครบ |
| DOM-PDPA-01 | AC-BKG-06 | T-01 เสร็จ (ตาราง), T-08 พร้อมทำ | db/models.py: AuditLog (มีตาราง ยังไม่มีการบันทึก) | ไม่มี | ยังไม่ถึง |
| IF-IDP-01 | ไม่มี AC ตรง (อยู่ใน Given ของ AC-BKG-01) | T-03 เสร็จ | auth/idp.py: get_verified_hn | test_TC_BKG_01_3_not_verified (ผ่าน) | ช่องโหว่ (F-02) |
| IF-HIS-01 | ไม่มี AC | T-01 เสร็จ, T-09 พร้อมทำ | db/models.py: Booking (ไม่มี national_id) | test_T01_no_national_id (ผ่าน) | ช่องโหว่ (F-01) |
| IF-NOT-01 | ไม่มี AC ตรง (AC-BKG-04) | T-07 พร้อมทำ | ไม่มี | ไม่มี | ยังไม่ถึง |

สรุป: ครบ 1 / ยังไม่ถึง 6 / รอ 0 / ช่องโหว่ 8 (รวม 15 ID)

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| GET /slots (slots/router.py: get_slots) | FR-BKG-01, FR-BKG-06 | ตรงบางส่วน | อยู่ใน plan.md ข้อ 4 แต่แสดงล่วงหน้าแค่ 14 วัน (F-04) |
| slots/service.py: DAYS_AHEAD = 14 | FR-BKG-01 | ไม่ตรง | FR-BKG-01 กำหนด 30 วัน (F-04) |
| slots/service.py: date.today() | FR-BKG-01 | ไม่ระบุเขตเวลา | ASM-02 กำหนด Asia/Bangkok (F-10) |
| POST /bookings (booking/router.py: create_booking) | FR-BKG-04, IF-IDP-01 | ตรง ยกเว้นฟิลด์ national_id | อยู่ใน plan.md ข้อ 4 ซึ่ง input มีแค่ slot_id (F-01) |
| BookingRequest.national_id + logger.info(... national_id) | ไม่มี | ขัด IF-HIS-01 | รับเลขบัตรแล้วเขียนลง log (F-01) |
| response queue_no | FR-BKG-04 | เดา Q-02 | (F-05) |
| DELETE /bookings/{id} (booking/router.py: cancel_booking) | FR-BKG-04 | ไม่ตรง | ยกเลิกคิวคือ UC-02 อยู่ใน Out of scope ไม่อยู่ใน plan.md ข้อ 4 (F-03) |
| booking/service.py: create_booking | FR-BKG-04 | ตรง (บันทึก ตัดที่นั่ง) | ยังไม่ส่งคำขอส่งข้อความยืนยัน (รอ T-07); ไม่ล็อกแถว slot ถ้าสองคนยืนยันพร้อมกันอาจจองเกินได้ ควรตรวจตอนทำ T-05 / AC-BKG-03 |
| booking/service.py: next_queue_no (A001 รีเซ็ตรายวัน) | FR-BKG-04 | เดา Q-02 | (F-05) |
| booking/service.py: cancel_booking | FR-BKG-04 | ไม่ตรง | อยู่ใน Out of scope (F-03) |
| auth/idp.py: get_verified_hn | IF-IDP-01 | ไม่ตรง | เชื่อ token จาก client โดยไม่ถามระบบยืนยันตัวตน (F-02) |
| config.py: DATABASE_URL ค่าเริ่มต้น sqlite:///./dev.db | CON-TECH-01 | ตรงถ้าตั้งตัวแปร | ถ้าลืมตั้ง DATABASE_URL ในระบบจริง จะใช้ SQLite โดยไม่มีอะไรเตือน |
| db/models.py: Slot, Booking, AuditLog | FR-BKG-01, FR-BKG-04, DOM-PDPA-01, IF-HIS-01 | ตรง | ตรงกับ plan.md ข้อ 3 |
| main.py: lifespan create_all | CON-TECH-01 | ตรง | |
| frontend/src/api/client.js: createBooking | FR-BKG-04 (T-12) | ยังไม่ถึง | ไม่ส่ง Authorization จะได้ 401 เสมอ ต้องทำใน T-12 |
| frontend/src/App.jsx, main.jsx | ไม่มี | โครงเริ่มต้นของรายวิชา | ไม่ใช่ของแถม |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-01 | ละเมิด Constraint | backend/app/booking/router.py:19, 25 | IF-HIS-01 (และหลัก PDPA) | POST /bookings รับฟิลด์ `national_id` แล้วเขียนเลขบัตรประชาชนลง log ทุกคำขอ ทั้งที่ IF-HIS-01 ให้ใช้เลขบัตรแค่ค้น HN และไม่เก็บ ส่วน plan.md ข้อ 4 กำหนด input ของ POST /bookings เป็นแค่ slot_id (เลขบัตรไปทาง GET /patients/lookup) แนวทาง: ลบฟิลด์และลบออกจาก log | |
| F-02 | ละเมิด Constraint | backend/app/auth/idp.py:13-15 | IF-IDP-01 | ไม่ได้รับผลจากระบบยืนยันตัวตนจริง แค่เชื่อ header `Bearer verified:<HN>` ที่ client ส่งมา ใครก็พิมพ์ HN คนอื่นแล้วจองแทนได้ คอมเมนต์ในโค้ดบอกเองว่าเป็นตัวจำลอง แต่ T-03 ถูกปิดเป็น "เสร็จ" ทีมต้องตัดสินว่ายอมรับตัวจำลองในเฟสนี้ หรือเพิ่ม task เชื่อมระบบจริง | |
| F-03 | โค้ดไม่มี FR | backend/app/booking/router.py:35-41, backend/app/booking/service.py:42-50 | Out of scope (UC-02), FR-BKG-04 | DELETE /bookings/{id} ยกเลิกการจองและคืนที่นั่ง **อยู่ใน Out of scope** ("ยกเลิก / เลื่อนคิว (UC-02)") ไม่อยู่ใน plan.md ข้อ 4 และไม่มี task แต่คอมเมนต์อ้าง FR-BKG-04 ซึ่งพูดถึงการยืนยันจอง ไม่ใช่การยกเลิก (อ้าง ID ผิดเรื่องด้วย) ไม่มี test | |
| F-04 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py:10 | FR-BKG-01 | `DAYS_AHEAD = 14` แต่ FR-BKG-01 กำหนดให้แสดง "ภายใน 30 วันข้างหน้า" ผู้ใช้จะไม่เห็นช่วงเวลาวันที่ 15-30 ไม่มี test ไหนจับได้ (ดู F-06) | |
| F-05 | เดา Q-02 | backend/app/booking/service.py:13-18, 34 | Q-02, plan.md ข้อ 3 และ 8 | `next_queue_no` ออกเลขรูปแบบ A001 และนับใหม่ทุกวัน ซึ่งคือการหยิบ "ตัวอย่าง" ในวงเล็บของ Q-02 มาใช้เป็นคำตอบ ทั้งที่ Q-02 ยังไม่ได้คำตอบ และ plan.md บอกว่ายังไม่กำหนดวิธีออกเลข POST /bookings ก็ส่ง queue_no นี้ออกไปแล้ว | |
| F-06 | FR ไม่มี AC | spec.md FR-BKG-01, AC-BKG-05 | FR-BKG-01 | AC เดียวที่อ้าง FR-BKG-01 (ผ่านตาราง Traceability) คือ AC-BKG-05 ซึ่งตรวจแค่ความเร็ว ไม่มี AC ตรวจว่า "แสดงช่วงเวลาภายใน 30 วัน พร้อมที่นั่งคงเหลือ" F-04 จึงหลุดมาได้ ควรเสนอ AC ใหม่ (เป็นคำถามต่อทีม) | |
| F-07 | test อ่อน | backend/tests/test_AC_BKG_05.py:11-14 | AC-BKG-05 | Given คือ "ผู้ใช้พร้อมกัน 200 คน" แต่ test เรียก GET /slots ทีละครั้ง 200 ครั้งต่อกัน ไม่มีการเรียกพร้อมกัน และมีข้อมูลแค่ 10 ช่วงบน SQLite ผลจึงบอกไม่ได้ว่า p95 ≤ 2 วินาที ตอนมีคนใช้พร้อมกัน (plan.md ข้อ 6 ระบุว่าผลจริงต้องวัดบนเครื่องทดสอบ ยังไม่มีบันทึกว่าวัดแล้ว) | |
| F-08 | AC ไม่มี test | specs/001-booking/test-cases.md แถว TC-BKG-01-1, TC-BKG-01-2 | AC-BKG-01 | แถว "ใช้ได้" ระบุชื่อ test `test_TC_BKG_01_1_last_seat` และ `test_TC_BKG_01_2_no_seat_left` แต่ในโค้ดไม่มีชื่อนี้ (test ที่ตรวจเรื่องเดียวกันมีอยู่ในชื่อเดิม `..._booking_success_and_seats_zero` และ `..._full_slot_rejects_booking`) ตามรอยด้วยชื่อไม่ได้ ต้องทำให้ชื่อตรงกัน | |
| F-09 | FR ไม่มี AC | spec.md FR-BKG-06 | FR-BKG-06 | FR-BKG-06 (เปลี่ยนแพ็กเกจแล้วคำนวณช่วงว่างใหม่) ไม่มี AC เลย (plan.md ข้อ 6 ก็ระบุไว้) โค้ดกรอง package_code มีอยู่แล้วแต่ไม่มี test ไหนเปลี่ยนแพ็กเกจ | |
| F-10 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py:15 | ASM-02 | ใช้ `date.today()` ตามเขตเวลาของเครื่อง ไม่ใช่ Asia/Bangkok ถ้าเครื่องเป็น UTC ช่วง 00.00-07.00 น. ไทย "วันนี้" จะเป็นวันก่อนหน้า ทำให้ช่วง 30 วันเลื่อนไป 1 วัน | |
| F-11 | test อ่อน | backend/tests/test_AC_BKG_01.py:6-12 | AC-BKG-01 | `test_AC_BKG_01` assert แค่ `status_code == 201` ไม่ดูว่าบันทึกจริงหรือที่นั่งเหลือ 0 (ตอนนี้ TC-BKG-01-1 ตรวจส่วนนี้แทนแล้ว ถ้ามีแค่ test นี้ ลบบรรทัด `slot.remaining -= 1` ไปก็ยังผ่าน) | |
| F-12 | FR ไม่มี AC | spec.md NFR-SEC-01 | NFR-SEC-01 | TLS 1.2 ขึ้นไป ไม่มี AC ไม่มี task และไม่มีอะไรใน plan.md ไม่มีใครรับผิดชอบ | |
| F-13 | FR ไม่มี AC | spec.md NFR-USE-01 | NFR-USE-01 | การทดสอบกับอาสาสมัคร 10 คน (8/10 จองสำเร็จใน 3 นาที) ไม่มี AC และไม่มี task ต้องเป็นการทดสอบโดย "คน" | |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| (ยังไม่มี rtm.md รอบก่อน) | บั๊กจองได้เมื่อเหลือ 0 ที่ ถูกแก้ก่อน /verify รอบนี้ (service.py:26 เป็น `<= 0`) | test_TC_BKG_01_2_full_slot_rejects_booking ผ่าน (commit db7c9f1) |
