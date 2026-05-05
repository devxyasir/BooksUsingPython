#!/usr/bin/env python3
"""
Mastering Python & DSA — Beautiful PDF Book Generator
"""

import re, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, PageBreak, KeepTogether, NextPageTemplate
)
from reportlab.platypus.flowables import Flowable

PAGE_W, PAGE_H = A4
ML, MR, MT, MB = 22*mm, 22*mm, 28*mm, 22*mm
CW = PAGE_W - ML - MR

# ── Color Palette (Python / Teal Green theme) ─────────────────────────────────
P = {
    'cover':        HexColor('#0A1F1A'),
    'cover_mid':    HexColor('#0F2E26'),
    'cover_accent': HexColor('#10B981'),
    'primary':      HexColor('#059669'),
    'primary_d':    HexColor('#047857'),
    'primary_l':    HexColor('#ECFDF5'),
    'dark':         HexColor('#0A1F1A'),
    'heading':      HexColor('#064E3B'),
    'sub':          HexColor('#065F46'),
    'text':         HexColor('#374151'),
    'muted':        HexColor('#9CA3AF'),
    'code_bg':      HexColor('#F0FDF4'),
    'code_bd':      HexColor('#6EE7B7'),
    'code_txt':     HexColor('#064E3B'),
    'tip_bg':       HexColor('#F0FDF4'),
    'tip_bd':       HexColor('#10B981'),
    'tip_txt':      HexColor('#065F46'),
    'err_bg':       HexColor('#FEF2F2'),
    'err_bd':       HexColor('#DC2626'),
    'err_txt':      HexColor('#991B1B'),
    'int_bg':       HexColor('#EFF6FF'),
    'int_bd':       HexColor('#2563EB'),
    'int_txt':      HexColor('#1D4ED8'),
    'ex_bg':        HexColor('#FAF5FF'),
    'ex_bd':        HexColor('#7C3AED'),
    'ex_txt':       HexColor('#5B21B6'),
    'tbl_hdr':      HexColor('#059669'),
    'tbl_even':     HexColor('#FAFAFA'),
    'tbl_odd':      HexColor('#FFFFFF'),
    'border':       HexColor('#E5E7EB'),
    'rule':         HexColor('#A7F3D0'),
    'sec_accent':   HexColor('#34D399'),
}


# ── Custom Flowables ───────────────────────────────────────────────────────────

class SectionDivider(Flowable):
    def __init__(self, number, title, subtitle=''):
        Flowable.__init__(self)
        self.number = number
        self.title = title
        self.subtitle = subtitle
        self.width = CW
        self.height = 78*mm

    def wrap(self, aw, ah):
        return CW, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.setFillColor(P['primary_l'])
        c.roundRect(0, 0, w, h, 6, fill=1, stroke=0)
        c.setFillColor(P['primary'])
        c.rect(0, 0, 5, h, fill=1, stroke=0)
        c.setFillColor(HexColor('#D1FAE5'))
        c.setFont('Helvetica-Bold', 96)
        c.drawString(w - 60*mm, 8, self.number)
        c.setFillColor(P['primary'])
        c.setFont('Helvetica-Bold', 9)
        c.drawString(14, h - 18, 'S E C T I O N')
        c.setFillColor(P['heading'])
        c.setFont('Helvetica-Bold', 22)
        if len(self.title) > 35:
            words = self.title.split()
            mid = len(words)//2
            c.drawString(14, h - 44, ' '.join(words[:mid]))
            c.drawString(14, h - 62, ' '.join(words[mid:]))
        else:
            c.drawString(14, h - 44, self.title)
        if self.subtitle:
            c.setFillColor(P['sub'])
            c.setFont('Helvetica', 10)
            c.drawString(14, 14, self.subtitle[:80])


