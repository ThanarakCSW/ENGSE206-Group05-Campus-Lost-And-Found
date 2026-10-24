# 08 — Validation, Traceability and Baseline Management

> เอกสารนี้มี 2 ส่วนหลัก: **ส่วน A** บันทึกการตรวจ Baseline Review (W05b) · **ส่วน B** บันทึกการตรวจ Post-SRS Validation, Traceability และ Change Management (W08)

---

## ส่วน A — Baseline Traceability (W05b)

## 1. Validation Plan

| Validation Activity | Artefact Evaluated | Participants & Roles | Quality Criteria | Verification Evidence Link |
|---|---|---|---|---|
| Artefact Health Check | `docs/01` to `docs/05` | Facilitator, Scribe | Completeness, Recency, Structural Alignment | `../evidence/week-05/baseline-review/health-check.md` |
| Traceability Audit | `docs/04` -> `docs/05` | Traceability Auditor | 100% Must Requirements traceable to E-ID & Stakeholder | Section 3 below & `peer-cross-review.md` |
| Quality & MoSCoW Audit | `docs/05-requirement-backlog.md` | Quality Checker | Verifiable, Unambiguous, Atomic, Rationalized Priority | Section 2 below & `health-check.md` |
| Peer Cross-Review | All Week 05 Artefacts | Cross-Review Team (Group 01) | 5-point Checklist Pass, ID-referenced feedback | `../evidence/week-05/baseline-review/peer-cross-review.md` |
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

## 3. Traceability Matrix

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

## 4. 3 Traceability Check Form

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

---

## ส่วน B — Post-SRS Review, Traceability and Change Management (W08)

> เติมใน Week 8 หลังจัดทำ `docs/07-srs-v1.md` (SRS Draft v1) เสร็จสิ้น  
> ตรวจสอบความสอดคล้อง (Consistency), ความสมบูรณ์ (Completeness), การสืบย้อนกลับได้แบบสองทิศทาง (Bidirectional Traceability) และวิเคราะห์ผลกระทบกรณีมีคำขอเปลี่ยนแปลง (Change Scenario)

### B1. Validation Plan

| Validation Activity | Artefacts Evaluated | Participants & Roles | Quality Criteria | Verification Evidence Link |
|---|---|---|---|---|
| V-1 Walkthrough & Checklist Review | `docs/07-srs-v1.md` (SRS Draft v1) | Reviewer: นรบดี บุญเลิศ<br>Author/Defend: ธนรัก ชุ่มสวัสดิ์ | Completeness, Unambiguity, Consistency เทียบกับ Baseline v1.0 และ Models W06 | B2 (Review Findings) |
| V-2 Seeded Error / Training Check | ข้อความจำลองกระบวนการส่งหลักฐาน | ทั้งทีม (ธนรัก, นรบดี) | ความสอดคล้องกับ BR-CLF-01, FR-CLF-05 และ UC-05 | B2 (RV-01-SIM) |
| V-3 Bidirectional Traceability Lab | `docs/04` -> `docs/05` -> `docs/06` -> `docs/07` | ธนรัก ชุ่มสวัสดิ์, นรบดี บุญเลิศ | ลากสายเดินหน้า (Forward) และย้อนกลับ (Backward) ได้ครบ 100% | B3 (Traceability Matrix) |
| V-4 Change Scenario & Impact Analysis | คำขอเปลี่ยนจำลอง (CR-01-SIM) | ทั้งทีม | วิเคราะห์ผลกระทบต่อ FR, BR, UC, AC, Test Case และนโยบาย | B4 และ `docs/requirements-change-log.md` |

---

### B2. Review Findings (ผลการตรวจทาน SRS Draft v1)

