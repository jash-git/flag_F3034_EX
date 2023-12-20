import pandas as pd

df = pd.read_csv("products.csv", encoding="utf8")

df.columns = ["type", "name", "price"]
ordinals = ["A", "B", "C", "D", "E", "F"]
df.index = ordinals

print(df.tail(3))
# 新增記錄
df.loc["G"] = ["科學", "全聯超", 28.5]
print(df.tail(3))
df.tail(3).to_html("ch13-4-3.html")
