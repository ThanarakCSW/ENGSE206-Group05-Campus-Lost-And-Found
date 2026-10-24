# Activity Diagrams

ใส่ workflow หลักและ alternate flow ที่สำคัญ

| ไฟล์ | เนื้อหา | เชื่อมกับ |
|---|---|---|
| [`w06-claim-verification-activity.drawio`](w06-claim-verification-activity.drawio) · [`w06-claim-verification-activity.png`](w06-claim-verification-activity.png) | Swimlane 3 lane (Requester · System · Staff): ยื่นคำร้องยืนยันความเป็นเจ้าของ (UC-04, FR-CLF-04) → ตรวจขนาดไฟล์ ≤ 10MB → บันทึกสถานะ Pending → ตรวจสอบหลักฐานแบบส่วนตัว (UC-05, FR-CLF-05) → Decision (Verified / Rejected) → นัดหมายส่งมอบของ → บันทึกสถานะ Returned (AC-06) | [`docs/06-requirement-models.md`](../../docs/06-requirement-models.md) UC-04, UC-05, AC-05, AC-06 · [`docs/07-srs-v1.md`](../../docs/07-srs-v1.md) |

## Checklist

- [x] มี source file ที่แก้ไขได้ (`.drawio`)
- [x] มี PNG export สำหรับใช้ในเอกสาร (`.png`)
- [x] ชื่อไฟล์สื่อถึง purpose
- [x] เชื่อมโยงกับ requirement/design document
