# 15 — Individual Reflection (Requirement Baseline Review v1.0)

> **Case Project:** Campus Lost and Found (Case-05)  
> **Course / Week:** ENGSE206 / Week 05 Consolidation Studio  
> **Date:** 18 สิงหาคม 2569

---

## Member 1: ธนรัก ชุ่มสวัสดิ์

### Student Information
| Field | Detail |
|---|---|
| Student ID | 66010001 |
| Name | ธนรัก ชุ่มสวัสดิ์ |
| Primary Role(s) | Facilitator, Requirements Lead, Traceability Auditor |

### 1. My Contribution
รับหน้าที่เป็น Facilitator คุมลำดับและเวลาในกระบวนการ Baseline Review พร้อมเป็น Traceability Auditor ทำการไล่สายย้อนกลับจาก Must Requirements (`FR-CLF-01` ถึง `FR-CLF-05`, `BR-CLF-01`, `NFR-CLF-01`) ไปยัง Evidence (`E-01`..`E-04`) และ Stakeholder Context ใน `docs/08-validation-traceability.md` จนครบ 100%

### 2. What I Learned About Requirements and Design
วันนี้เข้าใจชัดขึ้นว่า Baseline ไม่ใช่แค่การรวบรวมไฟล์ให้ครบ แต่คือการหยุดตรวจสอบว่าความต้องการทุกข้อมีที่มาจากหลักฐานจริง และไม่หลุด Scope จาก Case Card การล็อก Baseline v1.0 ช่วยให้ทีมมีฐานความต้องการที่สะอาดและมั่นใจก่อนนำไปสร้าง User Story และ Use Case ใน Week 06

### 3. A Decision I Influenced
ผลักดันให้แยกประเด็นนโยบายระยะเวลาจัดเก็บของตกค้าง (`ISSUE-CLF-01`) ออกเป็น Open Question แทนการทายตัวเลขวันเอาเอง ช่วยให้ Requirement Backlog สะท้อนเฉพาะความต้องการที่มีหลักฐานรองรับจริง

### 4. Feedback I Received and How I Responded
ได้รับ Feedback จากการตรวจ Quality Check ว่าข้อความ `FR-CLF-01` และ `FR-CLF-02` ยังกว้างเกินไป จึงได้ร่วมกับ Scribe ปรับถ้อยคำให้ระบุเกณฑ์ตัวเลขและเงื่อนไข (เช่น ระยะเวลาเรียกดูภายใน 3 วินาที และฟิลด์ข้อมูลบังคับ 3 ฟิลด์)

### 5. What I Would Improve Next Time
ในคาบถัดไปจะเตรียมโครงสร้างของ Acceptance Criteria (Gherkin syntax) ไว้ล่วงหน้า เพื่อให้แปลงจาก Business Rule (`BR-CLF-01`) ไปเป็น Testable Scenario ได้เร็วยิ่งขึ้น

### 6. Answers to Reflection Questions
1. **วันนี้ฉันเข้าใจอะไรชัดขึ้นเกี่ยวกับ requirement ของทีม?**  
   เข้าใจว่า Requirement ที่ดีต้องวัดผลได้จริง (Verifiable) และทุกลูกซอยลากย้อนกลับไปยังหลักฐานการสัมภาษณ์และ Pain Point ของผู้ใช้ได้โดยไม่มี Requirement ลอย
2. **จุดที่ทีมเรายังอ่อนที่สุดคืออะไร และจะทำอย่างไรต่อ?**  
   จุดที่ยังอ่อนคือประเด็นทางกฎหมายและนโยบายภายนอก (PDPA censorship และ retention policy) ที่ทีมไม่มี authority ตัดสินใจเอง แก้ไขโดยทำ Open Questions Log ส่งอาจารย์ก่อนเข้า Week 06
