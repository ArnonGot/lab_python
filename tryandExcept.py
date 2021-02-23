try:
    answer = 10/0
    number = int(input('Enter a Number: '))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print('invalid input')