x = str(input('Enter number: '))

li = []

for i in x:
    li.append(i)

d = int(len(li)) - 1

vSum = 0

for i in range(d + 1):

    y = int(li[d]) * 2 ** i
    d = d - 1
    vSum = vSum + y

print(vSum)
