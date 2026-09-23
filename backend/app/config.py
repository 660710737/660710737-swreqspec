import os

# CON-TECH-01: ฐานข้อมูลหลักคือ PostgreSQL แต่รับค่าต่อผ่านตัวแปรแวดล้อมเพื่อสลับฐานข้อมูลตอน test ได้โดยไม่แก้โค้ด
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql+psycopg://localhost/booking")
