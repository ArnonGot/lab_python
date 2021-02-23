convert = []

x = int(input('Enter number: '))
    
while x != 0 :

    for i in range(100):

        n = 2 * i

        if x - n == 0:
            convert.append(0)
            #print(n)
            #print(int(n/2))
            #print('*************************')
            x = int(n/2)

        elif x - n == 1:
            convert.append(1)
            #print(n)
            #print(int(n/2))
            #print('*************************')
            x = int(n/2)
        
        elif x == 0 or x == 1:
            break

#print(convert)

d = int(len(convert)) - 1

for _ in range(d + 1):
    print(convert[d], end ="")
    d = d - 1
