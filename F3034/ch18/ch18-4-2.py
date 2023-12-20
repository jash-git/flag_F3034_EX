import pandas as pd

df = pd.read_csv("duplicated-data.csv")
print(df)
df.to_html("ch16-4-2.html")
