import plotly.express as px
from plotly.offline import plot

df = px.data.gapminder()
df_2007 = df.query("year == 2007")
# 繪製散佈圖(一)
fig = px.scatter(df_2007, x="gdpPercap", y="lifeExp",
                 height=400)

plot(fig)