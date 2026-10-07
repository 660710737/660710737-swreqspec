// TC-BKG-01-2 (AC-BKG-01, ขอบ) ส่วนหน้าจอ
// ใช้ client จำลองตามแนวทางใน src/api/client.js (ไม่ต้องรันหลังบ้านจริง)
import { render, screen } from '@testing-library/react'
import { test, expect } from 'vitest'
import ConfirmBooking from '../pages/ConfirmBooking.jsx'

test('TC-BKG-01-2 ช่วงเต็มแล้ว หน้าจอแจ้ง "ช่วงเวลาเต็ม"', async () => {
  // Given ยืนยันตัวตนแล้ว และช่วง 09.00 น. เหลือ 0 ที่ (หลังบ้านตอบ 409 ตาม plan.md ข้อ 4)
  const client = {
    createBooking: async () => ({ status: 409, body: { detail: 'ช่วงเวลาเต็ม' } }),
  }
  render(<ConfirmBooking client={client} slotId={1} />)

  // When ยืนยันการจองช่วง 09.00 น.
  screen.getByRole('button', { name: /ยืนยัน/ }).click()

  // Then 2) แจ้ง "ช่วงเวลาเต็ม"
  expect(await screen.findByText(/ช่วงเวลาเต็ม/)).toBeTruthy()
  // ช่วงใกล้เคียง: ยังไม่ assert เพราะ plan.md ข้อ 4 ไม่ได้กำหนดรูปแบบข้อมูลช่วงใกล้เคียงใน response
})
