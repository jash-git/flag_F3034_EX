from openpyxl import load_workbook

wb = load_workbook("水果3.xlsx")
ws = wb.active
ws.title = "北區"
wb.save("水果全區.xlsx")
wb.close()