class CodeBox(Flowable):
    def __init__(self, lines, label=''):
        Flowable.__init__(self)
        self.lines = lines
        self.label = label
        self.pad = 10
        self.fs = 7.8
        self.lh = 10.5

    def wrap(self, aw, ah):
        self.width = aw
        top_extra = 16 if self.label else 0
        self.height = len(self.lines) * self.lh + self.pad * 2 + top_extra + 4
        return self.width, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.setFillColor(HexColor('#E5E7EB'))
        c.roundRect(2, -2, w, h, 5, fill=1, stroke=0)
        c.setFillColor(P['code_bg'])
        c.roundRect(0, 0, w, h, 5, fill=1, stroke=0)
        c.setStrokeColor(P['code_bd'])
        c.setLineWidth(0.6)
        c.roundRect(0, 0, w, h, 5, fill=0, stroke=1)
        if self.label:
            c.setFillColor(P['code_bd'])
            c.roundRect(0, h - 16, w, 16, 5, fill=1, stroke=0)
            c.rect(0, h - 16, w, 8, fill=1, stroke=0)
            c.setFillColor(P['sub'])
            c.setFont('Courier', 7)
            c.drawString(self.pad, h - 11, self.label)
        for i, col in enumerate([HexColor('#FC6058'), HexColor('#FEC02F'), HexColor('#2ACA44')]):
            c.setFillColor(col)
            c.circle(self.pad + i*12, h - 8, 3.5, fill=1, stroke=0)
        c.setFont('Courier', self.fs)
        c.setFillColor(P['code_txt'])
        top_offset = 16 if self.label else 0
        start_y = h - self.pad - self.fs - top_offset
        for line in self.lines:
            disp = line.rstrip()
            if len(disp) > 105:
                disp = disp[:102] + '...'
            c.drawString(self.pad, start_y, disp)
            start_y -= self.lh
            if start_y < self.pad:
                break


class Callout(Flowable):
    CONFIGS = {
        'tip':       ('#F0FDF4', '#10B981', '#065F46', 'PRO TIP'),
        'mistake':   ('#FEF2F2', '#DC2626', '#991B1B', 'COMMON MISTAKE'),
        'interview': ('#EFF6FF', '#2563EB', '#1D4ED8', 'INTERVIEW QUESTION'),
        'exercise':  ('#FAF5FF', '#7C3AED', '#5B21B6', 'EXERCISE'),
    }

    def __init__(self, lines, kind='tip'):
        Flowable.__init__(self)
        self.lines = lines
        self.kind = kind
        cfg = self.CONFIGS.get(kind, self.CONFIGS['tip'])
        self.bg, self.bd, self.tc = HexColor(cfg[0]), HexColor(cfg[1]), HexColor(cfg[2])
        self.label = cfg[3]
        self.pad = 10
        self.lh = 13

    def wrap(self, aw, ah):
        self.width = aw
        self.height = len(self.lines) * self.lh + self.pad * 2 + 18
        return self.width, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.setFillColor(self.bg)
        c.roundRect(0, 0, w, h, 5, fill=1, stroke=0)
        c.setFillColor(self.bd)
        c.roundRect(0, 0, 5, h, 2, fill=1, stroke=0)
        c.rect(3, 0, 2, h, fill=1, stroke=0)
        c.setFillColor(self.bd)
        c.setFont('Helvetica-Bold', 7.5)
        c.drawString(14, h - 14, self.label)
        c.setStrokeColor(self.bd)
        c.setLineWidth(0.3)
        c.line(14, h - 17, w - 10, h - 17)
        c.setFont('Helvetica', 9.5)
        c.setFillColor(self.tc)
        y = h - 18 - self.lh + 2
        for line in self.lines:
            c.drawString(14, y, line[:105])
            y -= self.lh
            if y < self.pad - 4:
                break


class HRule(Flowable):
    def __init__(self, color=None, thickness=0.5):
        Flowable.__init__(self)
        self.color = color or P['rule']
        self.thickness = thickness

    def wrap(self, aw, ah):
        self.width = aw
        return aw, 1

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 0, self.width, 0)


