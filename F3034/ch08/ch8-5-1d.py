from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm

doc = DocxTemplate("Word圖片模版範例.docx")

img = InlineImage(doc, "koala.png", Cm(5))
context = { "name": "陳會安",
            "image": img }

doc.render(context)
doc.save("輸出產生Wrod文件5.docx")
