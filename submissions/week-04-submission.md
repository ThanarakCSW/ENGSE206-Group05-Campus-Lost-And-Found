# Week 04 Submission — AI Stakeholder Panel, Evidence and Negotiation

## 1. Assignment

| Field | Value |
|---|---|
| Assignment ID | `W04-v2.0` |
| Course URL/version read | https://github.com/se-rmutl/engse206-lab/blob/main/weeks/week-04-stakeholder-simulation-negotiation/assignment-contract.md |
| Case/Role Pack | Case 05 — Campus Lost and Found · `docs/00-project-profile.md` |
| Date checked | 2026-08-04 |

## 2. Artefacts

| Artefact | Path/URL | Owner | Status |
|---|---|---|---|
| AI Conversation Excerpt | [`evidence/week-04/ai-conversation-excerpt.md`](../evidence/week-04/ai-conversation-excerpt.md) | ธนรัก ชุ่มสวัสดิ์ | Done |
| Requirement Candidates | [`docs/04-requirement-candidates.md`](../docs/04-requirement-candidates.md) | นรบดี บุญเลิศ | Done |
| Simulation Log (ไม่บังคับ) | [`evidence/week-04/ai-stakeholder-simulation-log.md`](../evidence/week-04/ai-stakeholder-simulation-log.md) | ธนรัก ชุ่มสวัสดิ์ | Done |
| Evidence/Conflict/RC | [`docs/04-evidence-log.md`](../docs/04-evidence-log.md) | ธนรัก ชุ่มสวัสดิ์, นรบดี บุญเลิศ | Done |
| Risk/Issue Log | [`project-management/risk-and-issue-log.md`](../project-management/risk-and-issue-log.md) | ธนรัก ชุ่มสวัสดิ์ | Done |
| Decision Log | [`project-management/decision-log.md`](../project-management/decision-log.md) | นรบดี บุญเลิศ | Done |
| Work/AI Logs | `project-management/team-worklog.md` · `project-management/ai-use-log.md` | ทุกคน | Updated |

## 3. Metrics and Quality Check

| Check | Value |
|---|---|
| Number of roles/sessions | 5 roles / 5 sessions (Loser, Finder, IT Admin, Executive, Officer) |
| Number of E-IDs | 5 (E-01–E-05) |
| Conflicts negotiated | 3 (C-01, C-02, C-03 — All Provisional) |
| Requirement candidates | 5 (RC-01–RC-05) |

- [x] each role uses a separate session
- [x] every evidence has source/tag/context/confidence/follow-up
- [x] conflict includes authority, interests, options and status/rationale
- [x] RCs cite E-IDs and do not claim real-world approval
- [x] no PII/confidential data; AI use and human review are recorded

## 4. Team Contribution

| Member | Role/work | Commit/file evidence |
|---|---|---|
| ธนรัก ชุ่มสวัสดิ์ | Evidence Owner / Facilitator — สรุป Simulation Evidence (E-01..E-05), จัดทำ Negotiation Record และทางเลือก Provisional | `docs/04-evidence-log.md`, `evidence/week-04/ai-conversation-excerpt.md` |
| นรบดี บุญเลิศ | Conflict Analyst / Reviewer — วิเคราะห์ Issue/Conflict (C-01..C-03) และจัดทำ Requirement Candidates (RC-01..RC-05) | `docs/04-evidence-log.md`, `docs/04-requirement-candidates.md` |

## 5. Tabletop Summary

- **Important evidence:** E-01 (ข้อมูลกระจัดกระจาย ขาดระบบกลาง), E-02 (ความกังวลเรื่องมิจฉาชีพสวมรอยรับของ), E-03 (ความเสี่ยงละเมิด PDPA จากภาพถ่ายส่วนบุคคล), E-04 (ผู้พบของกลัวภาระและความรับผิดชอบ), E-05 (ยังขาดนโยบายระยะเวลาจัดเก็บของตกค้าง)
- **Conflict and parties:**
  - C-01: ผู้บริหาร vs เจ้าหน้าที่ (ระยะเวลาเก็บของตกค้าง vs ข้อจำกัดพื้นที่คลัง)
  - C-02: ผู้ใช้ vs IT/เจ้าหน้าที่ (ความสะดวกในการค้นหาภาพชัดเจน vs ข้อบังคับ PDPA)
  - C-03: ผู้พบของ vs เจ้าหน้าที่ (การแจ้งพิกัดไม่เปิดเผยตัวตน vs ความถูกต้องและการนำของเข้าคลัง)
- **Options/status/rationale:**
  - C-01: Provisional เลือก Option C (แยกตามประเภทสิ่งของ ของมีค่า 90 วัน, ของทั่วไป 30 วัน)
  - C-02: Provisional เลือก Option C (Role-based Access + Automatic Blurring ภาพสาธารณะ)
  - C-03: Provisional เลือก Option C (แจ้งพิกัดไม่เปิดเผยตัวตน และแจ้งเตือนเจ้าหน้าที่พื้นที่ไปเก็บ)
- **Evidence-linked RC:** E-01..E-05 ลากโยงสู่ RC-01..RC-05 ครบถ้วน โดยระบุ Need และระดับความมั่นใจชัดเจน
- **Unresolved issue/Week 05 verification:** นโยบายการจัดการสิ่งของตกค้าง (Unclaimed items) ที่ต้องยืนยันตัวเลขกับผู้บริหารใน Week 05

## 6. Final Snapshot

| Field | Value |
|---|---|
| Commit | `submit(w04): evidence and requirement candidates` |
| Commit hash/time | `6cf8479` / 2026-08-04 |
| Known limitations/open questions | ยังรอความชัดเจนเรื่องข้อกำหนดนโยบายจัดเก็บสิ่งของตกค้างและหลักเกณฑ์การตรวจสอบกรรมสิทธิ์ |