# ── Page Templates ─────────────────────────────────────────────────────────────

def cover_canvas(cv, doc):
    cv.saveState()
    cv.setFillColor(P['cover'])
    cv.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    cv.setFillColor(P['cover_mid'])
    cv.circle(PAGE_W + 20*mm, PAGE_H - 20*mm, 110*mm, fill=1, stroke=0)
    cv.setFillColor(HexColor('#0A1A15'))
    cv.circle(-20*mm, 40*mm, 80*mm, fill=1, stroke=0)
    cv.setFillColor(HexColor('#064E3B'))
    cv.circle(PAGE_W - 50*mm, PAGE_H - 60*mm, 60*mm, fill=1, stroke=0)
    cv.setFillColor(HexColor('#059669'))
    cv.circle(PAGE_W - 50*mm, PAGE_H - 60*mm, 36*mm, fill=1, stroke=0)
    cv.setFillColor(P['cover_accent'])
    cv.rect(0, PAGE_H - 5*mm, PAGE_W, 5*mm, fill=1, stroke=0)
    cv.setFillColor(HexColor('#064E3B'))
    cv.rect(0, 0, 4*mm, PAGE_H, fill=1, stroke=0)
    cv.setFillColor(HexColor('#0E2A22'))
    for row in range(7):
        for col in range(5):
            cv.circle(ML + col*16*mm, PAGE_H - 70*mm - row*16*mm, 2, fill=1, stroke=0)
    cv.setFillColor(HexColor('#0E2A22'))
    cv.setFont('Helvetica-Bold', 130)
    cv.drawString(8*mm, PAGE_H/2 - 50*mm, 'PYTHON')
    cv.setFillColor(HexColor('#34D399'))
    cv.setFont('Helvetica-Bold', 10)
    cv.drawString(ML, PAGE_H - 78*mm, 'T H E   C O M P L E T E   L E A R N I N G   G U I D E')
    cv.setFillColor(P['cover_accent'])
    cv.rect(ML, PAGE_H - 84*mm, 18*mm, 3, fill=1, stroke=0)
    cv.setFillColor(white)
    cv.setFont('Helvetica-Bold', 40)
    cv.drawString(ML, PAGE_H - 108*mm, 'Mastering')
    cv.setFillColor(HexColor('#6EE7B7'))
    cv.setFont('Helvetica-Bold', 40)
    cv.drawString(ML, PAGE_H - 128*mm, 'Python & DSA')
    cv.setFillColor(P['cover_accent'])
    cv.rect(ML, PAGE_H - 138*mm, 65*mm, 2, fill=1, stroke=0)
    cv.setFillColor(HexColor('#94A3B8'))
    cv.setFont('Helvetica', 13)
    cv.drawString(ML, PAGE_H - 150*mm, 'From Beginner to Advanced Thinking')
    bx = ML
    by = PAGE_H - 175*mm
    for badge in ['16 Sections', 'Python Basics', 'Data Structures', 'OOP', 'Algorithms']:
        bw = len(badge) * 5.8 + 14
        cv.setFillColor(HexColor('#064E3B'))
        cv.roundRect(bx, by - 4, bw, 17, 4, fill=1, stroke=0)
        cv.setStrokeColor(HexColor('#10B981'))
        cv.setLineWidth(0.6)
        cv.roundRect(bx, by - 4, bw, 17, 4, fill=0, stroke=1)
        cv.setFillColor(HexColor('#6EE7B7'))
        cv.setFont('Helvetica-Bold', 7.5)
        cv.drawString(bx + 7, by + 1, badge)
        bx += bw + 6
    cv.setFillColor(HexColor('#64748B'))
    cv.setFont('Helvetica', 9.5)
    cv.drawString(ML, PAGE_H - 195*mm, 'A complete conceptual guide to Python programming and data structures & algorithms.')
    cv.drawString(ML, PAGE_H - 205*mm, 'Concepts first. Code second. Understanding always.')
    cv.setFillColor(HexColor('#080E0C'))
    cv.rect(0, 0, PAGE_W, 42*mm, fill=1, stroke=0)
    cv.setStrokeColor(HexColor('#064E3B'))
    cv.setLineWidth(0.5)
    cv.line(0, 42*mm, PAGE_W, 42*mm)
    cv.setFillColor(HexColor('#475569'))
    cv.setFont('Helvetica', 8)
    topics = 'Variables  |  Functions  |  Lists  |  Trees  |  Graphs  |  Recursion  |  Dynamic Programming  |  Heaps'
    cv.drawCentredString(PAGE_W/2, 18*mm, topics)
    cv.setFillColor(HexColor('#064E3B'))
    cv.setFont('Helvetica-Bold', 8)
    cv.drawCentredString(PAGE_W/2, 28*mm, 'TOPICS COVERED')
    cv.restoreState()


