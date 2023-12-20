import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

days = range(0, 22, 3)
celsius1 = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
celsius2 = [15.4, 13.1, 21.6, 18.1, 16.4, 20.5, 23.1, 13.2]

plt.plot(days, celsius1, "r-o", label="住家")
plt.plot(days, celsius2, "g--", label="辦公室")
plt.legend(loc=3)
plt.xlabel("日")
plt.ylabel("攝氏溫度")
plt.title("住家和辦公室溫度變化")
plt.show()

