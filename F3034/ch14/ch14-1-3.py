from openpyxl import load_workbook
from openpyxl.formatting.rule import IconSetRule

wb = load_workbook("2330TW.xlsx")
ws = wb.active

iconSet_rule = IconSetRule(icon_style="4Arrows",
                           type="num",
                           values=[10000000, 
                                   20000000,
                                   30000000,
                                   40000000])

ws.conditional_formatting.add("G2:G19", iconSet_rule)
wb.save("IconSet.xlsx")
wb.close()
