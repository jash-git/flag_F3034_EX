import pandas as pd

hours_phone_used = [0,0,0,1,1.3,1.5,2,2.2,2.6,3.2,4.1,4.4,4.4,5]
work_performance = [87,89,91,90,82,80,78,81,76,85,80,75,73,72]

df = pd.DataFrame({"手機使用時間(小時)":hours_phone_used,
                   "工作效率":work_performance})
print(df.corr())
df.corr().to_html("ch16-2-2.html")