def content_canvas(cv, doc):
    cv.saveState()
    cv.setStrokeColor(P['primary'])
    cv.setLineWidth(2)
    cv.line(ML, PAGE_H - 16*mm, PAGE_W - MR, PAGE_H - 16*mm)
    cv.setFont('Helvetica', 7.5)
    cv.setFillColor(P['muted'])
    cv.drawString(ML, PAGE_H - 13*mm, 'Mastering Python & DSA: From Beginner to Advanced Thinking')
    cv.setStrokeColor(P['border'])
    cv.setLineWidth(0.5)
    cv.line(ML, MB - 6*mm, PAGE_W - MR, MB - 6*mm)
    cv.setFont('Helvetica', 8)
    cv.setFillColor(P['muted'])
    cv.drawCentredString(PAGE_W/2, MB - 10*mm, str(doc.page))
    cv.restoreState()


# ── Styles ─────────────────────────────────────────────────────────────────────

def make_styles():
    S = {}
    S['body'] = ParagraphStyle('body', fontName='Helvetica', fontSize=10.5,
        leading=17, textColor=P['text'], alignment=TA_JUSTIFY, spaceAfter=6, spaceBefore=2)
    S['body_l'] = ParagraphStyle('body_l', fontName='Helvetica', fontSize=10.5,
        leading=17, textColor=P['text'], alignment=TA_LEFT, spaceAfter=5)
    S['h1'] = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=22,
        leading=28, textColor=P['primary'], spaceBefore=4, spaceAfter=10)
    S['h2'] = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=16,
        leading=22, textColor=P['heading'], spaceBefore=16, spaceAfter=5)
    S['h3'] = ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=13,
        leading=18, textColor=P['sub'], spaceBefore=10, spaceAfter=4)
    S['h4'] = ParagraphStyle('h4', fontName='Helvetica-Bold', fontSize=11,
        leading=16, textColor=P['sub'], spaceBefore=6, spaceAfter=3)
    S['bullet'] = ParagraphStyle('bullet', fontName='Helvetica', fontSize=10.5,
        leading=16, textColor=P['text'], leftIndent=16, bulletIndent=2,
        spaceAfter=3, spaceBefore=1)
    S['bullet2'] = ParagraphStyle('bullet2', fontName='Helvetica', fontSize=10,
        leading=15, textColor=P['text'], leftIndent=32, bulletIndent=20, spaceAfter=2)
    S['num'] = ParagraphStyle('num', fontName='Helvetica', fontSize=10.5,
        leading=16, textColor=P['text'], leftIndent=20, spaceAfter=4)
    S['toc_title'] = ParagraphStyle('toc_title', fontName='Helvetica-Bold',
        fontSize=26, leading=32, textColor=P['heading'], spaceAfter=20)
    S['toc1'] = ParagraphStyle('toc1', fontName='Helvetica-Bold', fontSize=12,
        leading=20, textColor=P['primary'], spaceAfter=1)
    S['toc2'] = ParagraphStyle('toc2', fontName='Helvetica', fontSize=9.5,
        leading=15, textColor=P['text'], leftIndent=18, spaceAfter=0)
    return S


