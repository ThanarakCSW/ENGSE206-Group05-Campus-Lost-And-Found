#!/usr/bin/env python3
"""Generate design/11-conceptual-architecture-v0.1.docx for Case 05 (Campus Lost and Found)."""

import copy
import os
import shutil
import zipfile
import xml.etree.ElementTree as ET

ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
for prefix, uri in [
    ('w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'),
    ('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'),
    ('m', 'http://schemas.openxmlformats.org/officeDocument/2006/math'),
    ('wp', 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'),
    ('a', 'http://schemas.openxmlformats.org/drawingml/2006/main'),
    ('pic', 'http://schemas.openxmlformats.org/drawingml/2006/picture'),
]:
    ET.register_namespace(prefix, uri)

src_docx = '/tmp/crbs-example/design/11-conceptual-architecture-v0.1.docx'
dst_docx = 'design/11-conceptual-architecture-v0.1.docx'

with zipfile.ZipFile(src_docx, 'r') as z_in:
    doc_xml_bytes = z_in.read('word/document.xml')
    core_xml_bytes = z_in.read('docProps/core.xml')

tree = ET.fromstring(doc_xml_bytes)

def set_cell_text(cell, text):
    """Set text of a table cell, preserving formatting where possible."""
    p_list = cell.findall('.//w:p', ns)
    if not p_list:
        p = ET.SubElement(cell, f'{{{ns["w"]}}}p')
        p_list = [p]
    first_p = p_list[0]
    # Remove extra paragraphs
    for p in p_list[1:]:
        cell.remove(p)
    # Get run properties from first run if available
    first_r = first_p.find('.//w:r', ns)
    r_props = None
    if first_r is not None:
        r_pr = first_r.find('w:rPr', ns)
        if r_pr is not None:
            r_props = copy.deepcopy(r_pr)
    
    # Remove all existing runs
    for r in list(first_p.findall('.//w:r', ns)):
        first_p.remove(r)
    
    # Handle multi-line text
    lines = text.split('\n')
    for idx, line in enumerate(lines):
        r = ET.SubElement(first_p, f'{{{ns["w"]}}}r')
        if r_props is not None:
            r.append(copy.deepcopy(r_props))
        t = ET.SubElement(r, f'{{{ns["w"]}}}t')
        t.text = line
        if idx < len(lines) - 1:
            r_br = ET.SubElement(first_p, f'{{{ns["w"]}}}r')
            ET.SubElement(r_br, f'{{{ns["w"]}}}br')

# Update title paragraph
for p in tree.findall('.//w:p', ns):
    t_nodes = p.findall('.//w:t', ns)
    full_text = ''.join([t.text for t in t_nodes if t.text])
    if 'ระบบ: Campus Resource Booking System' in full_text:
        for t in t_nodes:
            t.text = ''
        t_nodes[0].text = 'ระบบ: Campus Lost and Found (ระบบแจ้งของหาย-พบของในมหาวิทยาลัย) — Group 05 (Case 05)'
    elif 'ภาพที่ 2 Context diagram ของ CRBS' in full_text:
        for t in t_nodes:
            t.text = ''
        t_nodes[0].text = 'ภาพที่ 2 Context diagram ของ Campus Lost and Found (C4 ระดับ 1) — ระบบ 1 กล่อง ผู้ใช้ และระบบภายนอก'
    elif 'ภาพที่ 3 Container diagram ของ CRBS' in full_text:
        for t in t_nodes:
            t.text = ''
        t_nodes[0].text = 'ภาพที่ 3 Container diagram ของ Campus Lost and Found (C4 ระดับ 2) — 4 ชิ้นที่ต้องรัน ชนิด · stack และเส้นที่บอกว่าส่งอะไร'
    elif 'ภาพที่ 4 แต่ละ container รันที่ไหน' in full_text:
        for t in t_nodes:
            t.text = ''
        t_nodes[0].text = 'ภาพที่ 4 แต่ละ container รันที่ไหน และใครควบคุม — เส้นแบ่งความไว้ใจของ Campus Lost and Found'
    elif 'ภาพที่ 5 ทำไมที่อยู่ของกติกาสำคัญ' in full_text:
        for t in t_nodes:
            t.text = ''
        t_nodes[0].text = 'ภาพที่ 5 ทำไมที่อยู่ของกติกาสำคัญ — Drivers D1 & D2 ของ Campus Lost and Found เมื่อผู้ใช้พยายามข้ามขั้นตอนหรือดูข้อมูลส่วนบุคคล'
    elif full_text.startswith('ระบบรับผิดชอบ: ข้อมูลทรัพยากร'):
        for t in t_nodes:
            t.text = ''
        t_nodes[0].text = 'ระบบรับผิดชอบ: รับแจ้งของหายและค้นหารายการของที่พบ · รับแจ้งเบาะแสและพิกัดพบของแบบไม่ระบุตัวตน · บันทึกรับเข้าคลังและเบลอร์ภาพส่วนบุคคล (PDPA) · รับไฟล์หลักฐานยืนยันตน (≤ 10MB) แบบส่วนตัว · ตรวจสอบหลักฐานและเปลี่ยนสถานะคำร้อง · บันทึกการส่งมอบสิ่งของคืน (Returned) · ควบคุมสิทธิ์ RBAC และบันทึก Audit Log ทุกขั้นตอน · สรุปรายงานสิ่งของตกค้างเกินกำหนด (Unclaimed)'
    elif full_text.startswith('ไม่รับผิดชอบ: การเก็บรหัสผ่าน'):
        for t in t_nodes:
            t.text = ''
        t_nodes[0].text = 'ไม่รับผิดชอบ: การติดตามพัสดุหรือจัดส่งสิ่งของทางไปรษณีย์ · กล้องวงจรปิด (CCTV) และระบบรักษาความปลอดภัยกายภาพ · การตรวจสอบสิทธิ์ทางกฎหมายเต็มรูปแบบ / คดีความ · การขายทอดตลาด / ประมูล / ทำลายทรัพย์สินจริง · การส่งข้อความแจ้งเตือนภายนอกที่ยังไม่ยืนยัน integration · การจัดสรรอัตรากำลังเจ้าหน้าที่กายภาพประจำตึก'
    elif full_text.startswith('W12: ทุกหน้าจอ (ค้นหา'):
        for t in t_nodes:
            t.text = ''
        t_nodes[0].text = 'W12: ทุกหน้าจอ (ค้นหารายการของที่พบ · ฟอร์มแจ้งเบาะแส · ฟอร์มแจ้งของหาย · ฟอร์มยื่นหลักฐาน · คิวตรวจคำร้องและจัดการคลังของ Staff) อยู่ใน Web Application และระบุว่าเรียก API เรื่องอะไร'
    elif full_text.startswith('W12: ข้อความบนหน้าจอตรงกับ Request State'):
        for t in t_nodes:
            t.text = ''
        t_nodes[0].text = 'W12: ข้อความบนหน้าจอตรงกับ State (Pending = ยื่นแล้ว รอเจ้าหน้าที่ตรวจสอบ ยังไม่ยืนยันสิทธิ์) · NFR-CLF-02 ออกแบบ Responsive UI บนคอมพิวเตอร์และมือถือ'
    elif full_text.startswith('W13: ซูมเข้า API Application เป็น component'):
        for t in t_nodes:
            t.text = ''
        t_nodes[0].text = 'W13: ซูมเข้า API Application เป็น component diagram (C4 ระดับ 3) แยกส่วน Blurring/Redaction, State Machine, Audit Logger และ Auth Guard'
    elif full_text.startswith('W13: sequence ใช้ lifeline'):
        for t in t_nodes:
            t.text = ''
        t_nodes[0].text = 'W13: sequence ใช้ lifeline = Web Application + component ใน API + Database + File Storage · action card อ้าง DEC-01 และ DEC-02'
    elif 'ซูมเข้าไปในกล่อง CRBS' in full_text:
        for t in t_nodes:
            t.text = ''
        t_nodes[0].text = 'ซูมเข้าไปในกล่อง Campus Lost and Found: ระบบมี 4 ชิ้นที่ต้องรัน — เว็บแอป · โปรแกรมฝั่ง server · ฐานข้อมูล · ที่เก็บไฟล์ปลอดภัย — แต่ละชิ้นบอกชนิด เทคโนโลยี และหน้าที่ (ภาพที่ 3 อยู่ท้ายหัวข้อนี้)'
    elif 'ระบบ 1 กล่อง + ใครมาใช้ + ระบบภายนอก' in full_text:
        for t in t_nodes:
            t.text = ''
        t_nodes[0].text = 'ระบบ 1 กล่อง + ใครมาใช้ + ระบบภายนอก — ตอบคำถามว่า อะไรอยู่ในระบบเรา อะไรอยู่ข้างนอก ยังไม่มีกล่องย่อยในภาพนี้ (ภาพที่ 2 อยู่ท้ายหัวข้อนี้)'

tables = tree.findall('.//w:tbl', ns)

# Table 0: Intro Box
set_cell_text(tables[0].findall('.//w:tc', ns)[0],
    'เอกสารนี้\n'
    'ต่อจาก design/10-design-strategy.md และ design/00-design-spine.md ของทีม (W10) — ภาพทุกภาพมีไฟล์ .drawio ที่ diagrams/architecture/\n'
    'อ้าง SRS ของทีม docs/07-srs-v1.md: actor หัวข้อ 2.2 · NFR หัวข้อ 4–5 · BR หัวข้อ 4 · ข้อมูล หัวข้อ 6 · Open Issues หัวข้อ 10\n'
    'Campus Lost and Found เป็นโครงงานรายวิชา ENGSE206; stack เป็น stack อ้างอิงของรายวิชา (Proposed)'
)

# Table 1: Team Meta
rows_t1 = tables[1].findall('.//w:tr', ns)
set_cell_text(rows_t1[0].findall('.//w:tc', ns)[1], 'Group 05 — ENGSE206-Group05-Campus-Lost-And-Found')
set_cell_text(rows_t1[1].findall('.//w:tc', ns)[1], 'ธนรัก ชุ่มสวัสดิ์ (Editor / Lead) · นรบดี บุญเลิศ (Quality / Design)')
set_cell_text(rows_t1[2].findall('.//w:tc', ns)[1], 'Case 05 — ระบบแจ้งของหาย-พบของในมหาวิทยาลัย (Campus Lost and Found)')
set_cell_text(rows_t1[3].findall('.//w:tc', ns)[1], 'v0.1 — Design Draft / 5 ต.ค. 2026')
set_cell_text(rows_t1[4].findall('.//w:tc', ns)[1], 'docs/07-srs-v1.md (Case-05-SRS-W07-v1) — Baseline Candidate (not approved baseline); OI-01–OI-08 ยังเปิด')
set_cell_text(rows_t1[5].findall('.//w:tc', ns)[1], 'design/10-design-strategy.md + design/00-design-spine.md ฉบับส่ง W10')
set_cell_text(rows_t1[6].findall('.//w:tc', ns)[1], 'ใช้ stack อ้างอิง React · Node.js + Express · PostgreSQL — Proposed (ยืนยันกับ Dev: DD-06)')
set_cell_text(rows_t1[7].findall('.//w:tc', ns)[1], 'CR-01-SIM — Pending (ไม่นำมาใช้ในแบบนี้)')

# Table 2: สิ่งที่รับมาจาก W10
rows_t2 = tables[2].findall('.//w:tr', ns)
set_cell_text(rows_t2[1].findall('.//w:tc', ns)[1], 'Build now = แจ้งเบาะแส · รับเข้าคลัง/เบลอร์ภาพ · ค้นหาของที่พบ · ยื่นคำร้อง/หลักฐาน · ตรวจและตัดสินคำร้อง · ส่งมอบคืน; Overview = รายงานของตกค้าง · In-app notification; ยังไม่ทำ = ติดตามพัสดุภายนอก · กล้อง CCTV · แจ้งเตือนภายนอก')
set_cell_text(rows_t2[2].findall('.//w:tc', ns)[1], 'D1 Privacy Leak = พัง (BR-CLF-01) · D2 Pending Gate ป้องกันสวมรอย (FR-CLF-05) · D3 Audit Log ทุกการเปลี่ยนสถานะ (NFR-CLF-01)')
set_cell_text(rows_t2[3].findall('.//w:tc', ns)[1], 'วงจรสิ่งของหนึ่งชิ้น (Item & Claim Lifecycle) 7 ขั้น (ขั้น 1–6 Build now · ขั้น 7 Overview)')
set_cell_text(rows_t2[4].findall('.//w:tc', ns)[1], 'DD-01 ถึง DD-05 (ระยะเวลาเก็บของตกค้าง, เทคนิคการเบลอร์ภาพ, ช่องทางแจ้งเตือน, ฯลฯ)')

# Table 3: System Context
rows_t3 = tables[3].findall('.//w:tr', ns)
actors_ext = [
    ('ACT-01', 'ผู้ทำของหาย (Requester)', 'แจ้งของหาย · ค้นหารายการของที่พบ · ยื่นหลักฐาน (≤10MB)', 'รายการของที่พบ (censored) · สถานะคำร้อง · แจ้งเตือนในระบบ', 'Core'),
    ('ACT-02', 'ผู้พบของ (Finder)', 'แจ้งเบาะแสและพิกัดที่พบสิ่งของ (ไม่ระบุตัวตน)', 'รหัสติดตามเบาะแส · ผลบันทึกรับเรื่อง', 'Core'),
    ('ACT-03', 'เจ้าหน้าที่ (Staff)', 'บันทึกรับของ · เบลอร์ภาพส่วนบุคคล · ตรวจหลักฐาน · ปิดงานคืน', 'คิวคำร้องรอตรวจ · รายการของในคลัง · รายงานของตกค้าง', 'Core'),
    ('ACT-04', 'ผู้ดูแลระบบ (IT Admin)', 'กำหนดบทบาทสิทธิ์ (RBAC) · ตรวจสอบความปลอดภัย', 'บันทึก Audit Log · รายงานภาพรวมระบบ', 'Core (รุ่นแรกใช้ role fixture: DD-01)'),
    ('EXT-01', 'Institutional Identity Service', 'คำขอยืนยันตัวตน (Login Request)', 'User Reference · Role Claims (Student/Staff)', 'Core boundary; protocol และ field = TBD (DD-01)'),
    ('EXT-02', 'External Notification Service', 'คำขอส่งข้อความแจ้งเตือนสถานะคำร้อง', 'ผลการส่ง (เมื่อเปิดใช้)', 'Extension — รุ่นแรกใช้ in-app notification (DD-03)'),
    ('EXT-03', 'Object Storage Service', 'อัปโหลดภาพ (censored) / ไฟล์หลักฐาน (private)', 'File URL / Secure Stream [DR-02]', 'Core boundary · Secure Storage'),
]
for idx, data in enumerate(actors_ext):
    cells = rows_t3[idx + 1].findall('.//w:tc', ns)
    for c_idx, val in enumerate(data):
        set_cell_text(cells[c_idx], val)

# Table 4: Container Table
# We need 4 containers: Web Application, API Application, Database, File Storage.
# Existing Table 4 has 4 rows (1 header + 3 data). Let's duplicate row 3 to make a 4th data row for File Storage!
rows_t4 = tables[4].findall('.//w:tr', ns)
if len(rows_t4) == 4:
    new_tr = copy.deepcopy(rows_t4[3])
    tables[4].append(new_tr)
    rows_t4 = tables[4].findall('.//w:tr', ns)

containers_data = [
    ('Web Application', 'หน้าจอสำหรับ Requester, Finder, Staff และ IT Admin: ค้นหา · แจ้งเบาะแส · ยื่นหลักฐาน · คิวตรวจคำร้องและจัดการคลัง; แสดงเมนูตาม role', 'เว็บแอปในเบราว์เซอร์ Responsive · React', 'เบราว์เซอร์บนเครื่องหรือมือถือของผู้ใช้ — ผู้ใช้ควบคุม', 'ไม่เก็บข้อมูลถาวร', 'API Application — เรียก API ค้นหา · แจ้งเบาะแส · ส่งคำร้อง · ตัดสิน · ดูสถานะ [REST/JSON · HTTPS]'),
    ('API Application', 'กติกา BR-CLF-01 (เบลอร์ภาพ/เซ็นเซอร์ข้อมูลส่วนบุคคล) · ตรวจสิทธิ์ RBAC (NFR-CLF-01) · State Guard ตรึง Pending ป้องกันสวมรอย (D2) · ตรวจไฟล์แนบ ≤10MB (FR-CLF-04) · บันทึก Audit Log ทุก action (D3)', 'โปรแกรมฝั่ง server · Node.js + Express', 'server ของทีม — ทีมควบคุม', 'ไม่เก็บเอง — อ่าน/เขียนผ่าน Database และ File Storage', 'Database [SQL · transaction] · File Storage [Secure Stream] · EXT-01 [protocol = TBD] · EXT-02 (Extension)'),
    ('Database', 'เก็บข้อมูลเชิงโครงสร้างทั้งหมด (DR-01 ถึง DR-04) · แหล่งเดียวของ State และ Audit Log รองรับ ACID Transaction (D2, D3)', 'ฐานข้อมูลเชิงสัมพันธ์ · PostgreSQL', 'server ฐานข้อมูล — ทีมควบคุม · เข้าถึงผ่าน API เท่านั้น', 'DR-01 ถึง DR-04, Audit Logs', 'API Application เท่านั้น'),
    ('File Storage', 'เก็บภาพถ่ายสิ่งของที่เบลอร์แล้ว (Public) และไฟล์หลักฐานยืนยันตน (DR-02 Private ≤ 10MB) ป้องกัน Direct Public URL', 'พื้นที่จัดเก็บไฟล์ปลอดภัย · Secure Object Storage', 'server จัดเก็บไฟล์ของทีม — ทีมควบคุม', 'Blurred item images, Encrypted private proof files', 'API Application เท่านั้น'),
]
for idx, data in enumerate(containers_data):
    cells = rows_t4[idx + 1].findall('.//w:tc', ns)
    for c_idx, val in enumerate(data):
        set_cell_text(cells[c_idx], val)

# Table 6: What team chooses
rows_t6 = tables[6].findall('.//w:tr', ns)
team_choices = [
    ('เว็บแอปในเบราว์เซอร์', 'ใช้', 'ทุก actor ใช้ผ่านหน้าจอทั่วไปได้ทั้งบน PC และมือถือ · NFR-CLF-02 (Responsive Web โหลด ≤ 3s บน 4G)'),
    ('แอปมือถือ', 'ไม่ใช้ในรุ่นแรก', 'SRS ไม่มี requirement ที่ต้องใช้ความสามารถเฉพาะเครื่อง เช่น Bluetooth beacon หรือ background tracking'),
    ('แอป desktop', 'ไม่ใช้', 'ไม่มีงานที่ต้องเปิดค้างทั้งวันหรือใช้อุปกรณ์ต่อพ่วงในเครื่อง'),
    ('โปรแกรมฝั่ง server (API)', 'ใช้', 'กติกา BR-CLF-01, NFR-CLF-01, D1, D2 และ Audit Log (D3) ต้องอยู่ฝั่งที่ทีมควบคุมเท่านั้น'),
    ('ฐานข้อมูล', 'ใช้', 'DR-01 ถึง DR-04 ต้องเก็บถาวร · D2 และ D3 ต้องอาศัย ACID Transaction ป้องกันข้อมูลขัดแย้ง'),
    ('งานตามเวลา', 'ไม่ใช้ในรุ่นแรก', 'รายงานของตกค้าง (FR-CLF-08) สรุปเมื่อเจ้าหน้าที่เปิดดู (On-demand query) ยังไม่มีงานเบื้องหลังที่ต้องตั้งเวลา'),
]
for idx, data in enumerate(team_choices):
    cells = rows_t6[idx + 1].findall('.//w:tc', ns)
    for c_idx, val in enumerate(data):
        set_cell_text(cells[c_idx], val)

# Table 7: NFR impact on containers
# Table 7 has 9 rows. Case 05 has 5 NFRs. We will use the first 5 rows and remove rows 6-8 if needed, or update.
rows_t7 = tables[7].findall('.//w:tr', ns)
nfrs_data = [
    ('BR-CLF-01', 'ปิดบังเลขบัตร ข้อมูลติดต่อ และภาพส่วนบุคคลก่อนเผยแพร่สู่สาธารณะ', 'API Application มี Interceptor ตรวจสอบและเบลอร์ภาพก่อนบันทึก/ส่งออก', 'DEC-01'),
    ('NFR-CLF-01', 'จำกัดสิทธิ์ตามบทบาท Public, Requester, Staff, IT Admin และซ่อนหลักฐานจากผู้ที่ไม่ใช่เจ้าหน้าที่', 'API Application ตรวจทุก endpoint; File Storage แยก private bucket; Web App แค่ซ่อนเมนู', 'DEC-01, DEC-02'),
    ('FR-CLF-04 / CT-01', 'ไฟล์แนบหลักฐานขนาดไม่เกิน 10MB ส่งแบบส่วนตัว', 'API Application ตรวจสอบ Content-Length และ Multipart stream ปฏิเสธไฟล์เกิน 10MB ทันที', 'DEC-01'),
    ('FR-CLF-05 / D2', 'เปลี่ยนสถานะคำร้องเป็น pending, verified, rejected, returned พร้อมบันทึกเหตุผล', 'API Application คุม State Machine (Pending Gate) และบันทึก Database transaction เดียวกับ Audit Log', 'DEC-01, DEC-02'),
    ('NFR-CLF-02', 'แสดงผลแบบ Responsive Web บนอุปกรณ์มือถือ (โหลด ≤ 3s บน 4G)', 'Web Application ออกแบบโครงสร้างหน้าจอใน W12', 'ส่งต่อ W12'),
]
for idx, data in enumerate(nfrs_data):
    cells = rows_t7[idx + 1].findall('.//w:tc', ns)
    for c_idx, val in enumerate(data):
        set_cell_text(cells[c_idx], val)
# Remove extra rows in Table 7
while len(tables[7].findall('.//w:tr', ns)) > len(nfrs_data) + 1:
    tables[7].remove(tables[7].findall('.//w:tr', ns)[-1])

# Table 8: DEC-01
rows_dec1 = tables[8].findall('.//w:tr', ns)
set_cell_text(rows_dec1[0].findall('.//w:tc', ns)[0], 'DEC-01   กติกาความปลอดภัยและการตรวจสิทธิ์อยู่ที่ API Application ไม่ใช่ที่หน้าเว็บ   [Proposed]')
set_cell_text(rows_dec1[1].findall('.//w:tc', ns)[1], 'API Application เป็นที่เดียวที่ตรวจกติกา BR-CLF-01 (เบลอร์ภาพ/เซ็นเซอร์ข้อมูล), NFR-CLF-01 (ตรวจสิทธิ์ RBAC ทุก action) และ State Guard')
set_cell_text(rows_dec1[2].findall('.//w:tc', ns)[1], 'D1 (Privacy Leak = พัง) · D2 (Pending Gate) · BR-CLF-01 · NFR-CLF-01')
set_cell_text(rows_dec1[3].findall('.//w:tc', ns)[1], 'ตรวจที่หน้าเว็บอย่างเดียว — ผู้ใช้สามารถข้ามหน้าเว็บหรือยิง API ตรงได้ และอาจเห็นภาพก่อนเบลอร์ผ่าน Network Inspect')
set_cell_text(rows_dec1[4].findall('.//w:tc', ns)[1], 'หน้าเว็บยังตรวจเบื้องต้นได้เพื่อความสะดวก (UX) แต่ผลตัดสินทางความปลอดภัยและสิทธิ์อยู่ที่ API เสมอ')

# Table 9: DEC-02
rows_dec2 = tables[9].findall('.//w:tr', ns)
set_cell_text(rows_dec2[0].findall('.//w:tc', ns)[0], 'DEC-02   ฐานข้อมูลเดียวที่รองรับ transaction เป็นแหล่งความจริงของ State และ Audit Log   [Proposed]')
set_cell_text(rows_dec2[1].findall('.//w:tc', ns)[1], 'เก็บ DR-01–DR-04 และตาราง AuditLog ใน Database เดียว และให้การเปลี่ยนสถานะคำร้องกับการบันทึก AuditLog อยู่ใน transaction เดียวกัน')
set_cell_text(rows_dec2[2].findall('.//w:tc', ns)[1], 'D2 · D3 · FR-CLF-05 · NFR-CLF-01 · การเปลี่ยนสถานะต้องผูกกับหลักฐานและผู้ทำรายการเสมอ')
set_cell_text(rows_dec2[3].findall('.//w:tc', ns)[1], 'แยกเก็บสถานะและ Audit Log คนละที่ — อาจทำให้เกิดสถานะเปลี่ยนแต่ไม่มี Log หรือ Log บันทึกแต่สถานะไม่เปลี่ยนเมื่อเกิดข้อผิดพลาด')
set_cell_text(rows_dec2[4].findall('.//w:tc', ns)[1], 'ฐานข้อมูลต้องรองรับ ACID Transaction (PostgreSQL) · การันตีว่าทุกการตัดสินใจตรวจสอบย้อนหลังได้ 100%')

# Table 10: DEC-03
rows_dec3 = tables[10].findall('.//w:tr', ns)
set_cell_text(rows_dec3[0].findall('.//w:tc', ns)[0], 'DEC-03   เว็บแอปเดียวแบบ Responsive Web Application รองรับทุก Actor ตามบทบาท   [Proposed]')
set_cell_text(rows_dec3[1].findall('.//w:tc', ns)[1], 'Requester, Finder, Staff และ IT Admin ใช้ Web Application เดียวกันผ่านเบราว์เซอร์ แต่แสดงเมนูและหน้าจอตาม role')
set_cell_text(rows_dec3[2].findall('.//w:tc', ns)[1], 'NFR-CLF-02 · ทุก actor ใช้งานผ่านหน้าจอทั่วไปได้ทั้งบน PC และสมาร์ตโฟน · SRS ไม่มี requirement ที่ต้องใช้ความสามารถเฉพาะของฮาร์ดแวร์มือถือ')
set_cell_text(rows_dec3[3].findall('.//w:tc', ns)[1], 'พัฒนา Native Mobile App แยกต่างหาก — เพิ่มภาระงานพัฒนาและการบำรุงรักษาโดยไม่มี requirement บังคับ')
set_cell_text(rows_dec3[4].findall('.//w:tc', ns)[1], 'W12 มุ่งเน้นออกแบบ Responsive Web UI ให้ใช้งานได้สะดวกทั้งบนจอคอมพิวเตอร์และมือถือ · สิทธิ์จริงยังตรวจที่ API (DEC-01)')

# Table 11: DEC-04
rows_dec4 = tables[11].findall('.//w:tr', ns)
set_cell_text(rows_dec4[0].findall('.//w:tc', ns)[0], 'DEC-04   ใช้ stack อ้างอิงของรายวิชา: React · Node.js + Express · PostgreSQL   [Proposed]')
set_cell_text(rows_dec4[1].findall('.//w:tc', ns)[1], 'Web Application = React · API Application = Node.js + Express (REST API ส่ง JSON ผ่าน HTTPS) · Database = PostgreSQL · File Storage = Secure Object Storage')
set_cell_text(rows_dec4[2].findall('.//w:tc', ns)[1], 'ตรงกับชนิดที่ DEC-01–03 ต้องการ · PostgreSQL รองรับ ACID transaction (D2, D3) · หน้าเว็บกับ API ใช้ JavaScript/TypeScript ร่วมกันและทีมมีความคุ้นเคย')
set_cell_text(rows_dec4[3].findall('.//w:tc', ns)[1], 'stack อื่นในเมนู — ใช้ได้เหมือนกัน แต่ไม่มีเหตุผลจาก NFR ให้เปลี่ยน และเพิ่มความเสี่ยงด้านเวลา')
set_cell_text(rows_dec4[4].findall('.//w:tc', ns)[1], 'version และการตั้งโปรเจกต์ = DD-06 ให้ Dev ยืนยัน · ไม่ใช้ microservices หรือ message broker เกินความจำเป็นในรุ่นแรก')

# Table 12: Spine walk
rows_spine = tables[12].findall('.//w:tr', ns)
spine_walk = [
    ('1', 'ผู้พบของแจ้งเบาะแสและพิกัดพบสิ่งของแบบไม่เปิดเผยตัวตน', 'UC-03', 'Build now', 'Web/Mobile → API (Anonymous Intake) → Database & File Storage'),
    ('2', 'เจ้าหน้าที่บันทึกรับเข้าคลังส่วนกลางและเบลอร์ภาพส่วนบุคคล', 'UC-01, UC-06', 'Build now', 'Web (Staff) → API (Redaction & Blurring) → Database & File Storage'),
    ('3', 'ผู้ทำของหายค้นหารายการสิ่งของที่พบผ่านหน้าสาธารณะ', 'UC-01, UC-02', 'Build now', 'Web/Mobile → API (Public Filtered View) → Database'),
    ('4', 'ผู้ทำของหายยื่นคำร้องและแนบไฟล์หลักฐาน (≤ 10MB)', 'UC-04', 'Build now', 'Web/Mobile → API (Upload Validator, Pending Gate) → Database & Storage'),
    ('5', 'เจ้าหน้าที่เปิดตรวจหลักฐานส่วนตัวและเปลี่ยนสถานะ (Verified/Rejected)', 'UC-05', 'Build now', 'Web (Staff) → API (Private Viewer, State Decision) → Database (Transaction + Audit)'),
    ('6', 'ผู้ทำของหายติดต่อรับของ และเจ้าหน้าที่ส่งมอบพร้อมปิดงาน (Returned)', 'UC-05', 'Build now', 'Web (Staff) → API (Handover Logger, State=Returned) → Database (Transaction + Audit)'),
    ('7', 'ระบบสรุปรายงานสิ่งของตกค้างเกินกำหนด (Unclaimed Items Report)', 'UC-01', 'Overview', 'Web (Staff/Admin) → API (Report Generator) → Database'),
    ('ทุกแถว', 'ควบคุมสิทธิ์ตามบทบาท (RBAC) และบันทึก Audit Log ทุกขั้นตอน', 'UC-06', 'Build now (cross-cutting)', 'ตรวจสิทธิ์ที่ API ทุก Action · Audit Log ลง Database'),
]
for idx, data in enumerate(spine_walk):
    cells = rows_spine[idx + 1].findall('.//w:tc', ns)
    for c_idx, val in enumerate(data):
        set_cell_text(cells[c_idx], val)

# Table 13: Open Decisions
rows_dd = tables[13].findall('.//w:tr', ns)
dd_data = [
    ('DD-01', 'identity service และ protocol/field ที่ส่งมา (OI-04)', 'API Application + EXT-01', 'role fixture: ผู้ใช้ทดสอบพร้อม role ที่กำหนดล่วงหน้า · ไม่เก็บรหัสผ่าน', 'Security / IT Admin'),
    ('DD-02', 'เทคนิคการเบลอร์และเซ็นเซอร์ภาพถ่าย (Manual vs Automatic) (OI-06)', 'API Application + File Storage', 'รุ่นแรกรองรับ Manual Blurring โดยเจ้าหน้าที่ตรวจสอบและเซ็นเซอร์ก่อนกด Publish', 'ผู้ดูแลระบบ IT / ผู้บริหาร'),
    ('DD-03', 'ช่องทางการแจ้งเตือนอัตโนมัติภายนอก (OI-08)', 'API Application + EXT-02', 'รุ่นแรกใช้วิธีแสดงผล In-app Notification บนหน้าเว็บของผู้ใช้', 'ผู้ดูแลระบบ IT'),
    ('DD-04', 'นโยบายระยะเวลาจัดเก็บสิ่งของตกค้าง (OI-07)', 'API Application + Database', 'รุ่นแรกใช้ตัวกรอง 30 วันในรายงานของตกค้าง (Overview) โดยยังไม่ทำการตัดโอนหรือทำลายของจริง', 'ผู้บริหารมหาวิทยาลัย'),
    ('DD-05', 'นโยบายการสำรองข้อมูลและระยะเวลาจัดเก็บหลักฐานส่วนบุคคล (Data Retention)', 'Database + File Storage', 'ไม่ลบไฟล์หลักฐานและ audit log ในรุ่นแรกระหว่างรอนโยบาย PDPA มหาวิทยาลัย', 'Data / Compliance Reviewer'),
    ('DD-06 (ใหม่)', 'ยืนยัน version ของ Stack และเครื่องมือทดสอบ', 'ทุก container', 'ใช้ stack อ้างอิงตาม DEC-04 ระหว่างรอ Dev ยืนยัน', 'ทีมพัฒนาระบบ (Dev)'),
]
for idx, data in enumerate(dd_data):
    cells = rows_dd[idx + 1].findall('.//w:tc', ns)
    for c_idx, val in enumerate(data):
        set_cell_text(cells[c_idx], val)

# Table 14: AI use
rows_ai = tables[14].findall('.//w:tr', ns)
set_cell_text(rows_ai[1].findall('.//w:tc', ns)[0], 'Antigravity (Google DeepMind) — 5 ต.ค.')
set_cell_text(rows_ai[1].findall('.//w:tc', ns)[1], 'จัดโครงหัวข้อและตารางสถาปัตยกรรม (C4 context/container, NFR mapping, decision cards, Spine walk)')
set_cell_text(rows_ai[1].findall('.//w:tc', ns)[2], 'ธนรักและนรบดีตรวจเทียบกับ docs/07 หัวข้อ 2.2, 4–6, 10 และ design/10 ไม่เพิ่ม requirement หรือแต่งค่านโยบายเกินจริง · stack เป็น stack อ้างอิง')

# Table 15: Team Worklog (2 members)
rows_worklog = tables[15].findall('.//w:tr', ns)
worklog_data = [
    ('ธนรัก ชุ่มสวัสดิ์ (ThanarakCSW)', 'W11-A, W11-C · Editor', 'หัวข้อ 1, 2, 5, 6 (DEC-01–04), 9–11 · รวมเอกสาร Word · ภาพที่ 1, 2, 4, 5', 'design/11-conceptual-architecture-v0.1.docx · diagrams/architecture/'),
    ('นรบดี บุญเลิศ (nara-bodee)', 'W11-B, W11-D · Spine', 'หัวข้อ 3, 4, 7 (Spine บน Container), 8 (DD-01–06) · ภาพที่ 3 Container · บอร์ด Miro W11 ก่อน/หลังแก้ · ใบส่งงาน', 'diagrams/architecture/11-container.drawio · evidence/week-11/ · submissions/week-11-submission.md'),
]
for idx, data in enumerate(worklog_data):
    cells = rows_worklog[idx + 1].findall('.//w:tc', ns)
    for c_idx, val in enumerate(data):
        set_cell_text(cells[c_idx], val)
# Remove extra 2 member rows from Table 15
while len(tables[15].findall('.//w:tr', ns)) > len(worklog_data) + 1:
    tables[15].remove(tables[15].findall('.//w:tr', ns)[-1])

# Serialize updated document.xml
updated_doc_xml = ET.tostring(tree, encoding='utf-8', xml_declaration=True)

# Replace images in media
media_replacements = {
    'word/media/79f3f11027ea74d07f916ddc7a3ad84f7c827e83.png': 'diagrams/architecture/11-bridge-w10-to-w11.png',
    'word/media/4ce82aede0b8b78f3a62f0352add0906c2942d65.png': 'diagrams/architecture/11-context.png',
    'word/media/5d65d8b8df02756331a6091c668459b599a2438a.png': 'diagrams/architecture/11-container.png',
    'word/media/4be4f79dc03fb946bd4de7378eb71c2742052a0b.png': 'diagrams/architecture/11-where-containers-run.png',
    'word/media/3dac74718d6c6b2336ca158a4f96fc36e2b501b2.png': 'diagrams/architecture/11-d2-where-the-rule-lives.png',
}

# Update docProps/core.xml to reflect Group 05 and authors
core_tree = ET.fromstring(core_xml_bytes)
for elem in core_tree.iter():
    if elem.tag.endswith('title'):
        elem.text = 'Conceptual Architecture v0.1 — Campus Lost and Found'
    elif elem.tag.endswith('creator'):
        elem.text = 'Thanarak Chumsawat, Narabodee Boonlead'
updated_core_xml = ET.tostring(core_tree, encoding='utf-8', xml_declaration=True)

# Write to dst_docx
with zipfile.ZipFile(src_docx, 'r') as z_in, zipfile.ZipFile(dst_docx, 'w', zipfile.ZIP_DEFLATED) as z_out:
    for item in z_in.infolist():
        if item.filename == 'word/document.xml':
            z_out.writestr(item, updated_doc_xml)
        elif item.filename == 'docProps/core.xml':
            z_out.writestr(item, updated_core_xml)
        elif item.filename in media_replacements:
            with open(media_replacements[item.filename], 'rb') as img_f:
                z_out.writestr(item, img_f.read())
        else:
            z_out.writestr(item, z_in.read(item.filename))

print(f'Successfully built {dst_docx}')
