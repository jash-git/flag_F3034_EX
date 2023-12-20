from openpyxl import load_workbook

wb = load_workbook("水果資料.xlsx")
ws = wb["東區"]
ws.append([4, 5, 6])
ws.append([6, 5, 4])
wb.save("水果資料3.xlsx")   
wb.close()
