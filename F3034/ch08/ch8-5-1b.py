from docxtpl import DocxTemplate

tpl = DocxTemplate("Word表格模版範例.docx")

context = { 
       "table":[
                { "author" : "陳會安",
                  "date" : "2022-07-30",
                  "version" : "1.0",
                  "book" : "Python" }, 
                { "author" : "江小魚",
                  "date" : "2022-06-30",
                  "version" : "1.2",
                  "book" : "Excel"  } 
               ]
          }

tpl.render(context)
tpl.save("輸出產生Wrod文件3.docx")
