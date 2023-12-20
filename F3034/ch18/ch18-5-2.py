import pandas as pd

# 匯入JSON格式的檔案
df = pd.read_json("pttbeauty.json", encoding="utf-8")

df = df[df["images"] != 0]
df = df[df["author"] != "GeminiMan (GM)"]
df = df.drop(["file_urls","url","score","date","title"], axis=1)

df.columns = ["作者", "推文數", "回應數", "貼圖數"]
df.to_csv("pttbeauty2.csv", index=False, encoding="utf8")
print("存入pttbeauty2.csv")

print(df.info())

print(df.head())
df.head().to_html("Ch16-5-2.html")

