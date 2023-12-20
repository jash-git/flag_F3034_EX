from docxtpl import DocxTemplate

tpl = DocxTemplate("Word模版範例2.docx")

context = { 
            "username" : "hueyan",
            "list" : ["Python", "Excel", "docx-template"],
            "dict" : {
                        "name" : "陳會安",
                        "book" : "Python X Excel 自動化"
                     }
          }

tpl.render(context)
tpl.save("輸出產生Wrod文件2.docx")
