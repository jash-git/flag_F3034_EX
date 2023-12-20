import pandas as pd

# 匯入CSV格式的檔案
df = pd.read_csv("products.csv", encoding="utf8")
print(df)
df.to_html("ch13-2-2a-01.html")
# 匯入JSON格式的檔案
df2 = pd.read_json("products.json")
print(df2)
df.to_html("ch13-2-2a-02.html")