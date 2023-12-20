import plotly.express as px
from plotly.offline import plot

df = px.data.iris()
# 繪製直方圖
fig = px.histogram(df, x="sepal_length", y="petal_width",
                   height=400)

plot(fig)