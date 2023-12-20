import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["axes.unicode_minus"] = False
sns.set_style("white", {"axes.axisbelow": False,
                        "font.sans-serif":['Microsoft JhengHei']})

# 匯入CSV格式的檔案
df = pd.read_csv("pttbeauty2.csv", encoding="utf8")

sns.relplot(x="貼圖數", y="推文數", data=df)
plt.show()

