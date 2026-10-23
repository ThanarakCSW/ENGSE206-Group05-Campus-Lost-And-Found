# ใบส่งงานสอบปลายภาค — ส่วน ก งานกลุ่ม (Change-to-Design)

| รายการ | กรอก |
|---|---|
| กลุ่ม / Case | กลุ่ม 2 · Case 05 |
| ชื่อระบบ | Campus Lost and Found — ระบบแจ้งของหายและของที่พบภายในมหาวิทยาลัย |
| CR เสริมที่เลือก | CR-FX-02B — เวลาพัฒนารุ่นแรกเหลือครึ่งหนึ่ง |
| Branch | `final-exam` |
| Pull Request | `submit(final): change-to-design take-home` — ยังไม่ได้เปิด PR |
| Commit hash สุดท้าย (ก่อน T0 + 24 ชั่วโมง) | รอยืนยันการส่งล่าช้ากับอาจารย์ (HEAD ที่ตรวจพบ: `455e2b9151d1b006d9f3d20b573d2800aba57802`) |
| สถานะ SRS ที่ใช้เป็นฐาน | Draft v0.1 — ยังไม่ได้รับการอนุมัติ |

## งานเดิมที่ใช้เป็นฐาน

| งาน | ไฟล์และ Commit หรือวันที่ |
|---|---|
| SRS (W07) | `docs/07-srs-v1.md` — Draft v0.1, Commit `dc87cd1d0562` (22/09/2569) |
| งาน W08 (Review · Trace · CR) | `docs/08-validation-traceability.md` — Commit `2a4060d26a6c` (18/08/2569) ใช้ข้อมูล Review, Traceability และ Change Request โดยไม่อ้างสถานะ Approved |
| Design Strategy + Design Spine (W10) | `design/10-design-strategy.md` — Template เดิม (07/07/2569) ยังไม่มี Design Spine ฉบับสมบูรณ์ จึงจัดทำข้อเสนอใหม่ใน G3 |
| Conceptual Architecture (W11) | `design/11-conceptual-architecture.md` — Template เดิม (07/07/2569) จึงจัดทำ Context และ Container Diagram ใหม่ใน G4 |

## ไฟล์ที่ส่ง

- [x] `final-exam/final-exam-group-answer.docx`
- [x] `final-exam/diagrams/context-after.drawio` + `.png`
- [x] `final-exam/diagrams/container-after.drawio` + `.png`
- [x] `final-exam/final-exam-submission.md` (ไฟล์นี้)
- [x] `final-exam/ai-use-log.md`

หมายเหตุ: ตรวจพบไฟล์ทั้งหมดใน Repository แล้ว แต่ยังต้องตรวจความถูกต้องของเนื้อหาและ Diagram ฉบับสุดท้ายร่วมกัน

## สมาชิกและส่วนที่รับผิดชอบ

| ชื่อ–สกุล | รหัสนักศึกษา | รับผิดชอบ (G / ข้อ) | หลักฐาน (Commit หรือส่วนในไฟล์) |
|---|---|---|---|
| นายนรบดี บุญเลิศ | 68543210013-7 | จัดทำและรวบรวมเอกสารคำตอบ G1–G6 วิเคราะห์ Change Request, Requirement, Model และ Design Strategy | Commit `1bab91875d71`, `4504a3a31a3a`, `455e2b9151d1` |
| นายธนรัก ชุ่มสวัสดิ์ | 68543210018-6 | จัดทำ C4 Context Diagram และ Container Diagram สำหรับ G4 พร้อมตรวจความสอดคล้องกับข้อกำหนดของระบบ | Commit `61326ee2c660` (Diagram), `bb6d90a7eaa5` (AI Use Log) |

## รับรอง

- [x] สมาชิกทุกคนอ่านคำตอบทั้งฉบับ และสามารถอธิบายส่วนใดก็ได้ใน Oral Spot-check
- [x] ตรวจแล้วว่าไม่มีตัวเลข นโยบาย หรือ Protocol ที่แต่งขึ้น โดยค่าที่ยังไม่ทราบเป็น TBD และมี Open Issue หรือ Open Decision รองรับ
- [x] ตรวจแล้วว่าเอกสารคำตอบไม่อ้างว่า SRS หรือ CR ได้รับ Approved
- [x] ไม่ได้แก้ไฟล์งานเดิมของแต่ละสัปดาห์ — การเปลี่ยนแปลงใน branch `final-exam` อยู่ภายในโฟลเดอร์ `final-exam/`

**สถานะ:** รอการตรวจสอบเนื้อหาและ Diagram ร่วมกันก่อนส่ง Pull Request