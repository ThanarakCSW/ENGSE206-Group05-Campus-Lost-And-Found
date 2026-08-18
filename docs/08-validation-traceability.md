# 08 — Validation, Traceability and Baseline Management

> **Case:** Campus Lost and Found (Case-05)  
> **Week:** Week 05 Consolidation Studio (Requirement Baseline Review & Readiness Gate)  
> **Status:** Baseline v1.0 Approved & Locked  
> **Target:** ส่งมอบฐานความต้องการสอดคล้อง 100% สำหรับการทำ Requirement Modeling ใน Week 06

---

## 1. Validation Plan

| Validation Activity | Artefact Evaluated | Participants & Roles | Quality Criteria | Verification Evidence Link |
|---|---|---|---|---|
| Artefact Health Check | `docs/01` to `docs/05` | Facilitator, Scribe | Completeness, Recency, Structural Alignment | `../evidence/week-05/baseline-review/health-check.md` |
| Traceability Audit | `docs/04` -> `docs/05` | Traceability Auditor | 100% Must Requirements traceable to E-ID & Stakeholder | Section 3 below & `peer-cross-review.md` |
| Quality & MoSCoW Audit | `docs/05-requirement-backlog.md` | Quality Checker | Verifiable, Unambiguous, Atomic, Rationalized Priority | Section 2 below & `health-check.md` |
| Peer Cross-Review | All Week 05 Artefacts | Cross-Review Team (Sub-team A & B) | 5-point Checklist Pass, ID-referenced feedback | `../evidence/week-05/baseline-review/peer-cross-review.md` |
| Baseline Gate Lock | Repo State & Tag | Whole Team | All Gate criteria met, Git tagged `baseline-v1.0` | `project-management/decision-log.md` |

---

## 2. Requirements Quality Checklist

| Quality Dimension | Criteria Description | Evaluation Result | Evidence / Rationale Note |
|---|---|---|---|
| 1. ID Uniqueness & Nomenclature | ทุก Requirement มี ID เฉพาะตามรูปแบบ `[TYPE]-CLF-[NO]` ไม่ซ้ำซ้อน | **Pass** | ใช้ Prefix ชัดเจน: FR-CLF, NFR-CLF, BR-CLF, ISSUE-CLF |
| 2. Verifiability (วัด/ทดสอบได้) | มีเกณฑ์ตัวเลขหรือเงื่อนไขที่ตรวจรับได้ ชัดเจน ไม่ใช้คำลอยๆ | **Pass** | กำหนดเงื่อนไขเวลา (3s/1m), ขนาดไฟล์ (10MB), จำนวนคลิก (≤5) |
| 3. Unambiguity (ไม่กำกวม) | อ่านแล้วตีความได้ทางเดียว หลีกเลี่ยงคำว่า "เร็ว/ง่าย/สะดวก" ลอยๆ | **Pass** | ปรับแก้ถ้อยคำจาก "แสดงผลเร็ว" เป็น "แสดงผลภายใน 3 วินาทีบน 4G" |
| 4. Atomicity (หนึ่งข้อหนึ่งเรื่อง) | ไม่มัดหลาย workflow ที่แยกกันไว้ในข้อเดียว | **Pass** | แยกการแจ้งของหาย (FR-02) ออกจากการยื่นหลักฐาน (FR-04) และการตรวจสถานะ (FR-05) |
| 5. Traceability (มีที่มา) | ทุกลูกซอยลากย้อนกลับไปถึง Evidence, Need และ Stakeholder ได้ | **Pass** | มีตาราง Traceability ครบถ้วนย้อนกลับถึง E-01..E-05 |
| 6. MoSCoW Rationality | Priority มีเหตุผลรองรับ ไม่ใช้ความรู้สึกของทีม | **Pass** | Must ทุกข้อมี Rationale ด้าน Value, Risk (PDPA/สวมรอย), Urgency |
| 7. Scope Alignment | ไม่บวมเกินสิ่งที่ Case Card (Case-05) อนุญาต | **Pass** | ปฏิเสธระบบ CCTV, Tracking พัสดุ และจัดส่งภายนอกตาม Out-of-scope |

---

## 3. Full Traceability Matrix (Backward & Forward Traceability)

