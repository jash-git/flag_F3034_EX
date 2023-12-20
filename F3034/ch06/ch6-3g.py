from openpyxl import load_workbook

wb = load_workbook("水果全區2.xlsx")
ws = wb["東區"]
wb.move_sheet(ws, offset = -1)
wb.save("水果全區3.xlsx")
wb.close()
