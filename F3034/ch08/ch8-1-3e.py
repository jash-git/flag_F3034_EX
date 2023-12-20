import docx

doc = docx.Document("Word文件範例5.docx")
doc.add_page_break()
doc.save("Word文件範例6.docx")
