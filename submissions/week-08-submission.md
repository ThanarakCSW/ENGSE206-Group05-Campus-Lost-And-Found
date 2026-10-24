# Week 08 Submission — SRS Validation, Traceability and Change

## 1. Assignment Source

| Field | Value |
|---|---|
| Assignment ID | `W08-v1.0` |
| Course assignment URL | https://github.com/se-rmutl/engse206-lab/blob/main/weeks/week-08-srs-validation-traceability/assignment-contract.md |
| Course version/commit read | branch `main` — อ่านเมื่อ 2026-09-15 |
| Date checked | 2026-09-21 |
| Case ID / Case URL | Case 05 — Campus Lost and Found · https://github.com/se-rmutl/engse206-lab/blob/main/cases/05-campus-lost-and-found.md |

## 2. Artefacts Submitted

ผลลัพธ์หลัก: **Reviewed SRS + Traceability + Baseline**

Expected paths: `docs/08-validation-traceability.md`, `docs/requirements-change-log.md`, `final/midterm-snapshot/`, `submissions/week-08-submission.md`

| Artefact | Repository path / URL | Owner | Status |
|---|---|---|---|
| ส่วน B: Validation Plan, Review Findings (RV-01-SIM), Traceability ไป-กลับ, CR-01-SIM, Baseline Decision | [`docs/08-validation-traceability.md`](../docs/08-validation-traceability.md) | ธนรัก ชุ่มสวัสดิ์ | Done |
| Requirements Change Log (CR-01-SIM) | [`docs/requirements-change-log.md`](../docs/requirements-change-log.md) | นรบดี บุญเลิศ | Open — Pending |
| Midterm Snapshot Manifest (tag `midterm-snapshot`) | [`final/midterm-snapshot/snapshot-manifest.md`](../final/midterm-snapshot/snapshot-manifest.md) | นรบดี บุญเลิศ | Done |
| ใบส่งงาน | `submissions/week-08-submission.md` · tag `midterm-snapshot` | ธนรัก ชุ่มสวัสดิ์ | Done |

## 3. Evidence and Quality Check

- [x] มี source file ที่แก้ไขได้
- [x] diagram มี `.drawio` และ export `.png`/`.pdf` เมื่อเกี่ยวข้อง
- [x] evidence อ้างอิงกลับไปยัง artefact ได้ (ลากสายย้อนกลับจาก AC สู่ E-ID ได้ครบ 100%)
- [x] อัปเดต worklog และ AI use log แล้ว
- [x] มีการตรวจทานภายในทีม (Walkthrough Review)
- [x] ไม่มีข้อมูลส่วนบุคคล/secret

## 4. Team Contribution

| Member | Role / Work completed | Evidence (commit/file) |
|---|---|---|
| ธนรัก ชุ่มสวัสดิ์ | Facilitator / Traceability Auditor — ตรวจสอบสายความสัมพันธ์ไป-กลับ (Forward/Backward Traceability), วิเคราะห์ความครอบคลุมของ Must Requirements (100%) และสรุปมติ Baseline Decision | `docs/08-validation-traceability.md` |
| นรบดี บุญเลิศ | Quality Checker / Scribe — ดำเนินการ Checklist Walkthrough ตรวจสอบข้อความกำกวม (RV-01-SIM), จัดทำตาราง Requirements Change Log (CR-01-SIM) และรวบรวม Midterm Snapshot Manifest | `docs/08-validation-traceability.md`, `docs/requirements-change-log.md`, `final/midterm-snapshot/` |

## 5. Tabletop / Review Summary

- **สิ่งที่นำเสนอ:** การทบทวนความต้องการใน SRS Draft v1, การตรวจสอบ Traceability Matrix ย้อนกลับไปยัง Pain Points และหลักฐานการสัมภาษณ์จำลอง (E-01..E-05), การวิเคราะห์ผลกระทบกรณีขอเพิ่มระบบ AI Auto-matching (CR-01-SIM) และการล็อก Midterm Snapshot
- **Feedback ที่ได้รับ (ตรวจภายในทีม):** ต้องแยกข้อความฝึกจำลอง (Seeded Error) ออกจากข้อความจริงของ SRS ให้ชัดเจน และต้องระบุผลกระทบด้านความเสี่ยงและความผิดพลาดของ AI ในการจับคู่
- **สิ่งที่แก้ก่อนส่ง:** ปรับแก้ข้อความ RV-01-SIM ให้สอดคล้องกับกติกาการเปลี่ยนสถานะของเจ้าหน้าที่ และบันทึกข้อเสนอ CR-01-SIM เป็นสถานะ **Pending** โดยคง Baseline เดิมไว้สำหรับสอบกลางภาค

## 6. Final Submission Snapshot

| Field | Value |
|---|---|
| Commit message | `submit(w08): SRS validation and traceability` |
| Commit hash | tag `midterm-snapshot` |
| Submitted at | 2026-09-21 21:00 |
| Known limitations / open questions | Open Issues เรื่องระยะเวลาจัดเก็บของตกค้าง (OI-CLF-01) และสถาปัตยกรรมเซ็นเซอร์ภาพ (OI-CLF-02) ยังคงเป็น TBD รอการตัดสินใจจากผู้มีอำนาจ |

## 7. Revision after Feedback

| Date | Feedback | Change made | New commit |
|---|---|---|---|
| — | — | — | — |
