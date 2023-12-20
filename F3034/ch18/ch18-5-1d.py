import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 匯入CSV格式的檔案
df = pd.read_csv("tutsplus2.csv", encoding="utf8")

df["date"] = df["date"].str[0:7] 
df["date"] = pd.to_datetime(df["date"])
df2 = df.groupby("date").count()

df2["title"].plot(kind="line")
plt.title("各月份新增的教學文件數")
plt.xlabel("日期")
plt.ylabel("文件數")
plt.show()