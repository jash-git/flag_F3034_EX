import plotly.express as px
from plotly.offline import plot

df = px.data.tips()
# 繪製箱型圖
fig = px.box(df, x="day", y="total_bill")

plot(fig)