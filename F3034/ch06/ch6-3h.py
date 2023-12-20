from openpyxl import load_workbook

wb = load_workbook("水果全區3.xlsx")
ws = wb["中區"]
wb.remove(ws)
wb.save("水果全區4.xlsx")
wb.close()
