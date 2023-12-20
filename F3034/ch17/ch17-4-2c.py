import plotly.express as px
from plotly.offline import plot

df = px.data.gapminder()
df_2007 = df.query("year == 2007")
# 繪製散佈圖(二)
fig = px.scatter(df_2007, x="gdpPercap", y="lifeExp",
                 color="continent",
                 height=400)

plot(fig)