#Program Check Prime Number 1-1000
num = int(input('Please fill Number : '))
if num > 1:
    for i in range(2,num+1):
        if (num%2 == 0) and (num != 2):
            print('Number :',num,'Not Prime Number')
            break
        elif (num%3 == 0) and (num != 3):
            print('Number :',num,'Not Prime Number')
            break
        elif (num%5 == 0) and (num != 5):
            print('Number :',num,'Not Prime Number')
            break
        elif (num%7 == 0) and (num != 7):
            print('Number :',num,'Not Prime Number')
            break
        elif (num%11 == 0) and (num != 11):
            print('Number :',num,'Not Prime Number')
            break
        elif (num%13 == 0) and (num != 13):
            print('Number :',num,'Not Prime Number')
            break
        elif (num%17 == 0) and (num != 17):
            print('Number :',num,'Not Prime Number')
            break
        elif (num%19 == 0) and (num != 19):
            print('Number :',num,'Not Prime Number')
            break
        elif (num%23 == 0) and (num != 23):
            print('Number :',num,'Not Prime Number')
            break
        elif (num%29 == 0) and (num != 29):
            print('Number :',num,'Not Prime Number')
            break
        elif (num%31 == 0) and (num != 31):
            print('Number :',num,'Not Prime Number')
            break
        elif (num%37 == 0) and (num != 37):
            print('Number :',num,'Not Prime Number')
            break
        else:
            print('Number :',num,'is Prime Number')
            break            
else:
    print('Number :',num,'Not Prime Number')