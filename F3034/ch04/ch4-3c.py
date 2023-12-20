def bmi(height, weight):
    height_m = height / 100
    return weight / (height_m * height_m)

height = float(input("請輸入身高（公分）："))
weight = float(input("請輸入體重（公斤）："))

bmi_value = bmi(height, weight)

print("您的BMI值為：{:.2f}".format(bmi_value))
