lt = []
paid = []

print('Anyonghaseoyo!!!')
print('Welcome to Enough Cafe.\n')

menu = {'americano' : 80, 'latte' : 90, 'cappuchino' : 100, 'chocolate' : 100}

print('This is our drinks \n*****************')

#for x in menu:
    #print(x + ' ' ,end=' ')
    #print(menu[x])

for x,y in menu.items():
    print(x,y)
print('*****************')

order = str(input('\nWould you be prefer? '))

cond = str(input('hot? or iced? '))

lt.append(str(order) + ' ' + str(cond))

paid = menu[f'{order}']

add = str(input('Order more? y/n '))

while add == 'y' :
    order = str(input('\nWould you be prefer? '))
    cond = str(input('hot? or iced? '))
    add = str(input('Order more? y/n '))
    lt.append(str(order) + ' ' + str(cond)) 
    
    paid = paid + menu[f'{order}']

    if add != 'y' :
        break
 
print('\nYour order is',lt)
print(f'\nTotal payment is {paid} baht')
        