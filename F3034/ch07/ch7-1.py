from openpyxl import load_workbook

wb = load_workbook("營業額.xlsx")
ws = wb.active
print("工作表尺寸:", ws.dimensions)

ws.auto_filter.ref = "A1:D7"
ws.auto_filter.add_filter_column(2, ["USA", "China"])
ws.auto_filter.add_sort_condition("D2:D7")
wb.save("營業額_Filters.xlsx") 
wb.close()
