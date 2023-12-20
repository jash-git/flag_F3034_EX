from openpyxl import load_workbook

wb = load_workbook("營業額.xlsx")
ws = wb.active
for row in ws.rows:
    for cell in row:
        print(cell.value, end=" ")
    print()    
wb.close()
