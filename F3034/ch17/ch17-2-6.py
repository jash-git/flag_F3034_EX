import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
print(df.corr())

sns.set()
sns.heatmap(df.corr())
plt.show()
