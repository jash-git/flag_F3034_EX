import pandas as pd

df = pd.read_csv("missing-data.csv")
# 填補遺失資料
df1 = df.fillna(value=1)
print(df1)
df1.to_html("ch16-4-1c-01.html")

df["COL_B"] = df["COL_B"].fillna(df["COL_B"].mean())
print(df)
df.to_html("ch16-4-1c-02.html")

df["COL_C"] = df["COL_C"].fillna(df["COL_C"].median())
print(df)
df.to_html("ch16-4-1c-03.html")
