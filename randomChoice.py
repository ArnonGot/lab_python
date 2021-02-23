import random as rd
#input player
p = int(input('how many number of player? '))
#hello player
#for h in range(p):
    #print(f'hello! player-{h+1}')
#nameask
nl = []
for i in range(p):
    nameLoop = str(input(f'hello! player-{i+1}, what is your name? '))
    nl.append(nameLoop)
    #print(nl)
    
#create function
#def player(p):
    #for i in range(p):
        #nameLoop = str(input(f'hello! player- {i+1}, please enter your name = '))
        
#input list
lt = []
l = int(input('how many number of choice? '))
for j in range(l):
    condition = str(input(f'please enter choice-{j+1} = '))
    lt.append(condition)
    
print('*******************************************')

#randomStart

for k in range(l):
    random = rd.choice(lt)
    print(f'{nl[k]} =',random)
    def isRandom(e):
        return not e == random
    lt = list(filter(isRandom,lt))
    #print(f'hello! player- {k+2}, your random is',lt)

    
    


    

