lt = []
paid = []

print('\nHello!')
print('Welcome to Coffee shop.\n')

menu = {'Americano' : 80, 'Latte' : 90, 'Cappuchino' : 100, 'Chocolate' : 100}

print('This is our drinks.\n******************')

for x,y in menu.items():
    print(f'{x} = {y}')

order = str(input('Would you be prefer?\n'))
select = str(input('Hot or Iced?\n'))
moreCheck = str(input('Would you order more? Yes (y) No (n)\n'))

lt.append(f'{order} {select}')
paid = menu[f'{order}']

while moreCheck == 'y' :
    order = str(input('Would you be prefer?\n'))
    select = str(input('Hot or Iced?\n'))

    lt.append(f'{order} {select}')
    paid = paid + menu[f'{order}']

    moreCheck = str(input('Would you order more? Yes (y) No (n)\n'))
    if moreCheck != 'y' :
        break

print(f'\nYour order is {lt}')
print(f'Total banlance is {paid}')






