import random
number = int(random.randint(0,20))
#print(number)
vRound = 0
vCorect = False
for i in range(1,7):
    x = int(input("pls enter ur number "))
    if x == number:
        vCorect = True
        print("**********************")
        print("congrat! u guess is right.")
        print("end of game")
        if vCorect == True:
            break
    else :
        if x < number :
            print("lower!, try again")
            vRound = vRound + 1
            if vRound > 5:
                print("**********************")
                print("sry! over than 6times")
                print("end of game")
        else :
            print("greater!, try again")
            vRound = vRound + 1
            if vRound > 5:
                print("**********************")
                print("sry! over than 6times")
                print("end of game")