# Requirements Change Log

> บันทึกแบบสรุปของการเปลี่ยน requirement ตลอดภาคเรียน; รายละเอียด validation อยู่ใน `08-validation-traceability.md`

| Date | Change ID | Requirement(s) | Type | Summary | Reason | Impacted Design | Status |
|---|---|---|---|---|---|---|---|
| 2026-09-15 | CR-01-SIM | FR-CLF-02, FR-CLF-05, BR-CLF-01 | Changed (ข้อเสนอจำลอง — ยังไม่เปลี่ยนจริง) | ขอให้เพิ่มระบบจับคู่อัตโนมัติ (AI Auto-matching) ระหว่างคำร้องของหายกับของที่พบในคลังทันทีที่บันทึก | ผู้ใช้งาน (สถานการณ์จำลอง W08) ต้องการทราบผลจับคู่ทันทีเพื่อความรวดเร็ว แต่ยังไม่มีหลักฐานและนโยบายรองรับความถูกต้อง | กระทบ Form แจ้งของหาย (UC-02), ขั้นตอนตรวจสอบของเจ้าหน้าที่ (UC-05), สถาปัตยกรรม AI Service และความเสี่ยงส่งมอบผิดคน | Open — Decision Pending (Product Owner / Policy Owner) |

## หมายเหตุ

- Requirement ที่ใช้ใน W06–W08 คงตาม `docs/05-requirement-backlog.md` ที่ล็อกใน tag `baseline-v1.0` — ยังไม่มีการเปลี่ยน requirement ใดที่ได้รับการอนุมัติให้แก้ไข Baseline
- ประเด็น RV-01-SIM เป็นการปรับแก้ข้อความฝึกจำลอง (Seeded Error) ให้สอดคล้องกับกติกาความปลอดภัย ไม่ใช่การเปลี่ยน requirement
- ประเด็นระยะเวลาจัดเก็บสิ่งของตกค้าง (OI-CLF-01) และสถาปัตยกรรมเซ็นเซอร์ภาพ (OI-CLF-02) เป็น Open Issues ที่รอการตัดสินใจจากผู้มีอำนาจ
- รายละเอียด Impact Analysis ของ CR-01-SIM บันทึกไว้ใน [`08-validation-traceability.md`](08-validation-traceability.md) ส่วน B หัวข้อ B4
