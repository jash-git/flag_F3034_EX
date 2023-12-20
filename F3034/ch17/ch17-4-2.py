import plotly.express as px
from plotly.offline import plot

# 台灣的人口資料
df = px.data.gapminder()
df_tw = df.query("country == 'Taiwan'")
# 繪製長條圖(一)
fig = px.bar(df_tw, x="year", y="pop")

plot(fig)