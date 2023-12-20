import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("NBA_players_salary_stats_2018.csv")
# 繪製散佈圖
df.plot.scatter(x="PTS", y="salary", 
        title="NBA球員的薪水和得分的散佈圖")
plt.ylabel("薪水")
plt.xlabel("得分")
plt.show()