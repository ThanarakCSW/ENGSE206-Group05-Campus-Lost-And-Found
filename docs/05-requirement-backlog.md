# 05 — Requirement Backlog v1.0: Campus Lost and Found

> **Case:** Campus Lost and Found (Case-05)  
> **Source:** Week04 Evidence Log: `E-01..E-05`, `C-01..C-03`, `RC-01..RC-05`  
> **Status:** Baseline v1.0 (Reviewed & Locked for Week 6 Handoff)  
> **Goal:** จัดประเภท จัดลำดับ และล็อก requirement ที่ผ่านการตรวจสอบ Traceability และ Quality Audit เพื่อนำไปสร้าง Requirement Models ใน Week 06

## 1. Project Metadata

| Field | Value |
|---|---|
| Course / Week | ENGSE206 / Week05 (Consolidation Studio) |
| Team | Group05 |
| Case | Campus Lost and Found |
| Source Week04 file | `docs/04-evidence-log.md` |
| Traceability Audit file | `docs/08-validation-traceability.md` |
| Backlog version | `v1.0` |
| Date | 2026-08-18 |

## 2. Prioritization Method

ใช้ MoSCoW โดยประเมินจาก 4 มิติตามหลักวิศวกรรมซอฟต์แวร์:

| Dimension | วิธีใช้ในเคสนี้ |
|---|---|
| Value | ช่วยผู้ทำของหาย ผู้พบของ หรือเจ้าหน้าที่ทำงานหลักในการจับคู่และคืนของได้สำเร็จ |
| Risk | ถ้าขาด requirement นี้จะเกิดปัญหาข้อมูลกระจัดกระจาย ส่งของผิดคน หรือละเมิด PDPA |
| Urgency | จำเป็นต่อ core workflow รุ่นแรกก่อนขยายระบบ |
| Dependency | ต้องรอ policy, IT decision หรือ workflow การปฏิบัติงานกายภาพของเจ้าหน้าที่หรือไม่ |

## 3. Requirement Backlog Baseline v1.0

