import { useEffect, useState } from 'react'
import { fetchSlots } from '../api/client'

const PACKAGES = [
  { code: 'BASIC', label: 'แพ็กเกจพื้นฐาน' },
  { code: 'PREMIUM', label: 'แพ็กเกจพรีเมียม' },
]

// FR-BKG-01: แสดงช่วงเวลาว่างพร้อมที่นั่งคงเหลือ | FR-BKG-06: คำนวณช่วงเวลาว่างใหม่เมื่อเปลี่ยนแพ็กเกจ
export default function SlotPicker() {
  const [packageCode, setPackageCode] = useState(PACKAGES[0].code)
  const [slots, setSlots] = useState([])

  useEffect(() => {
    let active = true
    fetchSlots({ packageCode }).then((data) => {
      if (active) setSlots(data)
    })
    return () => {
      active = false
    }
  }, [packageCode])

  return (
    <section className="mt-6">
      <h2 className="text-lg font-semibold text-teal-800">เลือกแพ็กเกจและช่วงเวลา</h2>

      <label htmlFor="package-select" className="mt-4 block text-sm text-slate-600">
        แพ็กเกจ
      </label>
      <select
        id="package-select"
        value={packageCode}
        onChange={(e) => setPackageCode(e.target.value)}
        className="mt-1 rounded border border-slate-300 p-2"
      >
        {PACKAGES.map((pkg) => (
          <option key={pkg.code} value={pkg.code}>
            {pkg.label}
          </option>
        ))}
      </select>

      <ul className="mt-4 space-y-2">
        {slots.map((slot) => (
          <li key={slot.id} className="rounded border border-slate-200 p-2">
            {slot.slot_date} {slot.start_time} น. — เหลือ {slot.remaining} ที่
          </li>
        ))}
      </ul>
    </section>
  )
}
