# Week 05 Submission

- **Team / Case:** Group05 — Case 05: Campus Lost and Found
- **Repository URL:** `https://github.com/ThanarakCSW/ENGSE206-Group05-Campus-Lost-And-Found.git`
- **Submission commit:** Example commit message: `docs: prioritize functional and nonfunctional requirements`

## Artefact paths

- `docs/05-requirement-backlog.md`
- `docs/04-evidence-log.md`
- `evidence/week-05/README.md`
- `project-management/team-worklog.md`

## Prioritization Method

ทีมใช้ MoSCoW เพื่อจัดลำดับ requirement เพราะ template ของ Week 05 ต้องสรุป Must/Should/Could/Won't และเหมาะกับการแยก requirement ที่จำเป็นต่อปัญหาหลักออกจาก requirement ที่ยังต้องรอ validation

## What changed from Week 04

- แปลง Requirement Candidates จาก Week 04 ให้เป็น Functional Requirements ที่ระบุ acceptance measure ได้
- เพิ่ม Non-functional Requirements ด้าน usability, privacy, security, auditability, responsiveness, data quality และ maintainability
- เพิ่ม Business Rules/Constraints เพื่อควบคุม privacy, proof visibility, status tracking, unclaimed item policy และ scope boundary
- จัดลำดับ requirement ตามหลักฐาน E-ID และสถานะ negotiation โดยให้เรื่องระบบกลาง การยืนยันความเป็นเจ้าของ และ PDPA เป็น Must

## Readiness note for Week 06

Backlog มี FR/NFR พร้อม priority และ acceptance measure แล้ว สามารถนำไปต่อยอดเป็น user stories, use cases, activity/state model และ requirement model ใน Week 06 ได้ โดยต้องรักษา ID ของ requirement เพื่อให้ trace กลับมายัง evidence และ backlog ได้

## Question for instructor

> สำหรับ requirement เรื่องการจัดการของตกค้าง (Unclaimed items) ที่ยังรอนโยบายผู้บริหาร ควรคงไว้เป็น Should / Needs Validation ใน backlog หรือควรย้ายออกจากรุ่นปัจจุบันจนกว่าจะมีนโยบายชัดเจน?