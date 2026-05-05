
"""Build a beautiful PDF book from VS Code markdown details."""
import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, PageBreak, HRFlowable, NextPageTemplate
)
from reportlab.platypus.flowables import Flowable

PAGE_W, PAGE_H = A4
ML, MR, MT, MB = 22*mm, 22*mm, 28*mm, 22*mm
CW = PAGE_W - ML - MR

P = {
    'cover':        HexColor('#0B1120'),
    'primary':      HexColor('#3B6FE8'),
    'primary_l':    HexColor('#EEF2FF'),
    'heading':      HexColor('#1E293B'),
    'sub':          HexColor('#334155'),
    'text':         HexColor('#3D4E65'),
    'code_bg':      HexColor('#F1F5F9'),
    'tip_bg':       HexColor('#F0FDF4'),
    'tbl_hdr':      HexColor('#3B6FE8'),
    'tbl_even':     HexColor('#F8FAFC'),
    'tbl_odd':      HexColor('#FFFFFF'),
    'border':       HexColor('#E2E8F0'),
    'rule':         HexColor('#CBD5E1'),
    'sec_accent':   HexColor('#6366F1'),
}

class SectionDivider(Flowable):
    def __init__(self, number, title):
        Flowable.__init__(self)
        self.number = number
        self.title = title
        self.width = CW
        self.height = 80*mm

    def wrap(self, aw, ah):
        return CW, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.setFillColor(P['primary_l'])
        c.roundRect(0, 0, w, h, 6, fill=1)
        c.setFillColor(P['primary'])
        c.rect(0, 0, 5, h, fill=1)
        c.setFont('Helvetica-Bold', 96)
        c.drawString(w - 60*mm, 10, self.number)
        c.setFont('Helvetica-Bold', 9)
        c.setFillColor(P['primary'])
        c.drawString(14, h - 18, 'S E C T I O N')
        c.setFont('Helvetica-Bold', 24)
        c.setFillColor(P['heading'])
        if len(self.title) > 32:
            words = self.title.split()
            mid = len(words)//2
            c.drawString(14, h - 44, ' '.join(words[:mid]))
            c.drawString(14, h - 64, ' '.join(words[mid:]))
        else:
            c.drawString(14, h - 44, self.title)

class CodeBox(Flowable):
    def __init__(self, lines):
        Flowable.__init__(self)
        self.lines = lines
        self.pad = 10
        self.fs = 7.8
        self.lh = 10.5

    def wrap(self, aw, ah):
        self.width = aw
        self.height = len(self.lines) * self.lh + self.pad * 2 + 20
        return self.width, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.setFillColor(HexColor('#E2E8F0'))
        c.roundRect(2, -2, w, h, 5, fill=1)
        c.setFillColor(P['code_bg'])
        c.roundRect(0, 0, w, h, 5, fill=1)
        c.setStrokeColor(P['text'])
        c.setLineWidth(0.6)
        c.roundRect(0, 0, w, h, 5, fill=0)
        c.setFillColor(P['sub'])
        for i, col in enumerate([HexColor('#FC6058'), HexColor('#FEC02F'), HexColor('#2ACA44')]):
            c.setFillColor(col)
            c.circle(self.pad + i*12, h - 8, 3.5)
        c.setFont('Courier', self.fs)
        c.setFillColor(P['heading'])
        start_y = h - self.pad - self.fs
        for line in self.lines:
            c.drawString(self.pad, start_y, line.rstrip())
            start_y -= self.lh
            if start_y < self.pad:
                break

class Callout(Flowable):
    CONFIGS = {
        'tip':       ('#F0FDF4', '#16A34A', '#166534', 'PRO TIP'),
        'mistake':   ('#FEF2F2', '#DC2626', '#991B1B', 'COMMON MISTAKE'),
    }

    def __init__(self, lines, kind='tip'):
        Flowable.__init__(self)
        self.lines = lines
        self.kind = kind
        cfg = self.CONFIGS.get(kind, self.CONFIGS['tip'])
        self.bg, self.bd, self.tc = HexColor(cfg[0]), HexColor(cfg[1]), HexColor(cfg[2])
        self.label = cfg[3]
        self.height = len(lines) * 13 + 20

    def wrap(self, aw, ah):
        return CW, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height if hasattr(self, 'width') else CW
        c.setFillColor(self.bg)
        c.roundRect(0, 0, w, h, 5, fill=1)
        c.setFillColor(self.bd)
        c.roundRect(0, 0, 5, h, 2, fill=1)
        c.setFont('Helvetica-Bold', 7.5)
        c.setFillColor(self.bd)
        c.drawString(14, h - 14, self.label)
        c.setStrokeColor(self.bd)
        c.setLineWidth(0.3)
        c.line(14, h - 17, w - 10, h - 17)
        c.setFont('Helvetica', 9.5)
        c.setFillColor(self.tc)
        y = h - 18
        for line in self.lines:
            c.drawString(14, y, line)
            y -= 13

