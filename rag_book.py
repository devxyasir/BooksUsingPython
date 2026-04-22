#!/usr/bin/env python3
"""
RAG Complete Guide — Beautiful PDF Book Generator
Generates a professional, styled PDF from the RAG markdown guide.
"""

import re, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, PageBreak, KeepTogether, HRFlowable, NextPageTemplate
)
from reportlab.platypus.flowables import Flowable

# ── Dimensions ────────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4
ML, MR, MT, MB = 22*mm, 22*mm, 28*mm, 22*mm
CW = PAGE_W - ML - MR   # content width

# ── Color Palette ─────────────────────────────────────────────────────────────
P = {
    'cover':        HexColor('#0B1120'),
    'cover_mid':    HexColor('#112044'),
    'cover_accent': HexColor('#3B6FE8'),
    'primary':      HexColor('#3B6FE8'),
    'primary_d':    HexColor('#1D4ED8'),
    'primary_l':    HexColor('#EEF2FF'),
    'dark':         HexColor('#0F172A'),
    'heading':      HexColor('#1E293B'),
    'sub':          HexColor('#334155'),
    'text':         HexColor('#3D4E65'),
    'muted':        HexColor('#94A3B8'),
    'code_bg':      HexColor('#F1F5F9'),
    'code_bd':      HexColor('#CBD5E1'),
    'code_txt':     HexColor('#1E293B'),
    'tip_bg':       HexColor('#F0FDF4'),
    'tip_bd':       HexColor('#16A34A'),
    'tip_txt':      HexColor('#166534'),
    'err_bg':       HexColor('#FEF2F2'),
    'err_bd':       HexColor('#DC2626'),
    'err_txt':      HexColor('#991B1B'),
    'int_bg':       HexColor('#EFF6FF'),
    'int_bd':       HexColor('#2563EB'),
    'int_txt':      HexColor('#1D4ED8'),
    'ex_bg':        HexColor('#FAF5FF'),
    'ex_bd':        HexColor('#7C3AED'),
    'ex_txt':       HexColor('#5B21B6'),
    'tbl_hdr':      HexColor('#3B6FE8'),
    'tbl_even':     HexColor('#F8FAFC'),
    'tbl_odd':      HexColor('#FFFFFF'),
    'border':       HexColor('#E2E8F0'),
    'rule':         HexColor('#CBD5E1'),
    'sec_accent':   HexColor('#6366F1'),
}


# ── Custom Flowables ───────────────────────────────────────────────────────────

class SectionDivider(Flowable):
    """Full-page section divider."""
    def __init__(self, number, title, subtitle=''):
        Flowable.__init__(self)
        self.number = number
        self.title = title
        self.subtitle = subtitle
        self.width = CW
        self.height = 80*mm

    def wrap(self, aw, ah):
        return CW, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        # Background panel
        c.setFillColor(P['primary_l'])
        c.roundRect(0, 0, w, h, 6, fill=1, stroke=0)
        # Left accent bar
        c.setFillColor(P['primary'])
        c.rect(0, 0, 5, h, fill=1, stroke=0)
        # Large faded number
        c.setFillColor(HexColor('#DBEAFE'))
        c.setFont('Helvetica-Bold', 96)
        c.drawString(w - 60*mm, 10, self.number)
        # Section label
        c.setFillColor(P['primary'])
        c.setFont('Helvetica-Bold', 9)
        c.drawString(14, h - 18, 'S E C T I O N')
        # Title
        c.setFillColor(P['heading'])
        c.setFont('Helvetica-Bold', 24)
        # Handle long titles
        if len(self.title) > 32:
            words = self.title.split()
            mid = len(words)//2
            line1 = ' '.join(words[:mid])
            line2 = ' '.join(words[mid:])
            c.drawString(14, h - 44, line1)
            c.drawString(14, h - 64, line2)
        else:
            c.drawString(14, h - 44, self.title)
        # Subtitle
        if self.subtitle:
            c.setFillColor(P['sub'])
            c.setFont('Helvetica', 10)
            c.drawString(14, 14, self.subtitle[:80])