| Req ID | Source RC | Evidence / Need Trace | Requirement Statement | Type | Priority | Rationale | Status | Open Question / Gap | Week06 Use |
|---|---|---|---|---|---|---|---|---|---|
| FR-CLF-01 | RC-01 | E-01 -> N-01 | ระบบต้องให้เจ้าหน้าที่บันทึก ค้นหา และติดตามสถานะรับเข้า-จ่ายออกของรายการสิ่งของในคลังส่วนกลางได้ภายใน 3 วินาทีต่อการเรียกดู | Functional | Must | เป็น capability หลักในการแก้ปัญหาข้อมูลกระจัดกระจายและลดภาระเจ้าหน้าที่ | Baseline v1.0 | ฟิลด์ข้อมูลขั้นต่ำของรายการสิ่งของ | Use Case + User Story |
| FR-CLF-02 | RC-01 | E-01, E-02 -> N-01, N-02 | ระบบต้องให้ผู้ทำของหายกรอกแบบฟอร์มแจ้งของหายพร้อมระบุอย่างน้อย 3 ฟิลด์บังคับ (ชื่อสิ่งของ, หมวดหมู่, สถานที่สูญหาย) เพื่อใช้จับคู่เบื้องต้น | Functional | Must | เป็นจุดเริ่มต้นของ workflow การตามหาและจับคู่รายการสิ่งของ | Baseline v1.0 | ข้อมูลใดควรเปิดเผยต่อสาธารณะ | User Story + AC |
| FR-CLF-03 | RC-04 | E-04 -> N-04 | ระบบต้องให้ผู้พบของแจ้งเบาะแสและปักพิกัดสถานที่พบสิ่งของได้โดยไม่บังคับระบุชื่อหรือช่องทางติดต่อส่วนตัวต่อสาธารณะ | Functional | Must | ลดอุปสรรคของผู้พบของ เพิ่มโอกาสนำข้อมูลเข้าสู่ระบบส่วนกลาง | Baseline v1.0 | เจ้าหน้าที่ติดตามเบาะแสกลับอย่างไร | User Story + Use Case |
| FR-CLF-04 | RC-02 | E-02 -> N-02 | ระบบต้องให้ผู้ทำของหายแนบหลักฐานยืนยันความเป็นเจ้าของ (จำกัดขนาดไฟล์ไม่เกิน 10MB) ส่งตรงถึงเจ้าหน้าที่ผ่านช่องทางส่วนตัว | Functional | Must | ลดความเสี่ยงมิจฉาชีพสวมรอยและป้องกันการเปิดเผยหลักฐานสู่สาธารณะ | Baseline v1.0 | ประเภทเอกสารหลักฐานที่ยอมรับได้ | Use Case Rule + AC |
| FR-CLF-05 | RC-02 | E-01, E-02 -> N-02 | ระบบต้องให้เจ้าหน้าที่เปลี่ยนสถานะคำร้องยืนยันความเป็นเจ้าของ (pending, verified, rejected, returned) พร้อมบันทึกเหตุผลประกอบ | Functional | Must | เป็นจุดควบคุมการส่งมอบสิ่งของจริงเพื่อป้องกันความผิดพลาด | Baseline v1.0 | ขั้นตอนการตัดโอนสิ่งของคืน | Use Case + State Model |
| BR-CLF-01 | RC-03 | E-03 -> N-03 | รายการสิ่งของที่เผยแพร่สู่สาธารณะต้องปิดบังข้อมูลส่วนบุคคล (เลขบัตรประจำตัว, ข้อมูลติดต่อ, ภาพส่วนบุคคล) โดยผ่านการเบลอร์ภาพก่อนแสดงผล | Business Rule / Constraint | Must | ข้อกำหนดด้าน privacy/PDPA ที่ต้องบังคับใช้ในทุก workflow | Baseline v1.0 | นิยามข้อมูลอ่อนไหวในคำบรรยาย | Business Rule + AC |
| NFR-CLF-01 | RC-03 | E-03 -> N-03 | ระบบต้องจำกัดสิทธิ์เข้าถึงข้อมูลตามบทบาท (Public, Requester, Staff, IT Admin) โดยซ่อนหลักฐานยืนยันตัวตนจากผู้ใช้ที่ไม่ใช่เจ้าหน้าที่ | NFR / Security | Must | ป้องกันการรั่วไหลของข้อมูลส่วนบุคคลและหลักฐานสำคัญ | Baseline v1.0 | วิธีการยืนยันตัวตนตามบทบาท | Quality Scenario |
| FR-CLF-06 | RC-01 | E-01 -> N-01 | ระบบควรให้ผู้ใช้งานกรองรายการสิ่งของตาม 3 เงื่อนไข (หมวดหมู่สิ่งของ, สถานที่, ช่วงเวลา) และแสดงผลลัพธ์ไม่เกิน 5 คลิก | Functional | Should | เพิ่มความสะดวกและรวดเร็วในการค้นหาแต่ไม่ใช่ขั้นต่ำของ workflow | Baseline v1.0 | รายการตัวเลือกหมวดหมู่เริ่มต้น | User Story |
| FR-CLF-07 | RC-01 | E-01, Stakeholder Context -> N-01 | ระบบควรส่งการแจ้งเตือนอัตโนมัติไปยังผู้ยื่นคำร้องภายใน 1 นาที เมื่อสถานะคำร้องมีการเปลี่ยนแปลง | Functional | Should | ลดภาระเจ้าหน้าที่ในการตอบคำถามติดตามสถานะซ้ำซ้อน | Baseline v1.0 | ช่องทางแจ้งเตือนหลัก (Email/App) | Event List + AC |
| FR-CLF-08 | RC-05 | E-05, C-01 -> N-05 | ระบบควรสรุปรายงานสิ่งของตกค้างเกิน 30 วันเสนอเจ้าหน้าที่ประจำสัปดาห์เพื่อรอการตัดโอนตามนโยบาย | Functional + Policy Dependency | Should | มีคุณค่าต่อการบริหารคลัง แต่รอนโยบายอนุมัติระยะเวลากำหนดจริง | Baseline v1.0 | Retention policy จากผู้บริหาร | Follow-up + State Rule |
| NFR-CLF-02 | RC-03 | E-03 -> N-03 | ระบบต้องรองรับการแสดงผลแบบ Responsive บนอุปกรณ์มือถือ โดยโหลดหน้าจอหลักและแบบฟอร์มได้ภายใน 3 วินาทีบน 4G | NFR / Usability | Should | รองรับการแจ้งเหตุหน้างานทันทีผ่านโทรศัพท์มือถือ | Baseline v1.0 | หน้าจอสำคัญที่ต้องเน้น Mobile | Quality Scenario |
| FR-CLF-09 | RC-04 | E-04, C-03 -> N-04 | ระบบอาจรองรับ workflow ให้เจ้าหน้าที่ประจำพื้นที่รับแจ้งเบาะแสและไปรับสิ่งของเข้าคลังแทนผู้พบของ | Functional | Could | ช่วยลดภาระผู้พบของ แต่ต้องตกลงอัตรากำลังเจ้าหน้าที่กายภาพ | Baseline v1.0 | ผู้รับผิดชอบไปเก็บของจริง | Follow-up only |
| ISSUE-CLF-01 | E-05 / C-01 | E-05, C-01 -> N-05 | ยังไม่มีนโยบายอนุมัติระยะเวลาจัดเก็บและวิธีทำลาย/บริจาคสิ่งของตกค้างเกินกำหนดจากผู้บริหาร | Issue / Policy Gap | Won't yet | ห้ามสร้าง policy เอง ต้องเก็บเป็น Open Question ถามผู้บริหาร | Hold / Open Question | นโยบาย retention period สรุปกี่วัน | Follow-up only |
| ISSUE-CLF-02 | E-03 / C-02 | E-03, C-02 -> N-03 | ยังไม่ได้รับการยืนยันทางเลือกพัฒนาระบบ AI Auto-censor ภาพถ่าย เทียบกับการตรวจอนุมัติภาพโดยเจ้าหน้าที่ | Issue / Technical Gap | Won't yet | เป็นการตัดสินใจเชิงเทคโนโลยีและงบประมาณของ IT Admin | Hold / Open Question | IT เลือกสถาปัตยกรรมแบบใด | Follow-up only |

