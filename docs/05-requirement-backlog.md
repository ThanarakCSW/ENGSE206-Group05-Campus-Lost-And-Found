# 05 — Requirement Backlog v0.1: Campus Lost and Found

> **Case:** Campus Lost and Found
> **Source:** Week04 Evidence Log: `E-01..E-05`, `C-01..C-03`, `RC-01..RC-05`
> **Status:** Requirement Backlog
> **Goal:** จัดประเภท จัดลำดับ และแยก requirement ที่พร้อมใช้ต่อ Week06 ออกจาก issue ที่ยังต้องถามต่อ

## 1. Project Metadata

| Field | Value |
|---|---|
| Course / Week | ENGSE206 / Week05 |
| Team | Group05 |
| Case | Campus Lost and Found |
| Source Week04 file | `docs/04-evidence-log.md` |
| Backlog version | `v0.1` |
| Date | 2026-08-11 |

## 2. Prioritization Method

ใช้ MoSCoW โดยดูจาก 4 มิติ ไม่ใช้ความรู้สึกของทีมเป็นหลัก

| Dimension | วิธีใช้ในเคสนี้ |
|---|---|
| Value | ช่วยผู้ทำของหาย ผู้พบของ หรือเจ้าหน้าที่ทำงานหลักได้หรือไม่ |
| Risk | ถ้าขาด requirement นี้จะเกิดข้อมูลกระจัดกระจาย ส่งของผิดคน หรือ privacy leak หรือไม่ |
| Urgency | จำเป็นต่อ workflow รุ่นแรกหรือเป็นเรื่องปรับปรุงภายหลัง |
| Dependency | ต้องรอ policy, IT decision, workflow เจ้าหน้าที่ หรือข้อมูลเพิ่มก่อนหรือไม่ |

## 3. Requirement Backlog v0.1

