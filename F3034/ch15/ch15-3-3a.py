import pandas as pd

df = pd.read_csv("products.csv", encoding="utf8")

df.columns = ["type", "name", "price"]
ordinals = ["A", "B", "C", "D", "E", "F"]
df.index = ordinals

df2 = df.sort_values("price", ascending=False)
print(df2)
df2.to_html("ch13-3-3a-01.html")

df.sort_values(["type","price"], inplace=True)
print(df)
df.to_html("ch13-3-3a-02.html")