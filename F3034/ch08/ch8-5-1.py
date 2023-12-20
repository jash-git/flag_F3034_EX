from docxtpl import DocxTemplate

tpl = DocxTemplate("Word模版範例.docx")

context = { "name" : "陳會安",
            "book" : "Python X Excel 自動化"  }

tpl.render(context)
tpl.save("輸出產生Wrod文件.docx")
