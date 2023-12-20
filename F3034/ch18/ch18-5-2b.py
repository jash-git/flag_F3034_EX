import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["axes.unicode_minus"] = False
sns.set_style("white", {"axes.axisbelow": False,
                        "font.sans-serif":['Microsoft JhengHei']})

# 匯入CSV格式的檔案
df = pd.read_csv("pttbeauty2.csv", encoding="utf8")

sns.histplot(df["貼圖數"], kde=False)
plt.xlabel("貼圖數")
plt.ylabel("貼文數")
plt.title("貼圖數資料分佈的直方圖")
plt.show()

