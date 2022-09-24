#โปรแกรมคำนวณค่า BMI (ดัชนีมวลร่างกาย)
#Formula BMI = weight/(high*high)

#input weight and high
weight = int(input("กรอกน้ำหนัก (kg) : "))
high = int(input("กรอกส่วนสูง (cm) : "))

#process convert cm to m
high /= 100
#process bmi
bmi = weight/(high*high)

#output BMI
print("BMI :",bmi)