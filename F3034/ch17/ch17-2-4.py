import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Kobe_stats.csv")
data = pd.DataFrame()
data["Season"] = pd.to_datetime(df["Season"])
data["PTS"] = df["PTS"]

sns.set()
sns.lineplot(x=data["Season"], y=data["PTS"])
plt.show()

