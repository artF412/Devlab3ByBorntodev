weightList = []
def weghitFish():
    while True:
        weight = int(input("น้ำหนักปลา : "))
        if weight == 0:
            txt = input("Max Or Min : ")
            if txt.lower() == "max":
                for x in range(len(weightList)):
                    weightList.sort(reverse=True)
                    print(weightList[x],end=" ")
            elif txt.lower() == "min":
                for x in range(len(weightList)):
                    weightList.sort()
                    print(weightList[x],end=" ")
            else:
                print("No funtion")
            break
        else:
            weightList.append(weight)
weghitFish()
