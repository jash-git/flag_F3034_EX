import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("Kobe_stats.csv")
# 繪製折線圖
data = pd.DataFrame()
data["球季"] = pd.to_datetime(df["Season"])
data["得分"] = df["PTS"]
data["助攻"] = df["AST"]
data["籃板"] = df["TRB"]
data = data.set_index("球季")

data.plot(kind="line")
plt.title("Kobe Bryant生涯球員統計資料")
plt.show()
