import plotly.express as px
from plotly.offline import plot
import pandas as pd

# 匯入CSV格式的檔案
df = pd.read_csv("tech_stocks_2017.csv", encoding="utf8")

fig = px.scatter(df, x='Close', y='Volume', 
                 color="Name",
                 title="蘋概科技股的收盤價與成交量",
                 labels = {"Close": "2017年收盤價",
                           "Volume": "2017年成交量" },
                 hover_data=['Close', 'Volume'])
plot(fig)

