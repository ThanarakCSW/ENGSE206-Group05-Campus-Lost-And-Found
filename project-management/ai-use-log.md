# AI Use Log

> บันทึกเฉพาะการใช้ AI ที่มีผลต่อข้อความ การวิเคราะห์ รูปภาพ หรือโครงสร้างชิ้นงาน เพื่อความโปร่งใสและการตรวจสอบย้อนกลับ

| Date | Tool | Purpose | Input Summary (ไม่ใส่ข้อมูลลับ) | Output Used | Human Verification / Revision | Related File |
|---|---|---|---|---|---|---|
| 2026-08-03 | Claude / ChatGPT | interview rehearsal | ซ้อมบทบาทการสัมภาษณ์จากชุดคำถามในคู่มือสัมภาษณ์ Case-05 (ไม่มีข้อมูลส่วนบุคคล) | ใช้ทดสอบ flow คำถามและหาจุดติดขัดก่อนสัมภาษณ์จริง | ทีมตรวจคำตอบและปรับคำถามที่ไม่ชัดเจนในคู่มือสัมภาษณ์ ไม่นำคำตอบมาใช้เป็นข้อเท็จจริงโดยตรง | `docs/03-interview-guide.md`, `evidence/week-03/question-rehearsal-notes.md` |
| 2026-08-04 | Claude / ChatGPT | stakeholder simulation | prompt จำลองบทบาทผู้มีส่วนได้ส่วนเสีย (ผู้ทำของหาย, ผู้พบของ, เจ้าหน้าที่, IT Admin, ผู้บริหาร) ตามขอบเขต Case-05 | คำตอบจำลองสกัดเป็นหลักฐานความต้องการและความกังวล (E-01 ถึง E-05) | ทีมตรวจสอบเทียบกับ Case Card และแยกแยะ Assumption/Open Questions ก่อนสรุปเข้าสู่ Evidence Log | `evidence/week-04/ai-conversation-excerpt.md`, `docs/04-evidence-log.md` |
| 2026-09-22 | Antigravity (Google DeepMind) | Design Strategy & Spine Formatting | สรุปโครงสร้าง Scope 4 ระดับ และจัดทำตาราง Design Spine 7 แถวสำหรับ Case-05 | ช่วยจัดโครงตาราง Markdown และจัดหมวดหมู่ Design Drivers D1–D3 | ทีมตรวจสอบกับ SRS Draft v1 และข้อกำหนดของรายวิชา ยืนยันไม่มีการตัด FR ใดออกจากระบบ | `design/10-design-strategy.md`, `design/00-design-spine.md` |
| 2026-10-05 | Antigravity (Google DeepMind) | Conceptual Architecture Drafting | สรุปความต้องการสถาปัตยกรรมระดับ Container, NFR-to-Container mapping และ Decision Cards | ช่วยจัดรูปแบบเอกสาร Word (.docx), สรุปตารางความสัมพันธ์ C4 และสร้างไดอะแกรม | ทีมตรวจสอบความสอดคล้องกับ SRS v1 และ Design Strategy อย่างละเอียด ไม่มีการสร้างตัวเลขหรือเทคโนโลยีเกินจริง | `design/11-conceptual-architecture-v0.1.docx`, `diagrams/architecture/`, `evidence/week-11/` |