def fmt(text):
    if not isinstance(text, str): return ''
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # Protect code blocks FIRST so asterisks inside backticks do not break bold/italic regexes
    code_blocks = {}
    def store_code(m):
        key = f'\x00CODE{len(code_blocks)}\x00'
        code_blocks[key] = f'<font name="Courier" size="9" color="#064E3B">{m.group(1)}</font>'
        return key
    text = re.sub(r'`([^`]+)`', store_code, text)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*([^*\n]+?)\*', r'<i>\1</i>', text)
    for key, val in code_blocks.items():
        text = text.replace(key, val)
    return text


def render_table(rows):
    if not rows: return None
    parsed = []
    for row in rows:
        cells = [c.strip() for c in row.strip('|').split('|')]
        parsed.append(cells)
    clean = [r for r in parsed if not all(re.match(r'^[-: ]+$', c) for c in r)]
    if not clean: return None
    ncols = max(len(r) for r in clean)
    for r in clean:
        while len(r) < ncols: r.append('')
    header_style = ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=9,
        textColor=white, leading=13, alignment=TA_CENTER)
    cell_style = ParagraphStyle('td', fontName='Helvetica', fontSize=9,
        textColor=P['text'], leading=13, alignment=TA_LEFT)
    table_data = []
    for i, row in enumerate(clean):
        style = header_style if i == 0 else cell_style
        table_data.append([Paragraph(fmt(c), style) for c in row])
    col_w = CW / ncols
    t = Table(table_data, colWidths=[col_w]*ncols, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), P['tbl_hdr']),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [P['tbl_odd'], P['tbl_even']]),
        ('GRID', (0,0), (-1,-1), 0.4, P['border']),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('LINEBELOW', (0,0), (-1,0), 1, P['primary_d']),
    ]))
    return t


TOC_DATA = [
    ("1", "Introduction to Programming", ["What is Programming?", "Why We Need Programming", "How Computers Think", "Why Python Is Used"]),
    ("2", "Python Basics", ["Variables", "Data Types", "Strings", "Numbers", "Input and Output", "Conditions", "Loops"]),
    ("3", "Functions", ["Why Functions Exist", "Parameters and Arguments", "Return Values", "Scope", "Reusability Thinking"]),
    ("4", "Data Structures in Python", ["List — The Flexible Container", "Dictionary — The Lookup System", "Set — Unique Items Only", "Tuple — Fixed Data"]),
    ("5", "Object-Oriented Programming", ["What Is OOP?", "Inheritance"]),
    ("6", "Advanced Python", ["List Comprehensions", "Generators", "Decorators", "Error Handling"]),
    ("7", "DSA Foundations", ["What Is DSA?", "Why DSA Matters", "Time Complexity", "Space Complexity"]),
    ("8", "Arrays and Strings", ["Arrays — The Building Block", "Searching", "Sorting — Bubble and Selection", "Two Pointers Technique"]),
    ("9", "Linked Lists", ["What Is a Linked List?", "Singly vs Doubly vs Circular"]),
    ("10", "Stacks and Queues", ["Stack — LIFO", "Queue — FIFO", "Applications"]),
    ("11", "Trees", ["Binary Tree", "Binary Search Tree (BST)", "Tree Traversals"]),
    ("12", "Graphs", ["What Is a Graph?", "Graph Traversals — BFS and DFS"]),
    ("13", "Recursion", ["What Is Recursion?", "Recursion on Arrays and Trees", "Common Recursive Patterns"]),
    ("14", "Dynamic Programming", ["What Is Dynamic Programming?", "0/1 Knapsack Pattern", "Longest Common Subsequence"]),
    ("15", "Hashing and Hash Tables", ["What Is Hashing?", "Hash Tables in DSA", "Applications of Hashing"]),
    ("16", "Heaps and Priority Queues", ["What Is a Heap?", "Priority Queue"]),
]


