import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 匯入CSV格式的檔案
df = pd.read_csv("tutsplus.csv", encoding="utf8")

print(df["category"].value_counts().head(10))

df["category"].value_counts().head(10).plot(kind="barh")
plt.title("前10大分類的教學文件數")
plt.show()
