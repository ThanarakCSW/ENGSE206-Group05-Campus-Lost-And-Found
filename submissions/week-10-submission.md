# Week 10 Submission — Design Strategy

| Field | Value |
|---|---|
| Assignment ID / Version | W10-v1.0 |
| Assignment URL | https://github.com/se-rmutl/engse206-lab/blob/main/weeks/week-10-design-strategy/assignment-contract.md |
| Case ID / URL | Case 05 — Campus Lost and Found · https://github.com/se-rmutl/engse206-lab/blob/main/cases/05-campus-lost-and-found.md |
| Team | Group 05 — ENGSE206-Group05-Campus-Lost-And-Found |
| Submission commit hash | `dc87cd1` / `main` |

## Artefact links

| Artefact | Path | สถานะ |
|---|---|---|
| Design Strategy | `design/10-design-strategy.md` | Design Draft |
| Design Spine | `design/00-design-spine.md` | W10 & W11 column filled (7 แถว) |
| Worklog | `project-management/team-worklog.md` | อัปเดตแล้ว |
| AI use log (ถ้าใช้) | `project-management/ai-use-log.md` | อัปเดตแล้ว |

## Done checklist

- [x] scope table 4 ระดับ ไม่ลบ FR จาก SRS
- [x] ทุกแถวมี requirement ID
- [x] drivers 3 ข้อ อ้าง ID + ผลต่อการออกแบบ
- [x] Spine 7 แถว มี actor + UC
- [x] open decisions ≤ 5 มีเจ้าของ/ผลกระทบ/ระหว่างรอ ไม่มีค่าที่แต่งขึ้น
- [x] สถานะ SRS ตามจริง

## สิ่งที่ยังไม่แน่ใจ / ต้องการ feedback (1–3 ข้อ)

1. ประเด็น Open Decision DD-01 เรื่องระยะเวลาตัดโอนสิ่งของตกค้าง (Unclaimed Items) กำหนดไว้ 30 วันเป็นค่าสมมติสำหรับการแสดงผลรายงานสรุปในสเต็ป Overview หากมีนโยบายระเบียบที่แน่นอนจากทางมหาวิทยาลัย จะสามารถปรับเปลี่ยนในขั้นตอน Detailed Design ได้โดยไม่กระทบต่อสถาปัตยกรรมหลักใช่หรือไม่
2. การเบลอร์ภาพถ่ายตาม BR-CLF-01 ในรุ่นแรก ทีมเลือกใช้การเบลอร์แบบ Manual โดยให้ผู้ใช้และเจ้าหน้าที่ตรวจสอบและเบลอร์ภาพก่อนเผยแพร่ เพื่อลดความซับซ้อนก่อนนำเข้า AI Auto-censor ใน Increment ถัดไป ขอคำแนะนำว่าเหมาะสมกับบริบทของวิชาหรือไม่

## การมีส่วนร่วม

| สมาชิก | ทำส่วนใด (ระบุแถว/ข้อ) |
|---|---|
| ธนรัก ชุ่มสวัสดิ์ | Design Strategy หัวข้อ 1, 2 (Scope 4 ระดับ), 3 (Design Drivers D1–D3) และข้อตกลงที่ต้องรักษาในหัวข้อ 5 |
| นรบดี บุญเลิศ | Design Spine 7 แถว ใน `design/00-design-spine.md`, Open Decisions (DD-01–DD-03) และใบส่งงานนี้ |
