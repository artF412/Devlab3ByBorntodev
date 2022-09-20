years = int(input("รับค่าปี ค.ศ. : "))
sum = years%4
if sum == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")