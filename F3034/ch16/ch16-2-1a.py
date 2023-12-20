import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("GSW_players_stats_2017_18.csv")
df_grouped = df.groupby("Pos")
position = df_grouped["Pos"].count()
# 繪出長條圖
plt.barh([1, 2, 3, 4, 5], position)
plt.xticks([1, 2, 3, 4, 5], position.index)
plt.ylabel("人數")
plt.xlabel("位置")
plt.title("NBA金州勇士隊的球員陣容") 
plt.show()


