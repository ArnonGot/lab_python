import random as rd

nl = []

def player(x):
    print('\n******* Name input *********')
    for i in range(x):
        nameLoop = str(input(f'Player-{i+1}, What is your name?\n'))
        nl.append(nameLoop)
        #print(nl)
    
    l = []
    print('******* Choice input *******')
    for j in range(x):
        choice = str(input(f'Please enter choice-{j+1}\n'))
        l.append(choice)
        #print(l)

    print('******* Random output *******')
    for k in range (x):    
        random = rd.choice(l)
        print(f'{nl[k]} =',random)
        def isRandom(e):
            return not e == random
        l = list(filter(isRandom,l))

player(4)