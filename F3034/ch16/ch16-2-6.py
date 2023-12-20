import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("Kobe_stats.csv")
# 繪製折線圖
df["Season"] = pd.to_datetime(df["Season"])
df = df.set_index("Season")
#print(df)
plt.plot(df["PTS"], "r-o", label="得分")
plt.plot(df["AST"], "b-o", label="助攻")
plt.plot(df["TRB"], "g-o", label="籃板")
plt.legend()
plt.ylabel("統計資料")
plt.xlabel("球季")
plt.title("Kobe Bryant生涯球員統計資料") 
plt.show()