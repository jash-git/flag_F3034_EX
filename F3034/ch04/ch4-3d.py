import math

def bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    return weight_kg / math.pow(height_m, 2)

height = float(input("請輸入身高（公分）："))
weight = float(input("請輸入體重（公斤）："))

bmi_value = bmi(height, weight)

print("您的BMI值為：{:.2f}".format(bmi_value))

