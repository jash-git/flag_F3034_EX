from openpyxl import load_workbook

wb = load_workbook("水果資料.xlsx")
ws = wb["東區"]
ws.append([4])
ws.append([5])
ws.append([6])
wb.save("水果資料2.xlsx")   
wb.close()
