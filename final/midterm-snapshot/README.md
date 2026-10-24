# Midterm Snapshot (W08)

เก็บสำเนา (หรือ tag) ของ requirement baseline ก่อนสอบกลางภาค ตาม contract W08

- วิธีที่ทีมใช้: **git tag** `midterm-snapshot` บน commit ส่งงาน W08 แล้ว push tag — ไม่คัดลอกไฟล์ซ้ำในโฟลเดอร์นี้
- รายการไฟล์ เวอร์ชัน และสถานะที่ snapshot ครอบคลุม: [`snapshot-manifest.md`](snapshot-manifest.md)

| Field | Value |
|---|---|
| Tag / commit | tag `midterm-snapshot` → commit ส่งงาน `submit(w08): SRS validation and traceability` (hash ดูได้ด้วย `git rev-list -n 1 midterm-snapshot` และใน `submissions/submission-register.md`) |
| วันที่ | 21/09/2026 |
| ไฟล์ที่รวม | `docs/05-requirement-backlog.md` · `docs/06-requirement-models.md` · `docs/07-srs-v1.md` (v1) · `docs/08-validation-traceability.md` (ส่วน A + B) · `docs/requirements-change-log.md` · `diagrams/use-case/` · `diagrams/activity/` · `diagrams/context/` · `submissions/baseline-review-submission.md` · `submissions/week-06` ถึง `week-08` |
| สถานะ ณ snapshot | SRS = Baseline Candidate (ยังไม่ได้รับอนุมัติ) · CR-01-SIM = Pending · OI-CLF-01–08 = Open · RV-01-SIM = Resolved |

## วิธีสร้างและตรวจ tag

```bash
git tag midterm-snapshot            # บน commit submit(w08)
git push origin midterm-snapshot
git show --stat midterm-snapshot    # ตรวจว่า tag ชี้ commit ส่งงาน W08
```
