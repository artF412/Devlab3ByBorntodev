years = int(input("รับค่าปี ค.ศ. : "))
sum = years%4
if years == 1800:
    print("Not a Leap Year")
elif sum == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
