x = int(input(""))
list1 = []
for i in range(x):
    number = int(input(""))
    list1.append(number)
    if i == x-1:
        for y in range(len(list1)):
            list1.sort(reverse=True)
            print(list1[y])
