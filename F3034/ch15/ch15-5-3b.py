import pandas as pd

df = pd.read_csv("products3.csv", encoding="utf8")
df.index = ["A","B","C","D","E","F","G","H","I"]
df.columns = ["type", "name", "price"]

df["name_length"] = df.name.apply(len)
def inc(value):
    return value + 1
df["price2"] = df.price.apply(inc)
print(df.head())
df.head().to_html("ch13-5-3b.html")