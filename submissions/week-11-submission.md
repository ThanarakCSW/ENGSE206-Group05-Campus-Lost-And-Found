# Week 11 Submission — Conceptual Architecture

| Field | Value |
|---|---|
| Assignment ID / Version | W11-v1.1 |
| Assignment URL | https://github.com/se-rmutl/engse206-lab/blob/main/weeks/week-11-conceptual-architecture/assignment-contract.md |
| Case ID / URL | Case 05 — ระบบแจ้งของหาย-พบของในมหาวิทยาลัย (Campus Lost and Found) · ดู `CASE_CARD.md` |
| Team | Group 05 — ENGSE206-Group05-Campus-Lost-And-Found |
| Submission commit hash | `ba193bc` |

## Artefact links

| Artefact | Path | สถานะ |
|---|---|---|
| Conceptual Architecture (Word) | `design/11-conceptual-architecture-v0.1.docx` | Design Draft |
| Context diagram | `diagrams/architecture/11-context.drawio` + `.png` | C4 ระดับ 1 · = ภาพที่ 2 ในไฟล์ Word |
| Container diagram | `diagrams/architecture/11-container.drawio` + `.png` | C4 ระดับ 2 · = ภาพที่ 3 ในไฟล์ Word |
| Design Spine | `design/00-design-spine.md` | W11 column filled |
| สรุปแบบ .md (ไม่บังคับ) | `design/11-conceptual-architecture.md` | สรุป + ลิงก์ (ถือไฟล์ Word เป็นหลัก) |
| Evidence: ภาพ frame Miro ก่อน/หลังแก้ | `evidence/week-11/w11-miro-before.png` · `w11-miro-after.png` | ก่อนแก้ 29 ก.ย. (มี sticky) · หลังแก้ 5 ต.ค. (DEC-01 แก้แล้ว + คำตอบทุกใบ) |
| Worklog | `project-management/team-worklog.md` | อัปเดตแล้ว (W11 ทุกคน) |
| AI use log (ถ้าใช้) | `project-management/ai-use-log.md` | 1 รายการ (จัดโครงเอกสารและไดอะแกรม) |

## Done checklist

- [x] Context diagram: ระบบ 1 กล่อง + actor ครบ + ระบบภายนอกพร้อมป้าย Core / Extension / TBD
- [x] Container diagram: ทุก container มีชื่อ + [ชนิด · เทคโนโลยี] + หน้าที่; ลูกศรทุกเส้นบอกว่าส่งอะไร
- [x] ตาราง container บอกสภาพแวดล้อม (รันที่ไหน ใครควบคุม) และข้อมูลที่เก็บ
- [x] NFR ทุกข้อชี้ได้ว่ากระทบ container ไหน หรือเป็น TBD; decision card ≤ 3 ใบอ้าง NFR/driver
- [x] ทุกขั้น Build now/Overview ใน Spine เดินผ่าน container ได้ และกติกา D1–D3 อยู่ฝั่ง server
- [x] ใช้ stack อ้างอิง หรือมี decision card เมื่อเปลี่ยน; ไม่มีเทคโนโลยีเกินจำเป็น; ทุกภาพมี .drawio + PNG

> decision card จาก NFR/driver มี 3 ใบ (DEC-01–03) · DEC-04 เป็นใบ stack ที่ไม่บังคับ (ทีมใช้ stack อ้างอิง React · Node.js + Express · PostgreSQL) จึงไม่นับรวมใน 3 ใบ

## ข้อที่คู่บน Miro ถาม และทีมตอบ

| คำถาม / sticky | ทีมแก้หรือตอบอย่างไร |
|---|---|
| driver ที่ห้ามพลาดของทีม อยู่ container ไหน | D1 (Privacy Leak) และ D2 (Pending Gate) อยู่ที่ API Application เป็นหลัก โดย API มีตัวเซ็นเซอร์ภาพส่วนบุคคลและคุม State Guard ก่อนบันทึก Database transaction ส่วน D3 (Audit Log) API บันทึกคู่กับทุกการเปลี่ยนสถานะใน Database (PostgreSQL) |
| ✓ การแยก Public vs Private บน Web, API และ Storage ชัดเจนมาก สอดคล้องกับ PDPA (เขียว) | คงไว้ — ตรงกับ Done checklist ข้อ 2 |
| ! DEC-01 ควรอ้างถึง BR-CLF-01 เรื่องการเบลอร์ภาพ และ NFR-CLF-01 เรื่อง RBAC ให้ครบ (เหลือง) | **แก้แล้ว** — เพิ่มการอ้างถึง BR-CLF-01 ในช่อง 'เพราะ' ของ DEC-01 ทั้งในไฟล์ Word หัวข้อ 6 และไฟล์ Markdown เรียบร้อยแล้ว · ดู `w11-miro-after.png` |
| ? ถ้ามีคนอัปโหลดรูปภาพขนาดใหญ่มากหลายไฟล์พร้อมกัน ระบบจะป้องกันอย่างไร (ชมพู) | API Application มี File Size Validator ตรวจสอบ Content-Length จำกัดขนาดไฟล์เดี่ยว ≤ 10MB (CT-01) และมี Rate Limiter สกัดกั้น request ผิดปกติ โดยสตรีมไฟล์ตรงไปยัง Secure Object Storage |

## สิ่งที่ยังไม่แน่ใจ / ต้องการ feedback (1–3 ข้อ)

1. การเชื่อมต่อกับ Institutional Identity Service (EXT-01) ยังเป็น TBD (DD-01) — ในรุ่นแรกที่ใช้ Role Fixture เพื่อทดสอบ RBAC (NFR-CLF-01) ครบถ้วนเพียงพอต่อการตรวจรับสถาปัตยกรรมหรือไม่
2. การจัดเก็บไฟล์หลักฐานใน File Storage แบบ Private Bucket ที่ต้องเข้าถึงผ่าน Authorized API Stream มีแนวทางปฏิบัติด้าน Performance แนะนำเพิ่มเติมสำหรับภาพถ่ายจำนวนมากหรือไม่

## การมีส่วนร่วม

| สมาชิก | ทำส่วนใด (ระบุหัวข้อ/ภาพ) |
|---|---|
| ธนรัก ชุ่มสวัสดิ์ (`ThanarakCSW`) | หัวข้อ 1, 2 Context + ภาพที่ 2 `11-context` (W11-A) + หัวข้อ 5, 6 (DEC-01–04), 9–11 + รวมไฟล์ Word `design/11-conceptual-architecture-v0.1.docx` |
| นรบดี บุญเลิศ (`nara-bodee`) | หัวข้อ 3–4 Container + ภาพที่ 3 `11-container` (W11-B) + หัวข้อ 7 และคอลัมน์ W11 ใน `design/00-design-spine.md` + หัวข้อ 8 (DD-01–06) + frame Miro ก่อน/หลังแก้ใน `evidence/week-11/` + ใบส่งงานนี้ |
