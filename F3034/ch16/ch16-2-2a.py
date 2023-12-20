import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("NBA_salary_rankings_2018.csv")
# 繪出直方圖
num_bins = 15
plt.hist(df["salary"], num_bins)
plt.ylabel("頻率")
plt.xlabel("薪水")
plt.title("NBA年薪前100位球員的直方圖") 
plt.show()
