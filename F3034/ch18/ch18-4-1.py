import pandas as pd

df = pd.read_csv("missing-data.csv")
print(df)
df.to_html("ch16-4-1.html")