class HRule(Flowable):
    def __init__(self, color=None, thickness=0.5):
        Flowable.__init__(self)
        self.color = color or P['rule']
        self.thickness = thickness

    def wrap(self, aw, ah):
        return aw, 1

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 0, self.width, 0)

def cover_canvas(cv, doc):
    cv.saveState()
    cv.setFillColor(P['cover'])
    cv.rect(0, 0, PAGE_W, PAGE_H, fill=1)
    cv.setFillColor(HexColor('#0E1F45'))
    cv.setFont('Helvetica-Bold', 200)
    cv.drawString(10*mm, PAGE_H/2 - 70*mm, 'BEAM')
    cv.setFillColor(HexColor('#93C5FD'))
    cv.setFont('Helvetica-Bold', 44)
    cv.drawString(ML, PAGE_H - 128*mm, 'Internals Guide')
    cv.restoreState()

def content_canvas(cv, doc):
    cv.saveState()
    cv.setStrokeColor(P['primary'])
    cv.setLineWidth(2)
    cv.line(ML, PAGE_H - 16*mm, PAGE_W - MR, PAGE_H - 16*mm)
    cv.setFont('Helvetica', 7.5)
    cv.setFillColor(HexColor('#94A3B8'))
    cv.drawString(ML, PAGE_H - 13*mm, 'Beam Codebase - Internal Wiki')
    cv.restoreState()

def make_styles():
    S = {}
    S['body'] = ParagraphStyle('body', fontName='Helvetica', fontSize=10.5,
        leading=17, textColor=P['text'], alignment=TA_JUSTIFY, spaceAfter=6)
    S['h1'] = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=22,
        leading=28, textColor=P['primary'], spaceAfter=10)
    S['h2'] = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=16,
        leading=22, textColor=P['heading'], spaceBefore=16, spaceAfter=5)
    S['h3'] = ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=13,
        leading=18, textColor=P['sub'], spaceAfter=4)
    S['toc_title'] = ParagraphStyle('toc_title', fontName='Helvetica-Bold',
        fontSize=26, leading=32, textColor=P['heading'], spaceAfter=20)
    return S

def fmt(text):
    if not isinstance(text, str): return ''
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def render_table(rows):
    pass

def build_toc(S):
    story = []
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph('Table of Contents', S['toc_title']))
    for i in range(1, 13):
        section = f"Section {i}"
        story.append(Paragraph(section, S['h2']))
    story.append(PageBreak())
    return story

def parse_md(text, S):
    story = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        h1 = re.match(r'^# (.+)', line)
        h2 = re.match(r'^## (.+)', line)
        if h1:
            story.append(SectionDivider(str(1), h1.group(1)))
        elif h2:
            story.append(Paragraph(fmt(h2.group(1)), S['h2']))
        elif line.strip() and not line.startswith('```'):
            story.append(Paragraph(fmt(line), S['body']))
        i += 1
    return story

def build_book():
    OUT = 'Books/Beam_Internal_Wiki.pdf'
    S = make_styles()

    cover_frame = Frame(0, 0, PAGE_W, PAGE_H)
    content_frame = Frame(ML, MB, CW, PAGE_H - MT - MB)

    cover_tpl = PageTemplate(id='Cover', frames=[cover_frame], onPage=cover_canvas)
    content_tpl = PageTemplate(id='Content', frames=[content_frame], onPage=content_canvas)

    doc = BaseDocTemplate(OUT, pagesize=A4, pageTemplates=[cover_tpl, content_tpl])
    story = []
    story.append(NextPageTemplate('Cover'))
    story.append(PageBreak())
    story.append(NextPageTemplate('Content'))
    story.append(PageBreak())
    story += build_toc(S)
    with open('vsCodeDetails.md', 'r') as f:
        content = f.read()
    story += parse_md(content, S)
    doc.build(story)
    print(f'Book created at {OUT}')
    return OUT

if __name__ == '__main__':
    build_book()

