import random
myrandom = random.randrange(1,7)
round = 0
correct = False
print("คุณมีโอกาสตอบแค่เพียง 3 ครั้ง \n")
while True:
    num = int(input("ป้อนคำตอบ : "))
    correct = (num==myrandom)
    if not correct:
        if(num>myrandom):
            print("มากไป")
        if(num<myrandom):
            print("น้อยไป")
    if correct :
        print("ตอบถูกต้องคุณเยี่ยมมาก")
        break
    round+=1
    if num<0 or round==3:
        break
if not correct:
    print("เสียใจด้วยนะ")
print("เฉลย = ",myrandom)
print("จบโปรแกรม")