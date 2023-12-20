import seaborn as sns

df = sns.load_dataset("tips")
print(df.head())
df.head().to_html("ch15-1-4.html")


