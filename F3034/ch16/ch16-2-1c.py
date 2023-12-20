import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("HOU_players_stats_2017_18.csv")
df_grouped = df.groupby("Pos")
points = df_grouped["PTS/G"].mean()
rebounds = df_grouped["TRB"].mean()
# 繪出長條圖
index = range(1, 11)
plt.bar(index[0::2], points, label="得分")
plt.bar(index[1::2], rebounds, label="籃板")
plt.xticks(index[0::2], points.index)
plt.legend()
plt.ylabel("得分和籃板")
plt.xlabel("位置")
plt.title("NBA休斯頓火箭隊各位置得分和籃板平均") 
plt.show()

