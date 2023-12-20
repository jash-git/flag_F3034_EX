import pandas as pd

# 匯入CSV格式的檔案
df = pd.read_csv("stocks\\2330.TW.csv", encoding="utf8")

print(df.info())

df = df.dropna()
print(df.info())

print(df.head())
df.head().to_html("ch16-5-3.html")



