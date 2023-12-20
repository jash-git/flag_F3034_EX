import docx

doc = docx.Document("Python開發工具.docx")
for style in doc.styles:
    print(style.name, end=" ")

