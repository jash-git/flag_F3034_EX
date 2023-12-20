import pandas as pd

s = pd.Series([15, 33, 45, 55]) 
print(s) 
fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
s2 = pd.Series([15, 33, 45, 55], index=fruits) 
print(s2)
print(s2.index)
print(s2.values)  

 