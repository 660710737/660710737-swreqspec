// T-12 เสร็จเมื่อ: หน้าจอเรียก API จำลอง GET /slots แสดงรายการช่วงเวลาว่างพร้อมที่นั่งคงเหลือ
// และเปลี่ยนแพ็กเกจแล้วโหลดช่วงเวลาใหม่ (FR-BKG-01, FR-BKG-06)
import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import SlotPicker from '../pages/SlotPicker.jsx'

test('แสดงช่วงเวลาว่างพร้อมที่นั่งคงเหลือของแพ็กเกจเริ่มต้น', async () => {
  render(<SlotPicker />)

  await waitFor(() => {
    expect(screen.getByText(/2569-09-24 09:00 น\. — เหลือ 5 ที่/)).toBeTruthy()
  })
  expect(screen.getByText(/2569-09-24 10:00 น\. — เหลือ 0 ที่/)).toBeTruthy()
})

test('เปลี่ยนแพ็กเกจแล้วโหลดช่วงเวลาใหม่ตามแพ็กเกจที่เลือก', async () => {
  render(<SlotPicker />)

  await waitFor(() => {
    expect(screen.getByText(/2569-09-24 09:00 น\. — เหลือ 5 ที่/)).toBeTruthy()
  })

  fireEvent.change(screen.getByLabelText('แพ็กเกจ'), { target: { value: 'PREMIUM' } })

  await waitFor(() => {
    expect(screen.getByText(/2569-09-24 13:00 น\. — เหลือ 3 ที่/)).toBeTruthy()
  })
  expect(screen.queryByText(/2569-09-24 09:00 น\. — เหลือ 5 ที่/)).toBeNull()
})
