
def customerRegister():
    customerCount = int(input("จำนวนลูกค้า : "))
    customerName = []
    customerYearsBirth = []
    customerGender = []
    years = 2017
    for i in range (customerCount):
        nameCustomer = input("กรอกชื่อ-นามกสุล : ")
        customerName.append(nameCustomer)
        birthYearsCustomer = int(input("กรอกปีเกิดของลูกค้า (ค.ศ.) : "))
        customerYearsBirth.append(birthYearsCustomer)
        genderMaleOrFemale = input("กรอกเพศ Male(ชาย) หรือ Female(หญิง) : ").capitalize
        customerGender.append(genderMaleOrFemale)
    print("--Customers Information--")
    for x in range(len(customerName)):
        print(customerName[x],"(age :",str(years-customerYearsBirth[x])+")")

customerRegister()





