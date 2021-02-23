x = int(input(''))
n = [[],[],[],[],[],[],[],[],[],[]]

while x >= 0:
    if x == 0 :
        n[0].append('*')
    elif x == 1 :
        n[1].append('*')
    elif x == 2 :
        n[2].append('*')
    elif x == 3 :
        n[3].append('*')
    elif x == 4 :
        n[4].append('*')
    elif x == 5 :
        n[5].append('*')
    elif x == 6 :
        n[6].append('*')
    elif x == 7 :
        n[7].append('*')
    elif x == 8 :
        n[8].append('*')
    elif x == 9 :
        n[9].append('*')
    x = int(input(''))

for j in range(10):
    sum = ''
    for y in n[j]:
        sum = sum + y
    print(f'{j} : {sum}')


