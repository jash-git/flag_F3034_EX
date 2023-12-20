import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

df = pd.read_csv("products.csv", encoding="utf8")
print(df)
wb = Workbook()
ws = wb.active
for r in dataframe_to_rows(df, index=False, header=True):
    ws.append(r)

wb.save("products_openpyxl.xlsx")
