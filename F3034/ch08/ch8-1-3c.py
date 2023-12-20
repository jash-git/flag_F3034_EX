import docx

doc = docx.Document("Word文件範例3.docx")
records = (
    ("王小明", "0912-123456", 78),
    ("陳小安", "0933-234567", 66),
    ("李四誠", "0922-345678", 85) )
table = doc.add_table(rows=1, cols=3)
row = table.rows[0]
row.cells[0].text = "姓名" 
row.cells[1].text = "電話"
row.cells[2].text = "成績"
for name, tel, score in records:
    row_cells = table.add_row().cells
    row_cells[0].text = name
    row_cells[1].text = tel
    row_cells[2].text = str(score)
doc.save("Word文件範例4.docx")
 


