from openpyxl import load_workbook

wb = load_workbook("營業額.xlsx")
ws = wb['工作表1']
data = ws.values
for v in data:
    print(v)
wb.close()
