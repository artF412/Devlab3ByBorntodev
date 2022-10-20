x = int(input("รับค่าตัวเลขตีกรอบ : "))
if x > 1:
    print("#"*x)
    for i in range(x-2):
        print("#"+" "*(x-2)+"#")
else:
    pass
print("#"*x)