3. **คำถามที่อยากถามอาจารย์ในคาบหน้า (Week 6) คือ...**  
   อยากถามว่าในขั้นตอนการแปลง BR-CLF-01 (การเบลอร์ภาพ PDPA) ไปเป็น Acceptance Criteria ควรเขียนสโคปขั้นตอนการอนุมัติภาพของเจ้าหน้าที่แยกเป็นอีก Use Case หรือรวมอยู่ใน Flow การแจ้งพบของ?

---

## Member 2: นรบดี บุญเลิศ

### Student Information
| Field | Detail |
|---|---|
| Student ID | 66010002 |
| Name | นรบดี บุญเลิศ |
| Primary Role(s) | Quality Checker, Scribe, Timekeeper |

### 1. My Contribution
รับหน้าที่เป็น Quality Checker และ Scribe ดำเนินการตรวจประเมินคุณภาพของ FR/NFR ด้วยเกณฑ์ 4 มิติ (วัดได้, ไม่กำกวม, Atomic, มีที่มา) แก้ไขถ้อยคำที่ไม่ชัดเจนใน `docs/05-requirement-backlog.md` จัดทำ Decision Log (`project-management/decision-log.md`) และบันทึกผลการประเมิน Readiness Gate

### 2. What I Learned About Requirements and Design
เรียนรู้ว่าคำว่า "เร็ว" หรือ "สะดวก" เป็นคำกำกวมทางวิศวกรรมซอฟต์แวร์ที่ทำให้ผู้พัฒนาและผู้ทดสอบเข้าใจไม่ตรงกัน การปรับถ้อยคำให้ระบุเงื่อนไขเวลาและจำนวนคลิกชัดเจนช่วยลดความผิดพลาดในการออกแบบ UI และ State Diagrams ในสัปดาห์ถัดไป

### 3. A Decision I Influenced
นำเสนอทางเลือก Option C ใน Negotiation Record สำหรับการจัดการภาพถ่ายส่วนบุคคล โดยใช้ Role-Based Access Control ร่วมกับการปิดบังข้อมูลอ่อนไหว ซึ่งทำให้ `BR-CLF-01` และ `NFR-CLF-01` ผ่านการตรวจ PDPA Compliance

### 4. Feedback I Received and How I Responded
ได้รับ Feedback ในช่วง Peer Cross-Review ให้ตรวจสอบว่า MoSCoW มีเหตุผลสมบูรณ์หรือไม่ จึงได้เพิ่มคำอธิบาย Rationale ด้าน Risk (การสวมรอยรับของและข้อมูลรั่วไหล) ให้กับ Must Requirement ทุกข้อ

### 5. What I Would Improve Next Time
จะปรับปรุงกระบวนการบริหารเวลา (Timekeeping) ให้กระชับขึ้นในช่วงการอภิปราย Quality Check เพื่อให้มีเวลาในการร่าง User Stories ล่วงหน้าสำหรับ Week 06

### 6. Answers to Reflection Questions
1. **วันนี้ฉันเข้าใจอะไรชัดขึ้นเกี่ยวกับ requirement ของทีม?**  
   เข้าใจกระบวนการ Traceability Audit ที่ต้องสอบทานให้แน่ใจว่า Requirement มีความสอดคล้องกันตลอดทั้งสาย ตั้งแต่ Problem Brief, Evidence Log ไปจนถึง Backlog
2. **จุดที่ทีมเรายังอ่อนที่สุดคืออะไร และจะทำอย่างไรต่อ?**  
   การลงรายละเอียดเชิงเทคนิคเกี่ยวกับการเซ็นเซอร์ภาพถ่าย (AI Censor vs Manual Blur) ซึ่งทีมจะสอบทานศักยภาพทางเทคนิคกับอาจารย์เพิ่มเติม
3. **คำถามที่อยากถามอาจารย์ในคาบหน้า (Week 6) คือ...**  
   การทำ State Machine Diagram สำหรับสิ่งของ (Item Lifecycle) ควรแยกสถานะระหว่างคำร้องยืนยันตัวตน (Claim Request Status) กับสถานะกายภาพของสิ่งของในคลัง (Item Physical Status) หรือไม่?
