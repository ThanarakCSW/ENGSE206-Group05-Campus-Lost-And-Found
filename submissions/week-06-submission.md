# Week 06 Submission — Requirement Models and Acceptance Criteria

## 1. Assignment Source

| Field | Value |
|---|---|
| Assignment ID | `W06-v1.0` |
| Course assignment URL | https://github.com/se-rmutl/engse206-lab/blob/main/weeks/week-06-requirement-modeling-negotiation/assignment-contract.md |
| Course version/commit read | branch `main` — อ่านเมื่อ 2026-08-25 |
| Date checked | 2026-08-25 |
| Case ID / Case URL | Case 05 — Campus Lost and Found · https://github.com/se-rmutl/engse206-lab/blob/main/cases/05-campus-lost-and-found.md |

## 2. Artefacts Submitted

ผลลัพธ์หลัก: **User Stories + Use Cases + Acceptance Criteria**

Expected paths: `docs/06-requirement-models.md`, `diagrams/use-case/`, `diagrams/activity/`, `submissions/week-06-submission.md`

| Artefact | Repository path / URL | Owner | Status |
|---|---|---|---|
| Requirement models: 7 US · 6 UC · 8 AC · trade-off notes | [`docs/06-requirement-models.md`](../docs/06-requirement-models.md) | ธนรัก ชุ่มสวัสดิ์ | Done |
| Use case diagram (UC-01–UC-06) | [`diagrams/use-case/usecase.drawio`](../diagrams/use-case/usecase.drawio) · [`.png`](../diagrams/use-case/usecase.png) | นรบดี บุญเลิศ | Done |
| Activity diagram: ยื่นหลักฐาน ตรวจสอบ และส่งมอบสิ่งของ (UC-04, UC-05) | [`diagrams/activity/w06-claim-verification-activity.drawio`](../diagrams/activity/w06-claim-verification-activity.drawio) · [`.png`](../diagrams/activity/w06-claim-verification-activity.png) | นรบดี บุญเลิศ | Done |
| ใบส่งงาน | `submissions/week-06-submission.md` | ธนรัก ชุ่มสวัสดิ์ | Done |

## 3. Evidence and Quality Check

- [x] มี source file ที่แก้ไขได้ (`.drawio` และ `.md`)
- [x] diagram มี `.drawio` และ export `.png`/`.pdf` เมื่อเกี่ยวข้อง
- [x] evidence อ้างอิงกลับไปยัง artefact ได้ (เชื่อมโยงกับ Baseline v1.0 ใน `docs/05`)
- [x] อัปเดต worklog และ AI use log แล้ว
- [x] ไม่มีข้อมูลส่วนบุคคล/secret

## 4. Team Contribution

| Member | Role / Work completed | Evidence (commit/file) |
|---|---|---|
| ธนรัก ชุ่มสวัสดิ์ | Facilitator / Requirements Lead — เขียน User Stories (US-01..US-07), Acceptance Criteria (AC-01..AC-08), Use Case Specifications (UC-01..UC-06) และสรุป Trade-off Notes | `docs/06-requirement-models.md` |
| นรบดี บุญเลิศ | Designer / Quality Checker — พัฒนาแบบจำลอง Use Case Diagram (`diagrams/use-case/usecase.drawio`), Activity Diagram (`diagrams/activity/w06-claim-verification-activity.drawio`) และตรวจความสอดคล้องของ Actor / Scenario | `diagrams/use-case/`, `diagrams/activity/` |

## 5. Tabletop / Review Summary

- **สิ่งที่นำเสนอ:** Use Case Diagram 6 Use Cases สำหรับ 4 กลุ่มผู้ใช้ (Requester, Finder, Staff, IT Admin) และ Activity Diagram ของกระบวนการยื่นคำร้อง ตรวจสอบ และส่งคืนสิ่งของ
- **Feedback ที่ได้รับ (ตรวจภายในทีม):** ควรเน้น Alternate Flow กรณีขนาดไฟล์เกิน 10MB และกรณีเจ้าหน้าที่ปฏิเสธคำร้องพร้อมระบุเหตุผล
- **สิ่งที่แก้ก่อนส่ง:** เพิ่มเงื่อนไขการตรวจขนาดไฟล์และ Alternate Flow ใน UC-04, UC-05 และระบุ Guard Condition ใน Activity Diagram ชัดเจน

## 6. Final Submission Snapshot

| Field | Value |
|---|---|
| Commit message | `submit(w06): requirement models and acceptance criteria` |
| Commit hash | `0bc598d` |
| Submitted at | 2026-08-25 21:00 |
| Known limitations / open questions | โฟกัสเฉพาะ 7 Requirements ที่เป็น Must ตาม Baseline v1.0 ยังไม่รวม AI Auto-censor หรือนโยบาย Retention ระยะยาว |

## 7. Revision after Feedback

| Date | Feedback | Change made | New commit |
|---|---|---|---|
| — | — | — | — |
