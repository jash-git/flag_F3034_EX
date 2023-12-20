import pandas as pd
import dateparser

# 匯入CSV格式的檔案
df = pd.read_csv("tutsplus.csv", encoding="utf8")

def parse_date(value):
    return dateparser.parse(value,
                            settings={'TIMEZONE': 'UTC'})

df["date"] = df["date"].apply(parse_date)
df.to_csv("tutsplus2.csv", index=False, encoding="utf8")
print("存入tutsplus2.csv")
