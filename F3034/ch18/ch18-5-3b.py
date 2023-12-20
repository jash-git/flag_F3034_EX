import plotly.express as px
from plotly.offline import plot
import pandas as pd

# 匯入CSV格式的檔案
df = pd.read_csv("stocks\\2330.TW.csv", encoding="utf8")
df = df.dropna()
df["Date"] = pd.to_datetime(df["Date"])

fig = px.line(df, x="Date", y="Close",
              title="台積電2017年的每日收盤價",
              labels = {"Date": "2017年",
                        "Close": "收盤價" })
plot(fig)
