import plotly.express as px
from plotly.offline import plot
import pandas as pd

# 匯入CSV格式的檔案
df = pd.read_csv("stock_price.csv", encoding="utf8")
df["Date"] = pd.to_datetime(df["Date"])

fig = px.line(df, x="Date", y="Close",
              markers=True,
              title="2022年的5日收盤價",
              labels = {"Date": "2022年",
                        "Close": "收盤價" },
              hover_data=["Open","High","Low","Close"])
plot(fig)
