# Decision Log: Campus Lost and Found 

> ใช้สำหรับการตัดสินใจที่มีผลต่อ scope, requirement, architecture, UX/UI หรือ detailed design

| ID | Date | Decision | Options Considered | Rationale | Impacted Artefacts | Owner |
|---|---|---|---|---|---|---|
| D-01 | 2026-08-18 | ปรับข้อความ FR/NFR ทั้งหมดให้มีตัวเลขเกณฑ์วัดได้ (Verifiable Criteria) | Option A: ใช้คำบรรยายทั่วไป <br>Option B: กำหนดเกณฑ์ตัวเลขและเงื่อนไขวัดได้เชิงปริมาณ | ผ่านเกณฑ์ Quality Check ตามมาตรฐานวิศวกรรมซอฟต์แวร์ ช่วยให้เขียน Acceptance Criteria ใน Week 06 ได้ตรงจุด | `docs/05-requirement-backlog.md`, `docs/08-validation-traceability.md` | Quality Checker (นรบดี) |
| D-02 | 2026-08-18 | เลือกใช้วิธีซ่อนข้อมูลส่วนบุคคลและเบลอร์ภาพถ่ายสาธารณะร่วมกับ Role-Based Access Control (RBAC) | Option A: แสดงภาพเต็มสาธารณะ <br>Option B: ปิดภาพทั้งหมด <br>Option C: ปิดบังข้อมูลส่วนบุคคลและเบลอร์ภาพสาธารณะ พร้อมเปิดสิทธิ์เฉพาะเจ้าหน้าที่/ผู้ยื่นเรื่อง | สมดุลระหว่างการปฏิบัติตามกฎหมาย PDPA กับความสะดวกในการค้นหาสิ่งของของผู้ทำของหาย | `docs/05-requirement-backlog.md`, `docs/08-validation-traceability.md` | Requirements Lead (ธนรัก) |
| D-03 | 2026-08-18 | ไม่ยกระดับประเด็นนโยบายของตกค้างและ AI Censor เป็น Requirement จนกว่าจะได้รับอนุมัติ | Option A: ทีมกำหนดตัวเลข retention และ AI spec เอง <br>Option B: บันทึกเป็น Issue / Open Question รออนุมัติ | ป้องกันการสร้าง requirement จากความรู้สึกของทีมโดยไม่มีอำนาจอนุมัติจริง | `docs/05-requirement-backlog.md`, `evidence/week-05/baseline-review/open-questions.md` | Scribe (นรบดี) |
| D-04 | 2026-08-18 | อนุมัติการล็อกฐานความต้องการเป็น Baseline v1.0 | Option A: ปรับแก้ไปเรื่อยๆ <br>Option B: ล็อก Baseline v1.0 เพื่อเริ่มทำ Requirement Models ใน Week 06 | ผ่านเกณฑ์ Readiness Gate ครบทั้ง 5 ข้อ ทำให้ทีมมีจุดอ้างอิงนิ่งในการออกแบบซอฟต์แวร์ | `docs/05`, `docs/08`, `git tag baseline-v1.0` | Facilitator (ธนรัก) |
