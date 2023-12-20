import pandas as pd

df = pd.read_csv("duplicated-data.csv")

df1 = df.drop_duplicates("COL_B")
print(df1)
df1.to_html("ch16-4-2b-01.html") 

df2 = df.drop_duplicates("COL_B", keep="last")
print(df2)
df2.to_html("ch16-4-2b-02.html") 

df3 = df.drop_duplicates("COL_B", keep=False)
print(df3)
df3.to_html("ch16-4-2b-03.html") 