def build_toc(S):
    story = []
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph('Table of Contents', S['toc_title']))
    story.append(HRule(color=P['primary'], thickness=2))
    story.append(Spacer(1, 8*mm))
    for num, title, subs in TOC_DATA:
        story.append(Paragraph(f'<b>{num}.</b> {title}', S['toc1']))
        for s in subs:
            story.append(Paragraph(f'· {s}', S['toc2']))
        story.append(Spacer(1, 3*mm))
    story.append(PageBreak())
    return story


def parse_md(text, S):
    story = []
    lines = text.splitlines()
    i = 0
    in_code = False
    code_lines = []
    code_label = ''
    table_rows = []
    in_table = False

    CALLOUT_SECTIONS = {
        'interview questions': 'interview',
        'exercises': 'exercise',
        'pro tips': 'tip',
        'common mistakes': 'mistake',
    }

    def flush_table():
        nonlocal table_rows, in_table
        if table_rows:
            t = render_table(table_rows)
            if t:
                story.append(Spacer(1, 3*mm))
                story.append(t)
                story.append(Spacer(1, 4*mm))
        table_rows.clear()
        in_table.__class__  # no-op trick
        table_rows[:] = []
        return False

    def flush_code():
        nonlocal code_lines, in_code, code_label
        if code_lines:
            story.append(Spacer(1, 2*mm))
            story.append(CodeBox(list(code_lines), label=code_label))
            story.append(Spacer(1, 3*mm))
        code_lines.clear()
        return False, ''

    while i < len(lines):
        line = lines[i]

        if line.strip().startswith('```'):
            if in_code:
                flush_code()
                in_code = False
                code_label = ''
            else:
                if in_table:
                    flush_table()
                    in_table = False
                in_code = True
                code_label = line.strip()[3:].strip()
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        if line.strip().startswith('|'):
            if in_table:
                table_rows.append(line)
            else:
                in_table = True
                table_rows = [line]
            i += 1
            continue
        else:
            if in_table:
                flush_table()
                in_table = False

        if re.match(r'^[-─]{3,}$', line.strip()):
            story.append(Spacer(1, 3*mm))
            story.append(HRule())
            story.append(Spacer(1, 3*mm))
            i += 1
            continue

        if not line.strip():
            story.append(Spacer(1, 2*mm))
            i += 1
            continue

        h4 = re.match(r'^#### (.+)', line)
        h3 = re.match(r'^### (.+)', line)
        h2 = re.match(r'^## (.+)', line)
        h1 = re.match(r'^# (.+)', line)

        if h1:
            title = h1.group(1).strip()
            sec = re.match(r'^SECTION (\d+):\s*(.+)', title)
            if sec:
                story.append(PageBreak())
                story.append(Spacer(1, 5*mm))
                story.append(SectionDivider(sec.group(1), sec.group(2)))
                story.append(Spacer(1, 8*mm))
            else:
                story.append(Spacer(1, 4*mm))
                story.append(Paragraph(fmt(title), S['h1']))
                story.append(HRule(color=P['primary'], thickness=1.5))
                story.append(Spacer(1, 4*mm))
            i += 1
            continue

        if h2:
            title = h2.group(1).strip()
            title_lower = title.lower()
            matched_kind = None
            for key, kind in CALLOUT_SECTIONS.items():
                if key in title_lower:
                    matched_kind = kind
                    break

            if matched_kind:
                story.append(Spacer(1, 5*mm))
                story.append(HRule(color=P['border']))
                story.append(Spacer(1, 3*mm))
                story.append(Paragraph(fmt(title), S['h2']))
                i += 1
                callout_lines = []
                while i < len(lines) and not lines[i].startswith('#'):
                    cline = lines[i].strip()
                    if cline and not cline.startswith('```'):
                        clean = re.sub(r'\*\*(.+?)\*\*', r'\1', cline)
                        clean = re.sub(r'\*(.+?)\*', r'\1', clean)
                        clean = re.sub(r'`(.+?)`', r'\1', clean)
                        if len(clean) > 2:
                            callout_lines.append(clean[:100])
                    i += 1
                if callout_lines:
                    story.append(Callout(callout_lines[:20], kind=matched_kind))
                story.append(Spacer(1, 4*mm))
                continue

            story.append(Spacer(1, 2*mm))
            story.append(HRule(color=P['primary_l'], thickness=4))
            story.append(Spacer(1, 1*mm))
            story.append(Paragraph(fmt(title), S['h2']))
            i += 1
            continue

        if h3:
            story.append(Paragraph(fmt(h3.group(1).strip()), S['h3']))
            i += 1
            continue

        if h4:
            story.append(Paragraph(fmt(h4.group(1).strip()), S['h4']))
            i += 1
            continue

        bullet_m = re.match(r'^(\s*)[*\-]\s+(.+)', line)
        if bullet_m:
            indent = len(bullet_m.group(1))
            st = S['bullet2'] if indent >= 2 else S['bullet']
            story.append(Paragraph(f'<bullet>&bull;</bullet>{fmt(bullet_m.group(2))}', st))
            i += 1
            continue

        num_m = re.match(r'^\s*\d+\.\s+(.+)', line)
        if num_m:
            story.append(Paragraph(fmt(num_m.group(1)), S['num']))
            i += 1
            continue

        if line.strip():
            text_content = fmt(line.strip())
            if re.match(r'.*\*\*Pro Tip', line):
                clean = re.sub(r'\*\*(.+?)\*\*', r'\1', line.strip())
                clean = re.sub(r'`(.+?)`', r'\1', clean)
                story.append(Callout([clean[:100]], kind='tip'))
            elif re.match(r'.*\*\*Common Mistake', line):
                clean = re.sub(r'\*\*(.+?)\*\*', r'\1', line.strip())
                story.append(Callout([clean[:100]], kind='mistake'))
            else:
                story.append(Paragraph(text_content, S['body']))
        i += 1

    if in_table:
        flush_table()
    if in_code and code_lines:
        story.append(CodeBox(code_lines, label=code_label))

    return story


