from openpyxl import load_workbook
from openpyxl.formatting.rule import ColorScaleRule

wb = load_workbook("2330TW.xlsx")
ws = wb.active

colorScale_rule = ColorScaleRule(
                        start_type="min",
                        start_color="00FF0000",  # Red
                        end_type="max",
                        end_color="0000FF00")  # Green

ws.conditional_formatting.add("G2:G19", colorScale_rule)
wb.save("ColorScale.xlsx")
wb.close()
