import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("HOU_players_stats_2017_18.csv")
df["位置"] = df["Pos"]
df_grouped = df.groupby("位置")
points = df_grouped["PTS/G"].mean()
rebounds = df_grouped["TRB"].mean()
data = pd.DataFrame()
data["得分"] = points
data["籃板"] = rebounds
# 繪出長條圖
print(points)
points.plot.bar()
plt.title("得分")
print(data)
data.plot.bar()
plt.title("得分與籃板")
plt.show()
