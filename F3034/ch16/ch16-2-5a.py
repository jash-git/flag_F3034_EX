import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("GSW_players_stats_2017_18.csv")
df_grouped = df.groupby("Pos")
position = df_grouped["Pos"].count()
explode = (0, 0, 0.2, 0, 0.2)
# 繪出派圖
plt.pie(position, labels=position.index,
        explode=explode)
plt.axis("equal")
plt.title("NBA金州勇士隊的球員陣容")  
plt.show()