## 4. Priority Summary

| Priority | Count | Requirement IDs | เหตุผลรวม |
|---|---:|---|---|
| Must | 7 | FR-CLF-01, FR-CLF-02, FR-CLF-03, FR-CLF-04, FR-CLF-05, BR-CLF-01, NFR-CLF-01 | เป็นแกนกลาง workflow หลัก ป้องกันสวมรอยรับของ และคุ้มครอง PDPA |
| Should | 4 | FR-CLF-06, FR-CLF-07, FR-CLF-08, NFR-CLF-02 | เพิ่มประสิทธิภาพ UX และรายงาน แต่บางข้อยังรอนโยบายชัดเจน |
| Could | 1 | FR-CLF-09 | เป็นฟีเจอร์เสริมสำหรับพื้นที่ขนาดใหญ่ |
| Won't yet | 2 | ISSUE-CLF-01, ISSUE-CLF-02 | เป็นช่องว่างเชิงนโยบายและเทคนิคที่ห้ามยกระดับเป็น requirement เอง |

## 5. Ready / Follow-up / Hold Status

| Status | Requirement IDs | Action for Week06 |
|---|---|---|
| Ready for Week06 | FR-CLF-01, FR-CLF-02, FR-CLF-03, FR-CLF-04, FR-CLF-05, BR-CLF-01, NFR-CLF-01, FR-CLF-06, NFR-CLF-02 | แปลงเป็น User Story, Use Case, Acceptance Criteria และ Quality Scenarios |
| Needs Follow-up | FR-CLF-07, FR-CLF-08 | ยืนยันช่องทาง Notification และร่าง Retention Policy กับผู้บริหาร |
| Hold / Open Question | FR-CLF-09, ISSUE-CLF-01, ISSUE-CLF-02 | บันทึกใน Gap & Open Questions Log เพื่อสอบถามอาจารย์/ผู้บริหาร |

## 6. Review Checklist (Readiness Verification)

- [x] ทุก requirement มี Source RC หรือ Evidence source (Traceability ครบ)
- [x] ทุก requirement อ้างอิง Evidence / Need Trace ย้อนกลับได้ถึง E-ID และ Stakeholders
- [x] Type แยกแยะชัดเจน (Functional / NFR / Business Rule / Constraint / Issue)
- [x] Priority มี rationale สมเหตุสมผลอิงจาก Value, Risk, Urgency, Dependency
- [x] ข้อความ Requirement มีเกณฑ์วัดได้ (Verifiable), ไม่กำกวม (Unambiguous) และเป็นเรื่องเดียว (Atomic)
- [x] Scope ไม่บวมเกินขอบเขตของ Case Card (Case-05)
- [x] ล็อกสถานะเป็น Baseline v1.0 พร้อมส่งต่อ Week 06

## 7. Week06 Handoff Plan

| Week06 Artefact Target | Baseline Input Requirement |
|---|---|
| User Story | FR-CLF-01, FR-CLF-02, FR-CLF-03, FR-CLF-06 |
| Use Case & Flowchart | FR-CLF-01 (Officer Central Management), FR-CLF-04 & FR-CLF-05 (Ownership Verification Flow) |
| Acceptance Criteria | BR-CLF-01 (PDPA Blur Criteria), FR-CLF-02, FR-CLF-04 (Evidence Submission Rule) |
| Quality Scenarios | NFR-CLF-01 (RBAC Security), NFR-CLF-02 (Mobile Responsiveness) |
| State Machine Diagram | FR-CLF-05 (Item & Claim Lifecycle Statuses) |
| Open Questions Log | ISSUE-CLF-01, ISSUE-CLF-02 |

