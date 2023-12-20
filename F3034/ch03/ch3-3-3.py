lst1 = [1, 2, 3, 4, 5]
try:
    idx = int(input("輸入索引值 => "))
    print(lst1[idx])    
except IndexError:
    print("錯誤: 串列的索引值錯誤!")  
else:
    print("Else: 輸入的索引沒有錯誤!")
    