| Req ID | Requirement Statement (Baseline v1.0) | Priority | Primary Stakeholder | Evidence Trace (E-ID) | Need Trace (N-ID / RC-ID) | Verification / Review Method |
|---|---|---|---|---|---|---|
| FR-CLF-01 | เจ้าหน้าที่บันทึก ค้นหา และติดตามสถานะรับเข้า-จ่ายออกสิ่งของในคลังส่วนกลางได้ภายใน 3 วินาที | Must | เจ้าหน้าที่ศูนย์รับของหาย | E-01 | N-01 / RC-01 | Test case: Query database & UI render benchmark (≤ 3s) |
| FR-CLF-02 | ผู้ทำของหายกรอกฟอร์มแจ้งของหายพร้อมระบุ 3 ฟิลด์บังคับ (ชื่อ, หมวดหมู่, สถานที่) | Must | ผู้ทำของหาย | E-01, E-02 | N-01, N-02 / RC-01 | Form validation test (prevent submit if required fields empty) |
| FR-CLF-03 | ผู้พบของแจ้งเบาะแสและปักพิกัดพบสิ่งของได้โดยไม่บังคับเปิดเผยชื่อ/ติดต่อต่อสาธารณะ | Must | ผู้พบของ | E-04 | N-04 / RC-04 | Public submission simulation without auth check |
| FR-CLF-04 | ผู้ทำของหายแนบหลักฐานยืนยันความเป็นเจ้าของ (ไฟล์ ≤ 10MB) ส่งตรงถึงเจ้าหน้าที่ส่วนตัว | Must | ผู้ทำของหาย | E-02 | N-02 / RC-02 | Security & Privacy inspection (file visibility limited to staff) |
| FR-CLF-05 | เจ้าหน้าที่เปลี่ยนสถานะคำร้อง (pending, verified, rejected, returned) พร้อมบันทึกเหตุผล | Must | เจ้าหน้าที่ศูนย์รับของหาย | E-01, E-02 | N-02 / RC-02 | State transition test & audit log check |
| BR-CLF-01 | รายการสิ่งของสาธารณะต้องปิดบังข้อมูลส่วนบุคคล (เลขบัตร/ติดต่อ) และเบลอร์ภาพก่อนเผยแพร่ | Must | ผู้ดูแล IT / ผู้บริหาร | E-03 | N-03 / RC-03 | Privacy review & Public view image blurring check |
| NFR-CLF-01 | จำกัดสิทธิ์เข้าถึงข้อมูลตามบทบาท (RBAC: Public, Requester, Staff, IT Admin) | Must | ผู้ดูแล IT Admin | E-03 | N-03 / RC-03 | Access control penetration test & API authorization check |
| FR-CLF-06 | กรองรายการสิ่งของตาม 3 เงื่อนไข (หมวดหมู่, สถานที่, ช่วงเวลา) ไม่เกิน 5 คลิก | Should | ผู้ทำของหาย, เจ้าหน้าที่ | E-01 | N-01 / RC-01 | Usability step count review (≤ 5 clicks) |
| FR-CLF-07 | ส่งการแจ้งเตือนอัตโนมัติไปยังผู้ยื่นคำร้องภายใน 1 นาทีเมื่อสถานะเปลี่ยน | Should | ผู้ทำของหาย | E-01 | N-01 / RC-01 | Notification delivery timer audit (≤ 60s) |
| FR-CLF-08 | สรุปรายงานสิ่งของตกค้างเกิน 30 วันเสนอเจ้าหน้าที่ประจำสัปดาห์ | Should | เจ้าหน้าที่, ผู้บริหาร | E-05 | N-05 / RC-05 | Automated report batch generation test |
| NFR-CLF-02 | แสดงผล Responsive บนมือถือ โหลดหน้าหลัก/ฟอร์มภายใน 3 วินาทีบน 4G | Should | ผู้พบของ, ผู้ทำของหาย | E-03 | N-03 / RC-03 | Lighthouse Performance audit & Mobile device test |
| FR-CLF-09 | แสดงพิกัดเบาะแสสิ่งของบนแผนที่จำลองอาคารมหาวิทยาลัย | Could | ผู้พบของ, เจ้าหน้าที่ | E-04 | N-04 / RC-04 | Feature toggle check |

