import json
from turtle import right
from fpdf import FPDF

with open ("infos.json","r") as f:
    resume= json.loads(f.read())


pdf= FPDF()
pdf.add_page()
pdf.set_auto_page_break

pdf.set_font("Arial", "B", size= 17)
pdf.set_text_color(5, 29, 82)
pdf.cell(200, 2, txt = resume["informations"][0]["FullName"], ln=1)

pdf.set_font("Arial","", size= 15)
pdf.set_text_color(0, 0, 0)
pdf.cell(200, 9, txt = resume["informations"][0]["Address"], ln=1)
pdf.cell(200, 3, txt = resume["informations"][0]["ContactNumber"], ln=1)

pdf.cell(200, 17, txt = "Schools Attended:", ln=1)
pdf.cell(138, 9, txt = resume["informations"][0]["SchoolsAttended1"], ln=1, align="R")
pdf.cell(138.5, 4, txt = resume["informations"][0]["SchoolsAttended2"], ln=1, align="R")
pdf.cell(142, 9, txt = resume["informations"][0]["SchoolsAttended3"], ln=1, align="R")
pdf.set_text_color(250, 149, 7)
pdf.cell(135, 3, txt = resume["informations"][0]["SchoolsAttended3a"], ln=1, align="R")
pdf.set_text_color(0, 0, 0)
pdf.cell(182.5, 7, txt = resume["informations"][0]["SchoolsAttended4"], ln=1, align="R")
pdf.set_text_color(250, 149, 7)
pdf.cell(110, 7, txt = resume["informations"][0]["SchoolsAttended4a"], ln=1, align="R")
pdf.set_text_color(0, 0, 0)
pdf.cell(157, 7, txt = resume["informations"][0]["SchoolsAttended5"], ln=1, align="R")
pdf.set_text_color(250, 149, 7)
pdf.cell(130, 7, txt = resume["informations"][0]["SchoolsAttended5a"], ln=1, align="R")

pdf.set_text_color(0, 0, 0)
pdf.cell(200, 19, txt = resume["informations"][0]["Experiences"], ln=1)

pdf.cell(200, 17, txt = "Achievements:", ln=1)
pdf.set_text_color(250, 149, 7)
pdf.cell(70, .2, txt = resume["informations"][0]["Achievements1"], ln=1, align="R")
pdf.cell(122.5, 9, txt = resume["informations"][0]["Achievements2"], ln=1, align="R")
pdf.cell(112.1, .2, txt = resume["informations"][0]["Achievements3"], ln=1, align="R")

pdf.set_text_color(0, 0, 0)
pdf.cell(112.1, 30, txt = resume["informations"][0]["Summary"], ln=1)
pdf.cell(112.1, 0.1, txt = resume["informations"][0]["SummaryA"], ln=1)

pdf.cell(112.1, 40, txt = resume["informations"][0]["Objective"], ln=1)
pdf.cell(112.1, 0.001, txt = resume["informations"][0]["ObjectiveA"], ln=1)

pdf.image('picture.png', x=160, y=9, w=45, h=45, type= "", link= "")






pdf.output("test.pdf")