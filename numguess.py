num = 20
enterNum = int(input("guess the number:"))

if(enterNum < num):
    enterNum = int(input("guess higher"))

if(enterNum > num):
    enterNum = int(input("guess lower:"))

if(enterNum == num):
    print("horray you guessed it right")
