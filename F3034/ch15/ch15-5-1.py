import pandas as pd

df = pd.read_csv("products3.csv", encoding="utf8")
df.index = ["A","B","C","D","E","F","G","H","I"]
df.columns = ["type", "name", "price"]

print(df)
df.to_html("ch13-5-1-01.html")

print(df.groupby("type").sum())
df.groupby("type").sum().to_html("ch13-5-1-02.html")
print(df.groupby(["type","name"]).mean())
df.groupby(["type","name"]).mean().to_html("ch13-5-1-03.html")