import random
num=random.randint(1,100)
x=0
count=0
while count!=5:
        usr=int(raw_input ("enter number"))
        if num>usr :
            print("entered number is greater")
        elif num<usr:
            print("entered number is lesser")
        else :
            print("Entered number is guessed")
            x =1
            break
        count=count+1
if(x==0):
        print("not found;the correct number is", num)
