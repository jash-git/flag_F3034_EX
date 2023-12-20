import plotly.express as px
from plotly.offline import plot

df = px.data.tips()
# 繪製派圖
fig = px.pie(df, values="total_bill", names="day")

plot(fig)