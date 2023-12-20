import pandas as pd
from openpyxl import load_workbook
 
wb = load_workbook("products.xlsx")
ws = wb.active
data = ws.values
df = pd.DataFrame(data)
print(df)
df.to_html("ch13-2-3b-01.html")
# 第一列是欄索引
data = list(ws.values)
df2 = pd.DataFrame(data[1:], columns=data[0])
print(df2)
df2.to_html("ch13-2-3b-02.html")
# 第一列是欄索引, 第一欄是列索引
idx =  [r[0] for r in data[1:]]
cols =  data[0][1:]
data = [r[1:] for r in data[1:]]
df3 = pd.DataFrame(data, index=idx, columns=cols)
print(df3)
df3.to_html("ch13-2-3b-03.html")