| Finding ID | ตำแหน่งใน SRS | ข้อค้นพบ / สภาพปัญหา | ระดับความรุนแรง | ประเภทการจัดการ | แนวทางแก้ไข / การจัดการ |
|---|---|---|---|---|---|
| RV-01-SIM | หัวข้อ 2.3 & 3 (FR-CLF-04/05) | **ข้อความฝึกจำลอง (Seeded Error):** "เมื่อผู้ทำของหายยื่นคำร้อง ระบบจะเปลี่ยนสถานะเป็น Verified และนัดรับของทันที" ขัดกับกติกาความปลอดภัยที่ต้องให้เจ้าหน้าที่ตรวจสอบหลักฐานก่อน | High | แก้ไขข้อความทันที | ปรับแก้เป็น: "เมื่อยื่นคำร้อง สถานะเริ่มต้นเป็น Pending เพื่อให้เจ้าหน้าที่เปิดตรวจหลักฐานแบบส่วนตัวก่อนเปลี่ยนเป็น Verified หรือ Rejected" (ใน SRS จริงเขียนถูกต้องแล้ว) |
| RV-02 | หัวข้อ 1.3 & 8 (ISSUE-CLF-01) | ระยะเวลาจัดเก็บของตกค้าง (Unclaimed Items) ยังคงเป็น TBD รอการยืนยันนโยบายจากผู้บริหาร | Medium | Open Issue (OI-CLF-01) | คงสถานะ TBD ไว้ใน SRS โดยไม่แต่งตัวเลขขึ้นเอง และบันทึกไว้ใน Open Question Log |
| RV-03 | หัวข้อ 1.3 & 8 (ISSUE-CLF-02) | วิธีการเซ็นเซอร์ภาพส่วนบุคคล (AI Auto-censor vs Manual Staff Blurring) อยู่ระหว่างรอการประเมินความคุ้มทุน | Medium | Open Issue (OI-CLF-02) | กำหนดให้ใช้การเบลอร์แบบ Manual โดยผู้ส่ง/เจ้าหน้าที่ เป็นค่าเริ่มต้น (Baseline) ก่อนขยายสู่ AI ในอนาคต |
| CR-01-SIM | หัวข้อ 3 (FR-CLF-02) | คำขอเสนอระบบจับคู่อัตโนมัติ (AI Auto-matching) ทันทีที่แจ้งของหาย | — | Change Request (Simulated) | บันทึกใน Change Log และวิเคราะห์ผลกระทบ โดยคงสถานะเป็น **Pending** (ไม่แก้ Baseline ปัจจุบัน) |

**Before / After ของข้อความฝึก (RV-01-SIM):**
> **Before (ผิด):** เมื่อผู้ทำของหายกดส่งคำร้องยืนยันความเป็นเจ้าของ ระบบจะเปลี่ยนสถานะเป็น Verified ให้ทันทีเพื่อความสะดวก  
> **After (ถูกต้อง):** เมื่อผู้ทำของหายส่งคำร้องและแนบหลักฐาน (≤ 10MB) ระบบจะบันทึกสถานะเป็น Pending จากนั้นส่งให้เจ้าหน้าที่ตรวจสอบเปรียบเทียบกับสิ่งของจริงก่อนเปลี่ยนสถานะเป็น Verified หรือ Rejected พร้อมระบุเหตุผล (ตาม FR-CLF-05 และ AC-06)

---

### B3. Traceability Matrix — เดินได้ทั้งไปและกลับ

#### B3.1 Forward Traceability: จากปัญหาและหลักฐาน สู่ SRS และวิธีตรวจรับ

| Evidence (E-ID) | Need (N-ID) | Candidate (RC) | Requirement (FR/NFR/BR) | Model (US / UC / AC) | หัวข้อใน SRS v1 | วิธีตรวจรับที่วางแผน (Verification Method) | สถานะความครอบคลุม |
|---|---|---|---|---|---|---|---|
| E-01 | N-01 | RC-01 | FR-CLF-01 | US-01 / UC-01 / AC-01, AC-02 | หัวข้อ 3.1 | Test Case: Benchmark เวลาเรียกดูและค้นหารายการในคลัง (≤ 3 วินาที) | ✔ ครบถ้วน |
| E-01, E-02 | N-01, N-02 | RC-01 | FR-CLF-02 | US-02 / UC-02 / AC-03 | หัวข้อ 3.1 | Form Validation Test: ตรวจสอบ 3 ฟิลด์บังคับ (ชื่อ, หมวดหมู่, สถานที่) | ✔ ครบถ้วน |
| E-04 | N-04 | RC-04 | FR-CLF-03 | US-03 / UC-03 / AC-04 | หัวข้อ 3.1 | Inspection: ทดสอบการแจ้งเบาะแสโดยไม่ระบุตัวตน (Anonymous Report) | ✔ ครบถ้วน |
| E-02 | N-02 | RC-02 | FR-CLF-04 | US-04 / UC-04 / AC-05 | หัวข้อ 3.1 | Security & Limit Test: ตรวจสอบขนาดไฟล์แนบ (≤ 10MB) และสิทธิ์การเข้าถึงส่วนตัว | ✔ ครบถ้วน |
| E-01, E-02 | N-02 | RC-02 | FR-CLF-05 | US-05 / UC-05 / AC-06 | หัวข้อ 3.1 | State Transition Test: ทดสอบเปลี่ยนสถานะ 4 ค่า (pending, verified, rejected, returned) พร้อมเหตุผล | ✔ ครบถ้วน |
| E-03 | N-03 | RC-03 | BR-CLF-01 | US-06 / UC-06 / AC-07 | หัวข้อ 6.1 | Privacy Inspection: ตรวจสอบการเบลอร์ภาพและการปิดบังเลขบัตร/ข้อมูลติดต่อในหน้าสาธารณะ | ✔ ครบถ้วน |
| E-03 | N-03 | RC-03 | NFR-CLF-01 | US-07 / UC-06 / AC-08 | หัวข้อ 4.1 | RBAC Authorization Test: ตรวจสิทธิ์ 4 บทบาท (Public, Requester, Staff, IT Admin) | ✔ ครบถ้วน |

