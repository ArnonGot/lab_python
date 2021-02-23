name1 = str(input('Please enter your name: '))
name2 = []
name3 = []
aphabet = {'a' : 1,'b' : 2,'c' : 3,'d' : 4,'e' : 5,'f' : 6,'g' : 7,'h' : 8,'i' : 9,'j' : 10,'k' : 11,'l' : 12,'m' : 13,'n' : 14,'o' : 15,'p' : 16,'q' : 17,'r' : 18,'s' : 19,'t' : 20,'u' : 21,'v' : 22,'w' : 23,'x' : 24,'y' : 25,'z' : 26}

for i in name1:
    name2.append(i)    
for x1 in name2:
    for y1 in aphabet:
        if x1 == y1:
            name3.append(aphabet[y1])
            print(aphabet[y1],end='')
    
print('\r')
print(name3)
vsum  = sum(name3)
print(f'sum:{vsum}')
print('\r')