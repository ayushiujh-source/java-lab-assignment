from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, PageBreak, KeepTogether
from reportlab.lib import colors
import re, textwrap

ROOT=Path(".")
OUT=ROOT/"Java_Lab_File_Ayushi.pdf"
try:
    mono=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",16)
    small=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",13)
    bold=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",17)
except OSError:
    mono=small=bold=ImageFont.load_default()

def code_screenshot(source, target):
    raw=source.splitlines()
    lines=[]
    for line in raw:
        if len(line)>104:
            # wrap long source lines at whitespace when possible, otherwise split safely
            chunks=textwrap.wrap(line,width=104,subsequent_indent="    ",break_long_words=True,break_on_hyphens=False)
            lines.extend(chunks or [""])
        else:
            lines.append(line)
    line_h=23
    height=max(180,92+len(lines)*line_h)
    width=1540
    im=Image.new("RGB",(width,height),(30,32,36)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((12,12,width-12,height-12),radius=12,fill=(36,39,45),outline=(65,70,80),width=2)
    d.ellipse((30,28,44,42),fill=(255,95,86)); d.ellipse((54,28,68,42),fill=(255,190,60)); d.ellipse((78,28,92,42),fill=(40,200,90))
    d.text((120,25),"Main.java   |   IDE-style code view",font=bold,fill=(205,210,220))
    d.line((25,65,width-25,65),fill=(75,80,90),width=1)
    y=82
    for n,line in enumerate(lines,1):
        d.text((30,y),str(n).rjust(3),font=small,fill=(115,125,140))
        d.text((85,y),line,font=mono,fill=(225,228,235))
        y+=line_h
    im.save(target)

def page_footer(canvas,doc):
    canvas.saveState()
    canvas.setFont("Helvetica",8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(36,22,"BCS351 • Introduction to Programming Using Java Lab")
    canvas.drawRightString(A4[0]-36,22,f"Page {doc.page}")
    canvas.restoreState()

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle",parent=styles["Title"],fontName="Helvetica-Bold",fontSize=23,leading=29,alignment=TA_CENTER,textColor=colors.HexColor("#183153"),spaceAfter=18))
styles.add(ParagraphStyle(name="CoverSub",parent=styles["Normal"],fontSize=12,leading=18,alignment=TA_CENTER))
styles.add(ParagraphStyle(name="AHead",parent=styles["Heading1"],fontSize=17,leading=21,textColor=colors.HexColor("#183153"),spaceAfter=6))
styles.add(ParagraphStyle(name="QHead",parent=styles["Heading2"],fontSize=12,leading=15,textColor=colors.HexColor("#27364b"),spaceAfter=5))
styles.add(ParagraphStyle(name="BodySmall",parent=styles["BodyText"],fontSize=9,leading=13))
doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=36,leftMargin=36,topMargin=36,bottomMargin=38)
story=[]
story += [Spacer(1,1.1*inch),Paragraph("INVERTIS UNIVERSITY, BAREILLY",styles["CoverTitle"]),Paragraph("B.Tech CSE • Second Year",styles["CoverSub"]),Spacer(1,0.25*inch),Paragraph("INTRODUCTION TO PROGRAMMING<br/>USING JAVA LAB",styles["CoverTitle"]),Paragraph("BCS351 • Complete Lab File",styles["CoverSub"]),Spacer(1,0.55*inch),Paragraph("<b>Submitted by:</b> Ayushi",styles["CoverSub"]),Paragraph("<b>Roll Number:</b> BCS2025414",styles["CoverSub"]),Spacer(1,0.25*inch),Paragraph("Assignments 1–15",styles["CoverSub"]),PageBreak()]
story += [Paragraph("Submission note",styles["AHead"]),Paragraph("This soft-copy file contains the Java source code and corresponding program output for every question in the supplied BCS351 lab-assignment sheet. The programs use fixed sample values from the assignment; no task in the supplied sheet requires console input, so separate input screenshots are not applicable.",styles["BodySmall"]),Spacer(1,8),Paragraph("The code panels are clean IDE-style renderings of the submitted Main.java source files, rather than photographs captured from a live IDE. Output panels show the generated output for each program.",styles["BodySmall"]),PageBreak()]
for anum in range(1,16):
    folder=ROOT/f"Assignment{anum}"
    readme=(folder/"README.md").read_text(encoding="utf-8") if (folder/"README.md").exists() else ""
    title_match=re.search(r"^# Assignment \d+:\s*(.+)$",readme,re.M)
    title=title_match.group(1) if title_match else f"Assignment {anum}"
    aim_match=re.search(r"^## 2\. Aim\s*\n(.+)$",readme,re.M)
    aim=aim_match.group(1).strip() if aim_match else ""
    for qdir in sorted(folder.glob("Question*"),key=lambda p:int(re.search(r"\d+",p.name).group())):
        qnum=int(re.search(r"\d+",qdir.name).group())
        java=qdir/"Main.java"; out=qdir/"output.png"
        if not java.exists() or not out.exists():
            raise RuntimeError(f"Missing source or output: {qdir}")
        src=java.read_text(encoding="utf-8")
        temp=qdir/"code_view.png"
        code_screenshot(src,temp)
        story.append(Paragraph(f"Assignment {anum}: {title}",styles["AHead"]))
        if aim: story.append(Paragraph("<b>Aim:</b> "+aim,styles["BodySmall"]))
        story.append(Spacer(1,5))
        story.append(Paragraph(f"Question {qnum}: {qdir.name}",styles["QHead"]))
        story.append(Paragraph("Code screenshot (IDE-style source view)",styles["BodySmall"]))
        im=Image.open(temp); iw,ih=im.size
        maxw=A4[0]-72; maxh=4.15*inch
        scale=min(maxw/iw,maxh/ih)
        story.append(RLImage(str(temp),width=iw*scale,height=ih*scale))
        story.append(Spacer(1,7))
        story.append(Paragraph("Input",styles["QHead"]))
        story.append(Paragraph("No runtime input required; the values are initialized in the program.",styles["BodySmall"]))
        story.append(Spacer(1,5))
        story.append(Paragraph("Output screenshot",styles["QHead"]))
        story.append(RLImage(str(out),width=7.15*inch,height=7.15*inch*300/1100))
        story.append(PageBreak())
doc.build(story,onFirstPage=page_footer,onLaterPages=page_footer)
print(f"Created {OUT} ({OUT.stat().st_size:,} bytes)")