#### B3.2 Backward Traceability: เดินย้อนกลับจาก Acceptance Criteria สู่ Evidence

| เริ่มต้นจาก AC | เชื่อมกับ Use Case / Flow | ชี้ไปยัง Requirement | ย้อนสู่ Need & Evidence | ผลการตรวจสอบการสืบย้อนกลับ |
|---|---|---|---|---|
| **AC-05** แนบไฟล์หลักฐาน ≤ 10MB ส่งตรงถึงเจ้าหน้าที่แบบส่วนตัว | UC-04 (Main Flow) | FR-CLF-04 | N-02 ← E-02 (ความกังวลเรื่องมิจฉาชีพสวมรอย) | ✔ เดินครบถ้วน: มีไฟล์และหลักฐานยืนยันชัดเจนใน `docs/04` |
| **AC-06** เจ้าหน้าที่เปลี่ยนสถานะ 4 ค่าพร้อมบันทึกเหตุผลประกอบ | UC-05 (Main & Alternate Flows) | FR-CLF-05 | N-02 ← E-01, E-02 (ป้องกันการส่งมอบของผิดคน) | ✔ เดินครบถ้วน: มีเกณฑ์การตรวจรับและสอดคล้องกับ State Lifecycle |
| **AC-07** ปิดบังข้อมูลส่วนบุคคลและเบลอร์ภาพก่อนแสดงผลสาธารณะ | UC-06 (Main Flow) | BR-CLF-01 | N-03 ← E-03 (ความเสี่ยงละเมิด PDPA จากภาพถ่าย) | ✔ เดินครบถ้วน: มีที่มาจากข้อกฎหมาย PDPA และความต้องการของ IT Admin |

#### B3.3 Coverage Summary

- **Must Requirements (7 ข้อ):** เชื่อมโยงครบทั้ง 100% สู่ User Stories, Use Cases, Acceptance Criteria และมีหัวข้อรองรับใน SRS Draft v1
- **Trace Gap:** ไม่มี Requirement ลอย (Unlinked Requirement) และไม่มี Use Case ที่ขาดที่มาจากความต้องการของผู้มีส่วนได้ส่วนเสีย
- **Open Issues:** ประเด็นระยะเวลาจัดเก็บ (OI-CLF-01) และสถาปัตยกรรมเซ็นเซอร์ภาพ (OI-CLF-02) ถูกระบุสถานะชัดเจนเป็น TBD เพื่อรอการพัฒนาต่อยอด

---

### B4. Change Request & Impact Analysis

| CR-ID | วันที่บันทึก | รายละเอียดคำขอเปลี่ยนแปลง (Requested Change) | เหตุผล / ที่มา | การวิเคราะห์ผลกระทบ (Impact Analysis) | สถานะการตัดสินใจ | ผู้มีอำนาจตัดสินใจ |
|---|---|---|---|---|---|---|
| **CR-01-SIM** | 2026-09-15 | เสนอให้เพิ่มระบบจับคู่อัตโนมัติ (AI Auto-matching) ระหว่างคำร้องของหายกับรายการของที่พบในคลังทันทีที่บันทึกข้อมูล | ผู้ใช้งาน (ในสถานการณ์จำลอง) ต้องการทราบผลการจับคู่ทันทีโดยไม่ต้องรอค้นหา | • **Requirement:** กระทบ FR-CLF-02 และต้องเพิ่ม FR-CLF-10 (Auto-matching)<br>• **Models:** กระทบ UC-02, UC-05 และต้องเพิ่ม AC ด้านความแม่นยำของ AI<br>• **Risk:** อาจเกิด False Positive ทำให้แจ้งเตือนผิดพลาด หรือเกิดความเสี่ยงส่งมอบผิดคนหากไม่มีเจ้าหน้าที่ยืนยัน<br>• **Architecture:** ต้องเพิ่มบริการ AI Matcher และจัดการภาระประมวลผล | **Pending** (ยังไม่รับเข้า Baseline) | Product Owner / ผู้บริหาร (ทีมไม่มีอำนาจอนุมัติเปลี่ยน Scope กลางคัน) |

---

### B5. Baseline Decision for Midterm Snapshot

- **สถานะการล็อก:** ผ่านการตรวจทานความสอดคล้องและพร้อมสำหรับการจัดทำ Midterm Snapshot
- **Tag ที่ใช้ล็อก:** `midterm-snapshot`
- **มติทีม:** ให้คงชุดความต้องการ Baseline v1.0 และโครงสร้าง SRS Draft v1 ไว้เป็นหลักฐานสำหรับการสอบกลางภาค โดยไม่รับคำขอเปลี่ยนแปลง CR-01-SIM เข้ามาในรอบนี้
- **ผู้รับรอง:** ธนรัก ชุ่มสวัสดิ์ (Facilitator), นรบดี บุญเลิศ (Quality Checker) วันที่ 21 กันยายน 2569

