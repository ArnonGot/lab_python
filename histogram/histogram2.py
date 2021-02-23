def histogram(a):

    n = [[],[],[],[],[],[],[],[],[],[]]
    x = int(input(''))

    while x >= 0:

        for i in range(a):

            if x == i:
                n[i].append('*')

        x = int(input(''))

    for j in range(a):

        sum = ''
        for y in n[j]:
            sum = sum + y
        print(f'{j} : {sum}')

histogram(10)





