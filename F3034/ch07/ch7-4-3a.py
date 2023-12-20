import pandas as pd

df = pd.read_excel("收支流水帳清單.xlsx",
                        engine="openpyxl")

pivot_products = df.pivot_table(index=["項目","月份"],                  
                                values="金額",
                                aggfunc="sum")
print(pivot_products)
pivot_products.to_excel("收支流水帳樞紐分析表2.xlsx",
                        engine="openpyxl")