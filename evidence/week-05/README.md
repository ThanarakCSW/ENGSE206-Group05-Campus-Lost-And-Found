# Evidence — Week 05: Prioritization

- วันที่: 2026-08-11
- กิจกรรม: Requirement prioritization workshop
- ผู้เข้าร่วม/บทบาท: Facilitator/Submit, Scribe manager/Reviewer, Stakeholder Mapper
- หลักฐานที่เก็บ: `docs/04-evidence-log.md`, `docs/02-stakeholder-context-scope.md`, `docs/05-requirement-backlog.md`
- สิ่งที่ค้นพบ: Requirement ที่เกี่ยวกับระบบส่วนกลาง การยืนยันความเป็นเจ้าของ Privacy/PDPA และ role-based access เป็น Must เพราะเชื่อมกับปัญหาหลักและความเสี่ยงสูง ส่วนรายงานของตกค้างและ workflow รับของตามเบาะแสยังต้องตรวจสอบนโยบาย/กระบวนการเพิ่มเติม
- ผลกระทบต่อ artefact: อัปเดต `docs/05-requirement-backlog.md` ให้มี FR, NFR, Business Rules, MoSCoW priority และ acceptance measure ที่ trace กลับไปยัง E-ID ได้

## Prioritization Notes

| Source | Key point used in Week 05 | Impact on backlog |
|---|---|---|
| E-01 | ไม่มีระบบกลาง ทำให้ค้นหาและติดตามสถานะลำบาก | กำหนด FR-01, FR-02 และ FR-10 |
| E-02 | เสี่ยงมิจฉาชีพสวมรอยและส่งมอบผิดคน | กำหนด FR-04, FR-05 และ BR-02 เป็น Must |
| E-03 | ภาพ/ข้อมูลส่วนบุคคลเสี่ยงละเมิด PDPA | กำหนด FR-06, FR-07, NFR-02 และ NFR-03 เป็น Must |
| E-04 | ผู้พบของไม่อยากเปิดเผยตัวตนและไม่อยากเก็บของไว้เอง | กำหนด FR-03 เป็น Must และ FR-11 เป็น Could/Needs Validation |
| E-05 / C-01 | นโยบายของตกค้างยังไม่ชัดเจน | กำหนด FR-09 และ NFR-07 เป็น Needs Validation |

## Files

- [x] อัปเดต `docs/05-requirement-backlog.md`
- [x] บันทึกหลักฐานการจัดลำดับใน `evidence/week-05/README.md`
- [x] อัปเดต worklog และ submission note สำหรับ Week 05