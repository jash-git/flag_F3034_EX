import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("NBA_salary_rankings_2018.csv")
df["位置"] = df.pos
df.boxplot(column="salary",
           by="位置",
           figsize=(6,5))

plt.xticks(rotation=25)
plt.title("NBA前100名依位置年薪分佈的箱形圖")
plt.suptitle('')
plt.show()