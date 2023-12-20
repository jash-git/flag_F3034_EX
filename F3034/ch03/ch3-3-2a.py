try:
    n1, n2 = eval(input("輸入2個整數(n1,n2) => "))
    r = n1 / n2
    print("變數r的值 = " + str(r))    
except ZeroDivisionError:
    print("錯誤: 除以0的錯誤!")
except SyntaxError:
    print("錯誤: 輸入數字需以逗號分隔!")
except:
    print("錯誤: 輸入錯誤!")
    