# Architecture Diagrams (W11) — Campus Lost and Found

โฟลเดอร์นี้รวบรวมไดอะแกรมสถาปัตยกรรมระดับแนวคิด (Conceptual Architecture - C4 Model Level 1 & 2) ของระบบ **Campus Lost and Found (Case 05)** ตามสัญญาการส่งงานสัปดาห์ที่ 11

| ไฟล์ | เนื้อหา |
|---|---|
| `11-context.drawio` + `11-context.png` | **C4 ระดับ 1 (System Context):** ระบบ Campus Lost and Found 1 กล่องส่วนกลาง · Actors ครบ 4 บทบาท (ACT-01 Requester, ACT-02 Finder, ACT-03 Staff, ACT-04 IT Admin) · ระบบภายนอก (EXT-01 Identity, EXT-02 Notification, EXT-03 Storage) พร้อมป้ายสถานะ Core / Extension / TBD และลูกศรระบุสิ่งที่ส่ง-รับ |
| `11-container.drawio` + `11-container.png` | **C4 ระดับ 2 (Container Diagram):** แสดง 4 ชิ้นส่วนที่ต้องรันจริง (Web Application, API Application, Database, File Storage) พร้อม [ชนิด · เทคโนโลยี], หน้าที่, เส้นโปรโตคอลการคุยกัน (REST/JSON, SQL, Secure Stream) และ Badge อ้างอิง Drivers D1–D3 และ Decision Cards |
| `11-bridge-w10-to-w11.png` | **ภาพที่ 1 ในเอกสาร Word:** ภาพเชื่อมโยงสถาปัตยกรรม: รับอะไรจาก W10 (Design Strategy), ผลิตอะไรใน W11 (Conceptual Architecture) และส่งต่ออะไรให้ W12 (UX/UI) และ W13 (Detailed Design) |
| `11-where-containers-run.png` | **ภาพที่ 4 ในเอกสาร Word:** สภาพแวดล้อมและเส้นแบ่งความไว้ใจ (Trust Boundary) ระหว่างเครื่องของผู้ใช้ (Client Browser) กับ server ที่ทีมควบคุม (API, Database, File Storage) |
| `11-d2-where-the-rule-lives.png` | **ภาพที่ 5 ในเอกสาร Word:** การวิเคราะห์เหตุผลว่าทำไมกติกาและ State Guard (D1 และ D2) ต้องอยู่ที่ API Application และ Database บน Server เพื่อป้องกันข้อมูลส่วนบุคคลหลุดและป้องกันการสวมรอยรับของ |

## Checklist ความสอดคล้อง

- [x] เปิดไฟล์ `.drawio` ในโปรแกรม diagrams.net (draw.io) ได้จริง โครงสร้าง XML ถูกต้องสมบูรณ์
- [x] มีไฟล์ `.png` คุณภาพสูง สำหรับใช้วางในไฟล์ Word `design/11-conceptual-architecture-v0.1.docx`
- [x] ชื่อกล่อง container และข้อกำหนดสอดคล้องกับ `design/00-design-spine.md` และ `design/10-design-strategy.md`
- [x] กติกาและข้อกำหนดความปลอดภัย D1–D3 อยู่บน Server ฝั่งที่ทีมควบคุมอย่างเข้มงวด
