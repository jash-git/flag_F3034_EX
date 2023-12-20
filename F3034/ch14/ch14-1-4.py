from openpyxl import load_workbook
from openpyxl.formatting.rule import DataBarRule

wb = load_workbook("2330TW.xlsx")
ws = wb.active

dataBar_rule = DataBarRule(start_type="num",
                           start_value=13093208,
                           end_type="num",
                           end_value=48791728,
                           color="0000FF00")  # Green
ws.conditional_formatting.add("G2:G19", dataBar_rule)
wb.save("DataBar.xlsx")
wb.close()