class CodeBox(Flowable):
    """Monospaced code / ASCII diagram block."""
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
        # Shadow (subtle)
        c.setFillColor(HexColor('#E2E8F0'))
        c.roundRect(2, -2, w, h, 5, fill=1, stroke=0)
        # Background
        c.setFillColor(P['code_bg'])
        c.roundRect(0, 0, w, h, 5, fill=1, stroke=0)
        # Border
        c.setStrokeColor(P['code_bd'])
        c.setLineWidth(0.6)
        c.roundRect(0, 0, w, h, 5, fill=0, stroke=1)
        # Label bar
        if self.label:
            c.setFillColor(P['code_bd'])
            c.roundRect(0, h - 16, w, 16, 5, fill=1, stroke=0)
            c.rect(0, h - 16, w, 8, fill=1, stroke=0)
            c.setFillColor(P['sub'])
            c.setFont('Courier', 7)
            c.drawString(self.pad, h - 11, self.label)
        # Dot decorations (macOS-style)
        dot_y = h - 8 if not self.label else h - 8
        for i, col in enumerate([HexColor('#FC6058'), HexColor('#FEC02F'), HexColor('#2ACA44')]):
            c.setFillColor(col)
            c.circle(self.pad + i*12, dot_y if not self.label else h - 8, 3.5, fill=1, stroke=0)
        # Code lines
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
    """Styled callout box: tip, mistake, interview, exercise."""
    CONFIGS = {
        'tip':       ('#F0FDF4', '#16A34A', '#166534', 'PRO TIP'),
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
        # Label
        c.setFillColor(self.bd)
        c.setFont('Helvetica-Bold', 7.5)
        c.drawString(14, h - 14, self.label)
        # Separator
        c.setStrokeColor(self.bd)
        c.setLineWidth(0.3)
        c.line(14, h - 17, w - 10, h - 17)
        # Content
        c.setFont('Helvetica', 9.5)
        c.setFillColor(self.tc)
        y = h - 18 - self.lh + 2
        for line in self.lines:
            disp = line[:105]
            c.drawString(14, y, disp)
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
    # Dark background
    cv.setFillColor(P['cover'])
    cv.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # Gradient overlay circles
    cv.setFillColor(P['cover_mid'])
    cv.circle(PAGE_W + 30*mm, PAGE_H - 10*mm, 120*mm, fill=1, stroke=0)
    cv.setFillColor(HexColor('#0A1835'))
    cv.circle(-20*mm, 50*mm, 90*mm, fill=1, stroke=0)
    # Glow circle
    cv.setFillColor(HexColor('#1D3A7A'))
    cv.circle(PAGE_W - 55*mm, PAGE_H - 55*mm, 65*mm, fill=1, stroke=0)
    cv.setFillColor(HexColor('#1E4DB8'))
    cv.circle(PAGE_W - 55*mm, PAGE_H - 55*mm, 40*mm, fill=1, stroke=0)
    # Top accent strip
    cv.setFillColor(P['cover_accent'])
    cv.rect(0, PAGE_H - 5*mm, PAGE_W, 5*mm, fill=1, stroke=0)
    # Left accent strip
    cv.setFillColor(HexColor('#1E3A7A'))
    cv.rect(0, 0, 4*mm, PAGE_H, fill=1, stroke=0)
    # Dot grid decoration
    cv.setFillColor(HexColor('#1A3060'))
    for row in range(7):
        for col in range(5):
            cv.circle(ML + col*16*mm, PAGE_H - 70*mm - row*16*mm, 2, fill=1, stroke=0)
    # "RAG" watermark text
    cv.setFillColor(HexColor('#0E1F45'))
    cv.setFont('Helvetica-Bold', 200)
    cv.drawString(10*mm, PAGE_H/2 - 70*mm, 'RAG')
    # Eyebrow
    cv.setFillColor(HexColor('#60A5FA'))
    cv.setFont('Helvetica-Bold', 10)
    cv.drawString(ML, PAGE_H - 78*mm, 'T H E   C O M P L E T E   T E C H N I C A L   G U I D E')
    # Accent rule
    cv.setFillColor(P['cover_accent'])
    cv.rect(ML, PAGE_H - 84*mm, 18*mm, 3, fill=1, stroke=0)
    # Main title line 1
    cv.setFillColor(white)
    cv.setFont('Helvetica-Bold', 44)
    cv.drawString(ML, PAGE_H - 108*mm, 'Retrieval-Augmented')
    # Main title line 2
    cv.setFillColor(HexColor('#93C5FD'))
    cv.setFont('Helvetica-Bold', 44)
    cv.drawString(ML, PAGE_H - 128*mm, 'Generation')
    # Sub rule
    cv.setFillColor(P['cover_accent'])
    cv.rect(ML, PAGE_H - 138*mm, 65*mm, 2, fill=1, stroke=0)
    # Subtitle
    cv.setFillColor(HexColor('#94A3B8'))
    cv.setFont('Helvetica', 14)
    cv.drawString(ML, PAGE_H - 150*mm, 'From Beginner to System Designer')
    # Badges row
    bx = ML
    by = PAGE_H - 175*mm
    for badge in ['9 Sections', 'Algorithms', 'Architecture', 'Design Patterns', 'Evaluation']:
        bw = len(badge) * 5.8 + 14
        cv.setFillColor(HexColor('#1D3A7A'))
        cv.roundRect(bx, by - 4, bw, 17, 4, fill=1, stroke=0)
        cv.setStrokeColor(HexColor('#3B6FE8'))
        cv.setLineWidth(0.6)
        cv.roundRect(bx, by - 4, bw, 17, 4, fill=0, stroke=1)
        cv.setFillColor(HexColor('#93C5FD'))
        cv.setFont('Helvetica-Bold', 7.5)
        cv.drawString(bx + 7, by + 1, badge)
        bx += bw + 6
    # Description
    cv.setFillColor(HexColor('#64748B'))
    cv.setFont('Helvetica', 9.5)
    cv.drawString(ML, PAGE_H - 195*mm, 'A comprehensive guide covering RAG foundations, core components,')
    cv.drawString(ML, PAGE_H - 205*mm, 'retrieval techniques, system architecture, scaling & evaluation.')
    # Bottom bar
    cv.setFillColor(HexColor('#060C1A'))
    cv.rect(0, 0, PAGE_W, 42*mm, fill=1, stroke=0)
    cv.setStrokeColor(HexColor('#1D3A7A'))
    cv.setLineWidth(0.5)
    cv.line(0, 42*mm, PAGE_W, 42*mm)
    cv.setFillColor(HexColor('#475569'))
    cv.setFont('Helvetica', 8)
    topics = 'Embeddings  |  Vector Databases  |  BM25  |  Hybrid Search  |  Re-ranking  |  Agentic RAG  |  Graph RAG  |  Security  |  Evaluation'
    cv.drawCentredString(PAGE_W/2, 18*mm, topics)
    cv.setFillColor(HexColor('#1D3A7A'))
    cv.setFont('Helvetica-Bold', 8)
    cv.drawCentredString(PAGE_W/2, 28*mm, 'TOPICS COVERED')
    cv.restoreState()


def content_canvas(cv, doc):
    cv.saveState()
    cv.setStrokeColor(P['primary'])
    cv.setLineWidth(2)
    cv.line(ML, PAGE_H - 16*mm, PAGE_W - MR, PAGE_H - 16*mm)
    # Header text
    cv.setFont('Helvetica', 7.5)
    cv.setFillColor(P['muted'])
    cv.drawString(ML, PAGE_H - 13*mm, 'The Complete Guide to Retrieval-Augmented Generation')
    # Footer line
    cv.setStrokeColor(P['border'])
    cv.setLineWidth(0.5)
    cv.line(ML, MB - 6*mm, PAGE_W - MR, MB - 6*mm)
    # Page number
    cv.setFont('Helvetica', 8)
    cv.setFillColor(P['muted'])
    cv.drawCentredString(PAGE_W/2, MB - 10*mm, str(doc.page))
    cv.restoreState()


# ── Style Registry ─────────────────────────────────────────────────────────────

def make_styles():
    S = {}
    S['body'] = ParagraphStyle('body', fontName='Helvetica', fontSize=10.5,
        leading=17, textColor=P['text'], alignment=TA_JUSTIFY, spaceAfter=6,
        spaceBefore=2)
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
        leading=15, textColor=P['text'], leftIndent=32, bulletIndent=20,
        spaceAfter=2)
    S['num'] = ParagraphStyle('num', fontName='Helvetica', fontSize=10.5,
        leading=16, textColor=P['text'], leftIndent=20, spaceAfter=4)
    S['toc_title'] = ParagraphStyle('toc_title', fontName='Helvetica-Bold',
        fontSize=26, leading=32, textColor=P['heading'], spaceAfter=20)
    S['toc1'] = ParagraphStyle('toc1', fontName='Helvetica-Bold', fontSize=12,
        leading=20, textColor=P['primary'], spaceAfter=1)
    S['toc2'] = ParagraphStyle('toc2', fontName='Helvetica', fontSize=9.5,
        leading=15, textColor=P['text'], leftIndent=18, spaceAfter=0)
    return S


