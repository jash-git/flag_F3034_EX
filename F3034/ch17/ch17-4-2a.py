import plotly.express as px
from plotly.offline import plot

df = px.data.gapminder()
df_tw = df.query("country == 'Taiwan'")
# 繪製長條圖(二)
fig = px.bar(df_tw, x="year", y="pop", 
             color="lifeExp", 
             labels={"pop": "台灣人口",
                     "year": "年",
                     "lifeExp": "預期壽命"},
             height=400)

plot(fig)