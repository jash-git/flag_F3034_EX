from docxtpl import DocxTemplate, RichText

tpl = DocxTemplate("Word表格模版範例2.docx")

context = { 
       "table":[
                { "author" : RichText("陳會安", color='FF0000',
                                      bold=True, size=32),
                  "date" : "2022-07-30",
                  "version" : "1.0",
                  "book" : "Python",
                  "bg" : "FFDD00" }, 
                { "author" : RichText("江小魚", color='00FF00',
                                      italic=True, size=32),
                  "date" : "2022-06-30",
                  "version" : "1.2",
                  "book":"Excel",
                  "bg" : "8888FF" } 
               ]
          }

tpl.render(context)
tpl.save("輸出產生Wrod文件4.docx")
