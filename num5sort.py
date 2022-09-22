x = 5
list1 = []
for i in range(x):
    number = int(input("รับค่า : "))
    list1.append(number)
    if i >= 4:
        for y in range(len(list1)):
            list1.sort(reverse=True)
            print(list1[y])