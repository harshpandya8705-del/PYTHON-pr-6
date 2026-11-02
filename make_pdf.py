from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, PageBreak, Table, TableStyle

styles = getSampleStyleSheet()
title = ParagraphStyle("t", parent=styles["Title"], fontSize=22, spaceAfter=6)
sub = ParagraphStyle("s", parent=styles["Normal"], alignment=1, textColor=colors.grey, spaceAfter=14)
h1 = ParagraphStyle("h1", parent=styles["Heading1"], fontSize=15, spaceBefore=10, spaceAfter=6)
body = ParagraphStyle("b", parent=styles["Normal"], fontSize=10.5, leading=15, spaceAfter=8)
code = ParagraphStyle("c", fontName="Courier", fontSize=8.8, leading=11.5,
                      textColor=colors.HexColor("#E6E6E6"), backColor=colors.HexColor("#1E1E1E"),
                      leftIndent=6, rightIndent=6, borderPadding=(6, 6, 6, 6))

line_style = ParagraphStyle("l", fontName="Courier", fontSize=8.8, leading=11.5, textColor=colors.HexColor("#E6E6E6"))
def block(text):
    rows = [[Preformatted(l, line_style) if l.strip() else Spacer(1, 11.5)] for l in text.rstrip("\n").split("\n")]
    t = Table(rows, colWidths=[A4[0] - 36*mm], splitByRow=1)
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#1E1E1E")),
                           ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10)]))
    return t

raw = open("output.txt").read()
sessions = [s for s in raw.split("##### ") if s.strip()]
story = [Paragraph("File Operator", title),
         Paragraph("Personal Journal Manager - Project Output", sub),
         Paragraph("Overview", h1),
         Paragraph("This document shows the console output of the Personal Journal Manager, a Python program "
                   "built with an object-oriented <b>JournalManager</b> class. It stores timestamped entries in "
                   "<b>journal.txt</b>, supports add, view, search and delete operations, and handles file "
                   "errors gracefully with exception handling.", body)]

for i, s in enumerate(sessions, 1):
    head, _, text = s.partition("\n")
    story.append(Paragraph(head, h1))
    story.append(block(text.strip("\n")))
    story.append(Spacer(1, 8))

story.append(PageBreak())
story.append(Paragraph("File Handling Modes Demonstration (file_modes_demo.py)", h1))
story.append(Paragraph("Output showing how modes <b>x</b>, <b>a</b>, <b>r</b> and <b>w</b> behave.", body))
story.append(block(open("modes_output.txt").read()))
story.append(Spacer(1, 12))
story.append(Paragraph("Scenarios Covered", h1))
for line in ["Welcome menu and exit message",
             "Add a new entry (file created automatically with timestamp)",
             "View all entries, including the file-not-found case",
             "Search by keyword: match found and no match",
             "Delete all entries with yes/no confirmation",
             "Invalid menu option handling"]:
    story.append(Paragraph("&bull; " + line, body))

def footer(c, d):
    c.setFont("Helvetica", 8); c.setFillColor(colors.grey)
    c.drawCentredString(A4[0]/2, 10*mm, f"Personal Journal Manager - Project Output - Page {d.page}")

SimpleDocTemplate("Project_Output.pdf", pagesize=A4, leftMargin=18*mm, rightMargin=18*mm,
                  topMargin=18*mm, bottomMargin=20*mm,
                  title="Personal Journal Manager - Project Output").build(story, onFirstPage=footer, onLaterPages=footer)
