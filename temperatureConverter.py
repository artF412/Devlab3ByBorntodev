temp = input("ป้อนอุณหภูมิ(องศา)C/F : ")
degree = temp[:-1]
unit = temp[-1].upper()
if unit=="C":
    resultF = (int(degree)*9/5)+32
    print(str(resultF)+'F')
if unit=="F":
    resultC = (int(degree)-32)*5/9 
    print(str(resultC)+'C')