| Req ID | Source RC | Evidence / Need Trace | Requirement Statement | Type | Priority | Rationale | Status | Open Question | Week06 Use |
|---|---|---|---|---|---|---|---|---|---|
| FR-CLF-01 | RC-01 | E-01 -> N-01 | ระบบต้องให้เจ้าหน้าที่บันทึก แก้ไข ค้นหา และติดตามสถานะของรายการของหาย/พบของในฐานข้อมูลส่วนกลางได้ | Functional | Must | เป็น capability หลักที่แก้ปัญหาข้อมูลกระจัดกระจายและลดภาระเจ้าหน้าที่ | Draft | ฟิลด์ข้อมูลขั้นต่ำของรายการสิ่งของมีอะไรบ้าง | Use Case + User Story |
| FR-CLF-02 | RC-01 | E-01, E-02 -> N-01, N-02 | ระบบต้องให้ผู้ทำของหายแจ้งข้อมูลสิ่งของที่สูญหายพร้อมรายละเอียดที่ใช้ค้นหาและจับคู่เบื้องต้นได้ | Functional | Must | เป็นจุดเริ่มต้นของ workflow การตามหาและจับคู่ข้อมูล | Draft | ต้องบังคับรายละเอียดใดบ้างก่อนส่งรายการ | User Story + AC |
| FR-CLF-03 | RC-04 | E-04 -> N-04 | ระบบต้องให้ผู้พบของแจ้งเบาะแส สถานที่พบ และรายละเอียดสิ่งของได้โดยไม่เปิดเผยช่องทางติดต่อส่วนตัวต่อสาธารณะ | Functional | Must | ลดอุปสรรคของผู้พบของและเพิ่มโอกาสให้ข้อมูลเข้าสู่ระบบกลาง | Draft | อนุญาต anonymous ระดับใด และเจ้าหน้าที่ติดต่อกลับอย่างไร | User Story + Use Case |
| FR-CLF-04 | RC-02 | E-02 -> N-02 | ระบบต้องให้ผู้ทำของหายส่งหลักฐานยืนยันความเป็นเจ้าของให้เจ้าหน้าที่ตรวจสอบแบบส่วนตัวได้ | Functional | Must | ลดความเสี่ยงมิจฉาชีพสวมรอยและป้องกันการเปิดเผยหลักฐานสู่สาธารณะ | Draft | หลักฐานประเภทใดที่ยอมรับได้ | Use Case Rule + AC |
| FR-CLF-05 | RC-02 | E-01, E-02 -> N-02 | ระบบต้องให้เจ้าหน้าที่ตรวจสอบคำร้องรับของคืนและอัปเดตผลการตรวจสอบได้ | Functional | Must | เป็นจุดควบคุมการส่งมอบของจริงและลดความผิดพลาดในการคืนของ | Draft | สถานะตรวจสอบควรมีกี่สถานะ | Use Case + State Model |
| BR-CLF-01 | RC-03 | E-03 -> N-03 | รายการที่เผยแพร่ต่อสาธารณะต้องไม่แสดงข้อมูลส่วนบุคคล เช่น เลขบัตร ข้อมูลติดต่อ หรือหลักฐานยืนยันตัวตน | Business Rule / Constraint | Must | เป็นข้อจำกัดด้าน privacy/PDPA ที่ครอบทุก workflow | Draft | นิยามข้อมูลอ่อนไหวในภาพ/คำบรรยายมีอะไรบ้าง | Business Rule + AC |
| NFR-CLF-01 | RC-03 | E-03 -> N-03 | ระบบต้องควบคุมการเข้าถึงข้อมูลด้วย role-based access | NFR / Security | Must | ถ้าไม่มีสิทธิ์ตามบทบาท ข้อมูลส่วนตัวและหลักฐานอาจรั่วไหล | Draft | บทบาทและสิทธิ์แต่ละกลุ่มต้องยืนยันอย่างไร | Quality Scenario |
| FR-CLF-06 | RC-01 | E-01 -> N-01 | ระบบควรให้เจ้าหน้าที่จัดหมวดหมู่สิ่งของและกรองรายการตามประเภท สถานที่ และช่วงเวลาได้ | Functional | Should | ช่วยให้ค้นหาเร็วขึ้น แต่ไม่ใช่ minimum workflow เพียงข้อเดียว | Draft | หมวดหมู่เริ่มต้นควรมีอะไรบ้าง | User Story |
| FR-CLF-07 | RC-01 | E-01, Stakeholder Context -> N-01 | ระบบควรแจ้งเตือนผู้เกี่ยวข้องเมื่อสถานะคำร้องหรือรายการสิ่งของเปลี่ยนแปลง | Functional | Should | ลดความไม่แน่นอนและลดภาระเจ้าหน้าที่ตอบคำถามซ้ำ | Draft | แจ้งผ่านช่องทางใด และแจ้ง event ใดบ้าง | Event List + AC |
| FR-CLF-08 | RC-05 | E-05, C-01 -> N-05 | ระบบควรสร้างรายงานหรือรายการแจ้งเตือนสิ่งของตกค้างตามระยะเวลานโยบายที่กำหนด | Functional + Policy Dependency | Should | มีคุณค่าต่อเจ้าหน้าที่และผู้บริหาร แต่ยังรอนโยบายของตกค้าง | Draft | ระยะเวลาของตกค้างคือกี่วัน และใครอนุมัติ policy | Follow-up + State Rule |
| FR-CLF-09 | RC-04 | E-04, C-03 -> N-04 | ระบบอาจรองรับ workflow ให้เจ้าหน้าที่ประจำพื้นที่รับแจ้งเบาะแสและไปรับสิ่งของเข้าคลังแทนผู้พบของ | Functional | Could | ช่วยลดภาระผู้พบของ แต่ต้องยืนยัน workflow และผู้รับผิดชอบจริง | Draft | ใครมีหน้าที่ไปรับของตามเบาะแส และจัดการของหายระหว่างทางอย่างไร | Follow-up only |
| NFR-CLF-02 | RC-03 | E-03 -> N-03 | ระบบควรใช้งานบนโทรศัพท์ได้สำหรับการแจ้งเหตุหน้างาน | NFR / Usability | Should | การแจ้งของหาย/พบของมักเกิดนอกโต๊ะทำงาน จึงควรรองรับมือถือ | Draft | หน้าจอใดเป็น mobile-critical | Quality Scenario |
| ISSUE-CLF-01 | E-05 / C-01 | E-05, C-01 -> N-05 | ยังไม่มี policy ยืนยันระยะเวลาจัดเก็บของตกค้างและวิธีจัดการหลังครบกำหนด | Issue | Won't yet | ห้ามสร้าง policy เองจากความรู้สึก เพราะมีผลต่อสิทธิ์และกฎหมาย | Draft | ผู้บริหารกำหนด policy และ retention period อย่างไร | Follow-up only |
| ISSUE-CLF-02 | E-03 / C-02 | E-03, C-02 -> N-03 | ยังไม่ยืนยันว่าจะใช้ automatic censor หรือให้เจ้าหน้าที่ตรวจสอบภาพก่อนเผยแพร่ | Issue / Technical Dependency | Won't yet | เป็น decision เชิง IT/process ที่ยังไม่มีหลักฐานเพียงพอ | Draft | IT Admin เลือกแนวทางใดและมีทรัพยากรพอหรือไม่ | Follow-up only |

