# order from last to first 

number = str(input('Enter Number: '))

li = []
for i in number:
    li.append(i)
#print(li)

a = int(len(li)) - 1

for j in range(a + 1):
    print(li[a])
    a = a - 1
