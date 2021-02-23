def histogram(a):

    n = [[],[],[],[],[],[],[],[],[],[]]
    x = int(input(''))

    while x >= 0 and x < 100:

        for i in range(a):

            if x == i:
                n[0].append('*')
            
            elif x == i+10:
                n[1].append('*')

            elif x == i+20:
                n[2].append('*')

            elif x == i+30:
                n[3].append('*')

            elif x == i+40:
                n[4].append('*')

            elif x == i+50:
                n[5].append('*')

            elif x == i+60:
                n[6].append('*')

            elif x == i+70:
                n[7].append('*')

            elif x == i+80:
                n[8].append('*')

            elif x == i+90:
                n[9].append('*')

        x = int(input(''))

    for j in range(a):

        sum = ''
        for y in n[j]:
            sum = sum + y
        print(f'{j} : {sum}')

histogram(10)





