from openpyxl import load_workbook

wb = load_workbook("營業額.xlsx")
ws = wb.active
for column in ws.columns:
    for cell in column:
        print(cell.value, end=" ")
    print()    
wb.close()
