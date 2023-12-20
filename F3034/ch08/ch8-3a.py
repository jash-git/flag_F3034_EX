import docx
from docx.shared import RGBColor
from docx.shared import Pt 
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = docx.Document("Python散發套件.docx")
for para in doc.paragraphs:
    if para.style.name.startswith("Heading"):
        para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in para.runs:
            run.font.color.rgb = RGBColor(255, 0, 255)
            run.font.name = "細明體"
            run.font.size = Pt(28)
            print(run.text)
doc.save("Python散發套件3.docx")
