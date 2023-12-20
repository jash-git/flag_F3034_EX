import pandas as pd

# 匯入CSV格式的檔案
df = pd.read_csv("products.csv", index_col=0, encoding="utf8")
print(df)
df.to_html("ch13-2-2b.html")