## 4. Priority Summary

| Priority | Count | Requirement IDs | เหตุผลรวม |
|---|---:|---|---|
| Must | 7 | FR-CLF-01, FR-CLF-02, FR-CLF-03, FR-CLF-04, FR-CLF-05, BR-CLF-01, NFR-CLF-01 | เป็นแกน workflow และลด risk เรื่องส่งของผิดคน/ข้อมูลรั่ว |
| Should | 4 | FR-CLF-06, FR-CLF-07, FR-CLF-08, NFR-CLF-02 | มีคุณค่าสูง แต่บางข้อยังต้องยืนยัน channel/policy |
| Could | 1 | FR-CLF-09 | มีประโยชน์ แต่พึ่ง workflow เจ้าหน้าที่ประจำพื้นที่ |
| Won't yet | 2 | ISSUE-CLF-01, ISSUE-CLF-02 | ยังไม่มีหลักฐานหรือนโยบายเพียงพอ ห้ามยกระดับเป็น requirement |

## 5. Ready / Follow-up / Hold

| Status | Requirement IDs | สิ่งที่ต้องทำต่อ |
|---|---|---|
| Ready for Week06 | FR-CLF-01, FR-CLF-02, FR-CLF-03, FR-CLF-04, FR-CLF-05, BR-CLF-01, FR-CLF-06, NFR-CLF-02 | ทำ User Story / Use Case / Acceptance Criteria |
| Needs Follow-up | NFR-CLF-01, FR-CLF-07, FR-CLF-08 | ถาม stakeholder, IT หรือ policy owner เพิ่ม |
| Hold | FR-CLF-09, ISSUE-CLF-01, ISSUE-CLF-02 | เก็บเป็น issue/follow-up ยังไม่เขียนเป็น final rule หรือ design |

## 6. Review Checklist

- [x] ทุก requirement มี Source RC หรือ Evidence source
- [x] ทุก requirement อ้าง Evidence / Need Trace
- [x] Type แยกเป็น Functional / NFR / Business Rule / Constraint / Issue
- [x] Priority มี rationale จาก value/risk/urgency/dependency
- [x] Unknown หรือ policy issue ไม่ถูกยกระดับเป็น requirement โดยไม่มีหลักฐาน
- [x] มี Week06 Use สำหรับรายการที่พร้อมทำ model
- [x] Status ในตาราง Requirement Backlog เป็น Draft ทั้งหมด

## 7. Week06 Handoff

Week06 ควรเริ่มจาก requirement ที่พร้อมก่อน:

| Week06 artefact | Input ที่เหมาะสม |
|---|---|
| User Story | FR-CLF-01, FR-CLF-02, FR-CLF-03 |
| Use Case | FR-CLF-01 เป็น officer management flow; FR-CLF-04/FR-CLF-05 เป็น ownership verification flow |
| Acceptance Criteria | BR-CLF-01, FR-CLF-02, FR-CLF-04 |
| Quality Scenario | NFR-CLF-01, NFR-CLF-02 |
| State Model | FR-CLF-05, FR-CLF-08 หลังยืนยัน policy |
| Follow-up only | ISSUE-CLF-01, ISSUE-CLF-02 |