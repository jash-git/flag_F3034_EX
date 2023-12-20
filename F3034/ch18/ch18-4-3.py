import pandas as pd

df = pd.read_csv("categorical-data.csv")
print(df)
df.to_html("ch16-4-3-01.html")

size_mapping = {"XXL": 5,
                "XL": 4,
                "L": 3,
                "M": 2,
                "S": 1,
                "XS": 0}

df["Size"] = df["Size"].map(size_mapping)
print(df)
df.to_html("ch16-4-3-02.html")