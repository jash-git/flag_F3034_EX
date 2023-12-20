import plotly.express as px
from plotly.offline import plot

x = [1, 2, 3, 4]
y = [4, 3, 2, 1]

fig = px.line(x=x, y=y, markers=True)

plot(fig)