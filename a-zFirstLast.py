name1 = input("Name 1 : ")
name2 = input("Name 2 : ")
choose = input("Select first or last : ")

if choose.lower() == "first":
    if name1 < name2: # check if name1 is in front of name2 (alphabetical)
        print(name1)
    else:
        print(name2)
else:
    if name1 > name2: # check if name1 is after name2 (alphabetical)
        print(name1)
    else:
        print(name2)