def build_book():
    OUT = 'Books/Mastering_Python_DSA_Book.pdf'
    S = make_styles()

    cover_frame = Frame(0, 0, PAGE_W, PAGE_H, leftPadding=0, rightPadding=0,
                        topPadding=0, bottomPadding=0)
    content_frame = Frame(ML, MB, CW, PAGE_H - MT - MB,
                          leftPadding=0, rightPadding=0,
                          topPadding=0, bottomPadding=0)

    cover_tpl = PageTemplate(id='Cover', frames=[cover_frame], onPage=cover_canvas)
    content_tpl = PageTemplate(id='Content', frames=[content_frame], onPage=content_canvas)

    doc = BaseDocTemplate(OUT, pagesize=A4,
                          pageTemplates=[cover_tpl, content_tpl],
                          title='Mastering Python & DSA: From Beginner to Advanced Thinking',
                          author='Muhammad Yasir (devxyasir)',
                          subject='Python Programming and Data Structures & Algorithms')

    story = []
    story.append(NextPageTemplate('Cover'))
    story.append(PageBreak())
    story.append(NextPageTemplate('Content'))
    story.append(PageBreak())
    story += build_toc(S)

    for path in ['PythonDSA/python_dsa_part1.md', 'PythonDSA/python_dsa_part2.md', 'PythonDSA/python_dsa_part3.md']:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'part1' in path:
            content = re.sub(r'^# Mastering Python & DSA.*\n.*\n', '', content, flags=re.MULTILINE)
        story += parse_md(content, S)

    print(f'Building PDF with {len(story)} story elements...')
    doc.build(story)
    print(f'Done! → {OUT}')
    return OUT


if __name__ == '__main__':
    os.makedirs('Books', exist_ok=True)
    build_book()
