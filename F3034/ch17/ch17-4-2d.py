import plotly.express as px
from plotly.offline import plot

df = px.data.gapminder()
df_2007 = df.query("year == 2007")
# 繪製泡泡圖
fig = px.scatter(df_2007, x="gdpPercap", y="lifeExp",
                 color="continent",
                 size="pop", 
                 size_max=60,
                 hover_name="country")

plot(fig)