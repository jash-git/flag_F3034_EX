import pandas as pd

df = pd.read_csv("products.csv", encoding="utf8")

print(df.head()) 
print(df.head(3))
df.head().to_html("ch13-2-4-01.html")
df.head(3).to_html("ch13-2-4-02.html")

print(df.tail())
print(df.tail(3)) 
df.tail().to_html("ch13-2-4-03.html")
df.tail(3).to_html("ch13-2-4-04.html") 