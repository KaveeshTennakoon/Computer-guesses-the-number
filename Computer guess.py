import random

def guessing(num):
    flag=False
    count=1
    minimum=0
    maximum=100
    guess=random.randint(minimum,maximum)
    while flag==False:
        print("Guess",count,":",guess)
        if guess==num:
            flag=True
            print("Yayy,got it right")
        elif guess<num:
            minimum=guess+1
            guess=random.randint(minimum,maximum)
        elif guess>num:
            maximum=guess-1
            guess=random.randint(minimum,maximum)
        count=count+1
    print("It took",count-1,"attempts to computer to guess your number")

def getnum():
    num=int(input("Enter the number between 1 & 100: "))
    while num<1 or num>100:
        num=int(input("Pls make sure your number is between 1 & 100: "))
    return num


number=getnum()
guessing(number)
