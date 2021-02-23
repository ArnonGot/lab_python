# order by max to min

x = str(input('Enter Number: '))

number = sorted(x)

li = []

for i in number:
    li.append(i)
#print(li)

a = int(len(li)) - 1

for i in range(a + 1):
    print(li[a])
    a = a - 1
    


