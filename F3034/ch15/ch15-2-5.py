import pandas as pd

df = pd.read_csv("products.csv", encoding="utf8")

df2 = df.set_index("分類")
print(df2.head())
df2.head().to_html("ch13-2-5-01.html")

df3 = df2.reset_index()
print(df3.head())
df3.head().to_html("ch13-2-5-02.html")

