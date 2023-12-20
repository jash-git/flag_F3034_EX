from openpyxl import load_workbook

wb = load_workbook("營業額.xlsx")
ws = wb.active

ws.freeze_panes = "C2"
wb.save("營業額_Fozen.xlsx") 
wb.close()
