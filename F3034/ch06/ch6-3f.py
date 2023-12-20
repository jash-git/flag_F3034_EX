from openpyxl import load_workbook

wb = load_workbook("水果全區.xlsx")
ws = wb["中區"]
ws_copy = wb.copy_worksheet(ws)
ws_copy.title = "東區"
wb.save("水果全區2.xlsx")
wb.close()

