# Design Spine — เส้นทางงานหลักหนึ่งชิ้นของ Campus Lost and Found

> ตารางนี้โตขึ้นทุกสัปดาห์: W10 เติมคอลัมน์ "W10 ระดับ"; W11 เติม "W11 กล่องที่รับผิดชอบ"; W12 เติม "หน้าจอ"; W13 เติม "action/data/rule"  
> แถว = ขั้นที่ผู้ใช้/ระบบทำจริงตามลำดับ 5–8 แถว จาก Core use case ใน `docs/06-requirement-models.md`  
> ระดับ: **Build now** = Dev เริ่มเขียนได้หลัง W13 | **Overview** = อยู่ในภาพรวม/ข้อมูล/กติกา ยังไม่มีหน้าจอ-contract ละเอียด | **Later** = increment ถัดไป

แกนของระบบ Campus Lost and Found คือ **"วงจรสิ่งของหนึ่งชิ้น (Item & Claim Lifecycle)"** — เริ่มตั้งแต่มีผู้พบของ/แจ้งหาย การรับเข้าคลังส่วนกลาง การยื่นคำร้องพร้อมหลักฐานส่วนตัว การตรวจสอบสิทธิ์ และจบลงที่การส่งมอบสิ่งของคืนแก่เจ้าของจริงอย่างถูกต้องตามกฎหมาย PDPA

| # | ขั้นในเส้นทาง | Actor | UC | AC หลัก | W10 ระดับ | W11 กล่องที่รับผิดชอบ | W12 หน้าจอ | W13 action / data / rule |
|---|---|---|---|---|---|---|---|---|
| 1 | ผู้พบของแจ้งเบาะแสและพิกัดพบสิ่งของแบบไม่เปิดเผยตัวตน | ผู้พบของ (Finder) | UC-03 | AC-04 | Build now | Web/Mobile → API (Anonymous Intake) → Database | | |
| 2 | เจ้าหน้าที่บันทึกรับเข้าคลังส่วนกลางและเบลอร์ภาพส่วนบุคคล | เจ้าหน้าที่ (Staff) | UC-01, UC-06 | AC-01, AC-07 | Build now | Web (Staff) → API (Image Blurring & Censorship) → Database | | |
| 3 | ผู้ทำของหายค้นหารายการสิ่งของที่พบผ่านหน้าสาธารณะ | ผู้ทำของหาย (Requester) | UC-01, UC-02 | AC-02, AC-03 | Build now | Web/Mobile → API (Public Filtered View) → Database | | |
| 4 | ผู้ทำของหายยื่นคำร้องและแนบไฟล์หลักฐาน (≤ 10MB) | ผู้ทำของหาย (Requester) | UC-04 | AC-05 | Build now | Web/Mobile → API (Upload Validator, State=Pending) → Database | | |
| 5 | เจ้าหน้าที่เปิดตรวจหลักฐานส่วนตัวและเปลี่ยนสถานะ (Verified / Rejected) | เจ้าหน้าที่ (Staff) | UC-05 | AC-06 | Build now | Web (Staff) → API (Private Evidence Viewer, State Decision) → Database | | |
| 6 | ผู้ทำของหายติดต่อรับของ และเจ้าหน้าที่ส่งมอบพร้อมปิดงาน (Returned) | ผู้ทำของหาย / เจ้าหน้าที่ | UC-05 | AC-06 | Build now | Web (Staff) → API (Handover Logger, State=Returned) → Database | | |
| 7 | ระบบสรุปรายงานสิ่งของตกค้างเกินกำหนด (Unclaimed Items Report) | เจ้าหน้าที่ / ผู้บริหาร | UC-01 | AC-01 | Overview | Web (Staff/Admin) → API (Report Generator) → Database | | |
| ทุกแถว | ควบคุมสิทธิ์ตามบทบาท (RBAC) และบันทึก Audit Log ทุกขั้นตอน | ทุก Actor | UC-06 | AC-08 | Build now (Cross-cutting) | ตรวจสิทธิ์ที่ API ทุก Action · Audit Log ลง Database | | |

## บันทึกการเปลี่ยนแปลง

| สัปดาห์ | เปลี่ยนอะไร | เพราะ |
|---|---|---|
| W10 | สร้างครั้งแรก: 7 แถว เติมคอลัมน์ "W10 ระดับ" (ขั้น 1–6 Build now · ขั้น 7 Overview) | ใช้ "วงจรสิ่งของหนึ่งชิ้น" เป็นแกนหลักในการเชื่อมโยง Use Cases ทั้ง 6 เรื่องใน `docs/06-requirement-models.md` |
| W11 | เติมคอลัมน์ "W11 กล่องที่รับผิดชอบ" ทั้ง 7 แถว (Web/Mobile · API Application · Database) | สอดคล้องกับสถาปัตยกรรมระดับ Container (C4 Model) ใน `design/11-conceptual-architecture-v0.1.docx` |
