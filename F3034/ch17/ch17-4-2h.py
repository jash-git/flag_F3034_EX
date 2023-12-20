import plotly.express as px
from plotly.offline import plot

df = px.data.tips()
# 繪製提琴圖
fig = px.violin(df, x="day", y="total_bill")

plot(fig)