# ── Inline Format ──────────────────────────────────────────────────────────────

def fmt(text):
    """Convert markdown inline → ReportLab XML markup."""
    if not isinstance(text, str): return ''
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*([^*\n]+?)\*', r'<i>\1</i>', text)
    text = re.sub(r'`([^`]+)`', lambda m: '<font name="Courier" size="9" color="#1E293B">' + m.group(1) + '</font>', text)
    return text


# ── Table Renderer ─────────────────────────────────────────────────────────────

def render_table(rows):
    """Convert markdown table rows → ReportLab Table flowable."""
    if not rows: return None

    # Parse rows
    parsed = []
    for row in rows:
        cells = [c.strip() for c in row.strip('|').split('|')]
        parsed.append(cells)

    # Remove separator rows (---|---|--)
    clean = [r for r in parsed if not all(re.match(r'^[-: ]+$', c) for c in r)]
    if not clean: return None

    # Normalize column count
    ncols = max(len(r) for r in clean)
    for r in clean:
        while len(r) < ncols: r.append('')

    # Build paragraph cells
    header_style = ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=9,
        textColor=white, leading=13, alignment=TA_CENTER)
    cell_style = ParagraphStyle('td', fontName='Helvetica', fontSize=9,
        textColor=P['text'], leading=13, alignment=TA_LEFT)

    table_data = []
    for i, row in enumerate(clean):
        style = header_style if i == 0 else cell_style
        table_data.append([Paragraph(fmt(c), style) for c in row])

    # Column widths: distribute evenly
    col_w = CW / ncols

    t = Table(table_data, colWidths=[col_w]*ncols, repeatRows=1)
    cmds = [
        ('BACKGROUND', (0,0), (-1,0), P['tbl_hdr']),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [P['tbl_odd'], P['tbl_even']]),
        ('GRID', (0,0), (-1,-1), 0.4, P['border']),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ROWBACKGROUNDS', (0,0), (-1,0), [P['tbl_hdr']]),
        ('LINEBELOW', (0,0), (-1,0), 1, P['primary_d']),
    ]
    t.setStyle(TableStyle(cmds))
    return t


