from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "東區"
data = [("香蕉", "蘋果", "西瓜"),
        (1, 3, 2),
        (4, 5, 6),
        (6, 5, 4)
        ]
for i in data:
    ws.append(i) 

wb.save("Excel水果資料.xlsx")   
wb.close()
