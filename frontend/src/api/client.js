// FR-BKG-01, FR-BKG-06: API จำลองตามสัญญา GET /slots ใน plan.md ข้อ 4 (ต่อกับ API หลังบ้านจริงใน T-15)
const MOCK_SLOTS = [
  { id: 1, slot_date: '2569-09-24', start_time: '09:00', package_code: 'BASIC', remaining: 5 },
  { id: 2, slot_date: '2569-09-24', start_time: '10:00', package_code: 'BASIC', remaining: 0 },
  { id: 3, slot_date: '2569-09-25', start_time: '09:00', package_code: 'BASIC', remaining: 2 },
  { id: 4, slot_date: '2569-09-24', start_time: '13:00', package_code: 'PREMIUM', remaining: 3 },
  { id: 5, slot_date: '2569-09-25', start_time: '14:00', package_code: 'PREMIUM', remaining: 1 },
]

export async function fetchSlots({ packageCode }) {
  return MOCK_SLOTS.filter((slot) => slot.package_code === packageCode)
}
