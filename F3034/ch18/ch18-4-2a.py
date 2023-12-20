import pandas as pd

df = pd.read_csv("duplicated-data.csv")

df1 = df.drop_duplicates()
print(df1)
df1.to_html("ch16-4-2a.html") 
