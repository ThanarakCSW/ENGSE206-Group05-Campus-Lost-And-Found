# Midterm Snapshot Manifest — Campus Lost and Found (Group 05)

> รายการสิ่งที่ tag `midterm-snapshot` ครอบคลุม ใช้ตรวจย้อนว่า requirement ก่อนสอบกลางภาคอยู่ในสถานะใด · ไฟล์จริงอยู่ที่ path เดิมใน repo (ไม่คัดลอกซ้ำ)

## เอกสาร Requirement

| ไฟล์ | เวอร์ชัน / tag | เนื้อหาที่ล็อก | สถานะ |
|---|---|---|---|
| `docs/05-requirement-backlog.md` | tag `baseline-v1.0` (W05b) | 5 Must FR · 1 Must BR · 1 Must NFR · Should/Could requirements | Baseline ของทีมสำหรับ W06–W08 |
| `docs/06-requirement-models.md` | Model Pack (W06) | 7 US · 6 UC · 8 AC · Trade-off notes | ส่งต่อ W07 แล้ว |
| `docs/07-srs-v1.md` | SRS Draft v1 (W07) | FR / NFR / BR / Data Requirements · Verification Plan · User Classes | Draft v1 (Baseline Candidate) |
| `docs/08-validation-traceability.md` | ส่วน A (W05b) + ส่วน B (W08) | Review findings (RV-01-SIM, RV-02, RV-03) · Bidirectional Traceability · CR-01-SIM | ทำครบถ้วนทั้งส่วน A และ B |
| `docs/requirements-change-log.md` | W08 | CR-01-SIM (AI Auto-matching scenario) | Open — Pending |

## Diagrams

| ไฟล์ (source + export) | ใช้ใน |
|---|---|
| `diagrams/use-case/usecase.drawio` / `.png` | `docs/06` หัวข้อ 4 · SRS Draft v1 |
| `diagrams/activity/w06-claim-verification-activity.drawio` / `.png` | `docs/06` และ `docs/07` (กระบวนการยื่นหลักฐาน ตรวจสอบ และส่งมอบ) |
| `diagrams/context/w02-system-context.drawio.xml` / `.png` | `docs/02` และ SRS Draft v1 |
| `diagrams/stakeholders/w02-stakeholder-map.drawio.xml` / `.png` | `docs/02` Stakeholder Profile |

## สิ่งที่ยังเปิดอยู่ ณ Midterm Snapshot

| ID | เรื่อง | สถานะและการส่งต่อ |
|---|---|---|
| OI-CLF-01 | นโยบายระยะเวลาจัดเก็บสิ่งของตกค้าง (Unclaimed Items Retention Policy) สรุปกี่วัน (30/60/90 วัน) และผู้มีอำนาจอนุมัติ | TBD — รอคำตอบและนโยบายจากผู้บริหาร |
| OI-CLF-02 | สถาปัตยกรรมเซ็นเซอร์ภาพถ่าย (AI Auto-censor vs Manual Staff Blurring) | TBD — รอการประเมินความคุ้มทุนของ IT Admin (ปัจจุบันใช้ Manual Blurring ตาม Baseline) |
| CR-01-SIM | ข้อเสนอระบบ AI Auto-matching ทันทีที่บันทึกข้อมูล (สถานการณ์จำลอง) | Pending — ไม่รับเข้า Baseline ปัจจุบัน เพื่อป้องกันความผิดพลาดและ Scope บวม |

## ใบส่งงานที่อยู่ใน Midterm Snapshot

- `submissions/baseline-review-submission.md` (W05b)
- `submissions/week-06-submission.md` (W06)
- `submissions/week-07-submission.md` (W07)
- `submissions/week-08-submission.md` (W08)
