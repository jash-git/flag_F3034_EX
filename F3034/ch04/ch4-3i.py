# 定義變數height為使用者輸入的身高（公分）除以100得到的公尺值
height = float(input("請輸入您的身高（公分）：")) / 100

# 定義變數weight為使用者輸入的體重（公斤）
weight = float(input("請輸入您的體重（公斤）："))

# 定義變數bmi為計算得到的BMI值，公式為體重（公斤）除以身高的平方（公尺平方）
bmi = weight / (height ** 2)

# 輸出BMI值，並使用round函數將小數點後的位數設為2
print("您的BMI值為：", round(bmi, 2))
