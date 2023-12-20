import pandas as pd

# 匯入Excel檔案
df = pd.read_excel("products.xlsx")
print(df)
df.to_html("ch13-2-3a.html")