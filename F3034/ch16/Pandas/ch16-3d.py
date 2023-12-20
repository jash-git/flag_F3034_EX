import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("GSW_players_stats_2017_18.csv")
df["位置"] = df.Pos
df_grouped = df.groupby("位置")
position = df_grouped["位置"].count()
explode = (0, 0, 0.2, 0, 0.2)
# 繪出派圖
position.plot.pie(figsize=(6, 6),
                  explode=explode, 
              title="NBA金州勇士隊的球員陣容") 
plt.legend(position.index, loc="best")
plt.show()