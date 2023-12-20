import seaborn as sns

df = sns.load_dataset("iris")
print(df.head())
df.head().to_html("ch15-1-4a.html")