---

## 4. 3 Must Requirements Audit Form (Traceability Check Form)

| Req ID | มาจาก Evidence (E-xx) | ผูกกับ Stakeholder | Need / Candidate (RC) | ลากครบ? | Audit Result & Notes |
|---|---|---|---|---|---|
| FR-CLF-01 | E-01 | เจ้าหน้าที่ศูนย์รับของหาย | RC-01 / N-01 | **[x] ครบ** | ลากย้อนกลับถึงปัญหาคลังกระจัดกระจายและภาระงานเจ้าหน้าที่ได้ชัดเจน |
| FR-CLF-04 | E-02 | ผู้ทำของหาย | RC-02 / N-02 | **[x] ครบ** | ลากย้อนกลับถึงความกังวลเรื่องการสวมรอยรับของและความเป็นส่วนตัว |
| NFR-CLF-01 | E-03 | ผู้ดูแล IT Admin | RC-03 / N-03 | **[x] ครบ** | ลากย้อนกลับถึงข้อกำหนดกฎหมาย PDPA และสิทธิ์การเข้าถึงข้อมูลองค์กร |

---

## 5. Gap Analysis & Open Questions Log

| Gap / Issue ID | Description of Gap / Open Question | Rationale & Related Evidence | Impact on Requirements | Proposed Action / Week 06 Plan |
|---|---|---|---|---|
| ISSUE-CLF-01 | นโยบายระยะเวลาจัดเก็บและทำลายสิ่งของตกค้างยังรอนโยบายอนุมัติจากผู้บริหาร | E-05, C-01 (ยังไม่มีนโยบายส่วนกลางเรื่อง Retention Period) | ไม่กระทบ Core Workflow แต่กระทบการสร้าง Rule ตัดโอนใน FR-CLF-08 | บันทึกใน `evidence/week-05/baseline-review/open-questions.md` เพื่อสอบถามอาจารย์/ผู้บริหารใน Week 06 |
| ISSUE-CLF-02 | สถาปัตยกรรม AI Auto-censor ภาพถ่ายเทียบกับการตรวจอนุมัติภาพโดยเจ้าหน้าที่ | E-03, C-02 (กังวลภาระงานเจ้าหน้าที่ vs ความซับซ้อนทางเทคนิค) | กระทบรายละเอียด Implementation ของ BR-CLF-01 | ใช้แนวทาง Owner/Staff manual blur approval เป็น Baseline ไปก่อน รอยืนยันสถาปัตยกรรม IT ใน Week 06 |

---

## 6. Change Request Log

| CR-ID | Date | Requested Change | Reason / Evidence | Impacted Artefacts | Decision | Owner |
|---|---|---|---|---|---|---|
| CR-01 | 2026-08-18 | ปรับปรุงข้อความ FR/NFR ทั้งหมดให้มีตัวเลขเกณฑ์วัดได้ (Verifiable Criteria) | ผลการตรวจ Quality Audit ช่วงที่ 3 (พบถ้อยคำกำกวม) | `docs/05-requirement-backlog.md` | Approved | Quality Checker (นรบดี) |
| CR-02 | 2026-08-18 | ล็อกสถานะ Backlog เป็น Baseline v1.0 | Readiness Gate Check ข้อที่ 5 | `docs/05`, `docs/08`, `decision-log.md` | Approved | Facilitator (ธนรัก) |

---

## 7. Baseline Decision

- **Baseline Name:** `baseline-v1.0`
- **Date:** 18 สิงหาคม 2569
- **Approved/Reviewed by:** ทีม Group05 (ธนรัก ชุ่มสวัสดิ์ - Facilitator, นรบดี บุญเลิศ - Quality Checker / Scribe)
- **Remaining Open Issues:** `ISSUE-CLF-01` (Unclaimed retention policy), `ISSUE-CLF-02` (AI auto-censor architecture)
- **Sign-off Summary:** ฐานความต้องการ Campus Lost and Found ผ่านเกณฑ์ Readiness Gate ครบ 5 ข้อ สมบูรณ์สำหรับการนำไปทำ Requirement Models (User Story, Use Case, AC, State Machine) ใน Week 06
