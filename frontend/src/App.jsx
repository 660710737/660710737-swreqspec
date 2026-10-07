import SlotPicker from './pages/SlotPicker'

// หน้าจอของแต่ละ task อยู่ใน src/pages/ ตาม tasks.md
export default function App() {
  return (
    <main className="mx-auto max-w-2xl p-6">
      <h1 className="text-2xl font-bold text-teal-800">ระบบจองคิวตรวจสุขภาพ</h1>
      <SlotPicker />
    </main>
  )
}
