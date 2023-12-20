from openpyxl import load_workbook
from openpyxl.formatting.rule import ColorScaleRule

wb = load_workbook("2330TW.xlsx")
ws = wb.active

colorScale_rule = ColorScaleRule(
                        start_type="num",
                        start_value=13093208,
                        start_color="00FF0000",  # Red
                        mid_type="num",
                        mid_value=27600844,
                        mid_color="00FFFF00",  # Yellow
                        end_type="num",
                        end_value=41235817,
                        end_color="0000FF00")  # Green

ws.conditional_formatting.add("G2:G19", colorScale_rule)
wb.save("ColorScale2.xlsx")
wb.close()