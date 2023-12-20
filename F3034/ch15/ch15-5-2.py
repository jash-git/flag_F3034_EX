import pandas as pd

df = pd.read_csv("products3.csv", encoding="utf8")

df.columns = ["type", "name", "price"]
ordinals = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
df.index = ordinals

# 呼叫 pivot_table() 方法
pivot_products = df.pivot_table(index="type",
                                columns="name",
                                values="price",
                                aggfunc="sum")
print(pivot_products)
pivot_products.to_html("ch13-5-2.html")