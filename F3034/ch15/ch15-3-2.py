import pandas as pd

df = pd.read_csv("products.csv", encoding="utf8")

df.columns = ["type", "name", "price"]
ordinals = ["A", "B", "C", "D", "E", "F"]
df.index = ordinals

print(df[df.price > 20])
df[df.price > 20].to_html("ch13-3-2-01.html")

print(df.query("price > 20"))
df.query("price > 20").to_html("ch13-3-2-02.html")

print(df[df["type"].isin(["科技","居家"])])
df[df["type"].isin(["科技","居家"])].to_html("ch13-3-2-03.html")
