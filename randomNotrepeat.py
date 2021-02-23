import random as rd
li = ['red','green','blue']

for j in range(3):
    random = rd.choice(li)
    print(random)
    def isRandom(e):
        return not e == random
    li = list(filter(isRandom,li))
    #print(li)