# ── TOC ────────────────────────────────────────────────────────────────────────

TOC_DATA = [
    ("1", "Foundations", ["What is RAG?", "Why RAG is Needed", "Fine-tuning vs RAG vs Prompt Engineering", "Core Concepts: Embeddings, Similarity, Retrieval"]),
    ("2", "Core Components", ["Embedding Generation Pipeline", "Vector Database Internals & ANN Search", "Chunking Strategies & Trade-offs", "Indexing Pipeline", "Query Pipeline"]),
    ("3", "RAG Architecture", ["End-to-End System Design", "Data Ingestion Flow", "Retrieval Flow", "Generation Flow"]),
    ("4", "Retrieval Techniques", ["Dense vs Sparse Retrieval", "BM25 — Intuition & Formula", "Hybrid Search & RRF", "Re-ranking with Cross-Encoders", "Multi-Query Retrieval", "Context Compression"]),
    ("5", "Types of RAG Systems", ["Naive RAG", "Advanced RAG & HyDE", "Multi-hop RAG", "Agentic RAG", "Graph RAG", "Memory-Augmented RAG"]),
    ("6", "Optimization & Scaling", ["Latency Bottlenecks", "Cost Optimization", "Caching Logic & Semantic Cache", "Index Sharding & Distributed Search", "Accuracy vs Speed Trade-offs"]),
    ("7", "Evaluation", ["Retrieval Metrics: Precision, Recall, MRR", "Generation Metrics: Faithfulness, Relevancy", "Hallucination Detection", "RAG Evaluation Pipelines (RAGAS)"]),
    ("8", "Security & Risks", ["Prompt Injection — Internal Mechanics", "Data Leakage in RAG", "Secure Retrieval Design Principles"]),
    ("9", "Practical Design Patterns", ["Document Q&A System", "Chat with PDFs", "Enterprise Knowledge Assistant", "Codebase Assistant", "Customer Support Bot"]),
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


# ── Markdown Parser ────────────────────────────────────────────────────────────

def parse_md(text, S):
    """Parse markdown text → list of ReportLab flowables."""
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
        table_rows = []
        in_table = False

    def flush_code():
        nonlocal code_lines, in_code, code_label
        if code_lines:
            story.append(Spacer(1, 2*mm))
            story.append(CodeBox(code_lines, label=code_label))
            story.append(Spacer(1, 3*mm))
        code_lines = []
        in_code = False
        code_label = ''

    while i < len(lines):
        line = lines[i]

        # Code block toggle
        if line.strip().startswith('```'):
            if in_code:
                flush_code()
            else:
                if in_table: flush_table()
                in_code = True
                code_label = line.strip()[3:].strip()
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        # Table row
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

        # Skip pure separators within content
        if re.match(r'^[-─]{3,}$', line.strip()):
            story.append(Spacer(1, 3*mm))
            story.append(HRule())
            story.append(Spacer(1, 3*mm))
            i += 1
            continue

        # Blank line
        if not line.strip():
            story.append(Spacer(1, 2*mm))
            i += 1
            continue

        # Headings
        h4 = re.match(r'^#### (.+)', line)
        h3 = re.match(r'^### (.+)', line)
        h2 = re.match(r'^## (.+)', line)
        h1 = re.match(r'^# (.+)', line)

        if h1:
            title = h1.group(1).strip()
            # Check if it's a section header like "SECTION X: TITLE"
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

            # Check for special callout section headers
            matched_kind = None
            for key, kind in CALLOUT_SECTIONS.items():
                if key in title_lower:
                    matched_kind = kind
                    break

            if matched_kind:
                # Collect subsequent content for callout
                story.append(Spacer(1, 5*mm))
                story.append(HRule(color=P['border']))
                story.append(Spacer(1, 3*mm))
                story.append(Paragraph(fmt(title), S['h2']))
                i += 1
                # Collect items until next heading
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

        # Bullet list
        bullet_m = re.match(r'^(\s*)[*\-]\s+(.+)', line)
        if bullet_m:
            indent = len(bullet_m.group(1))
            st = S['bullet2'] if indent >= 2 else S['bullet']
            story.append(Paragraph(f'<bullet>&bull;</bullet>{fmt(bullet_m.group(2))}', st))
            i += 1
            continue

        # Numbered list
        num_m = re.match(r'^\s*\d+\.\s+(.+)', line)
        if num_m:
            story.append(Paragraph(fmt(num_m.group(1)), S['num']))
            i += 1
            continue

        # Regular paragraph
        if line.strip():
            text = fmt(line.strip())
            # Detect inline Pro Tip / Common Mistake paragraphs
            if re.match(r'.*\*\*Pro Tip', line):
                clean = re.sub(r'\*\*(.+?)\*\*', r'\1', line.strip())
                clean = re.sub(r'`(.+?)`', r'\1', clean)
                story.append(Callout([clean[:100]], kind='tip'))
            elif re.match(r'.*\*\*Common Mistake', line):
                clean = re.sub(r'\*\*(.+?)\*\*', r'\1', line.strip())
                story.append(Callout([clean[:100]], kind='mistake'))
            else:
                story.append(Paragraph(text, S['body']))
        i += 1

    if in_table: flush_table()
    if in_code: flush_code()

    return story


# ── Main Build ─────────────────────────────────────────────────────────────────

def build_book():
    OUT = '/mnt/user-data/outputs/RAG_Complete_Guide_Book.pdf'

    S = make_styles()

    # Frames
    cover_frame = Frame(0, 0, PAGE_W, PAGE_H, leftPadding=0, rightPadding=0,
                        topPadding=0, bottomPadding=0)
    content_frame = Frame(ML, MB, CW, PAGE_H - MT - MB,
                          leftPadding=0, rightPadding=0,
                          topPadding=0, bottomPadding=0)

    cover_tpl = PageTemplate(id='Cover', frames=[cover_frame],
                             onPage=cover_canvas)
    content_tpl = PageTemplate(id='Content', frames=[content_frame],
                               onPage=content_canvas)

    doc = BaseDocTemplate(OUT, pagesize=A4,
                          pageTemplates=[cover_tpl, content_tpl],
                          title='The Complete Guide to RAG',
                          author='AI Research Guide',
                          subject='Retrieval-Augmented Generation')

    story = []

    # ── Cover Page ────────────────────────────────────────────────────────────
    story.append(NextPageTemplate('Cover'))
    story.append(PageBreak())          # triggers cover template

    # ── Switch to content ─────────────────────────────────────────────────────
    story.append(NextPageTemplate('Content'))
    story.append(PageBreak())

    # ── TOC ───────────────────────────────────────────────────────────────────
    story += build_toc(S)

    # ── Read markdown ─────────────────────────────────────────────────────────
    md_path = 'Rag/rag_guide_part1.md'
    md_path2 = 'Rag/rag_guide_part2.md'

    for path in [md_path, md_path2]:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Remove the top-level title from part1 (already on cover)
        if path == md_path:
            content = re.sub(r'^# The Complete Guide.*?\n.*?\n', '', content, flags=re.MULTILINE)
        story += parse_md(content, S)

    print(f'Building PDF with {len(story)} story elements...')
    doc.build(story)
    print(f'Done! → {OUT}')
    return OUT


if __name__ == '__main__':
    build_book()