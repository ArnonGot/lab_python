# try out the birthday paradox

import random as rd
day = []
month = []
birthDays = []

def people(numbers):
    for i in range(numbers):
        d = rd.randint(1,31)
        m = rd.randint(1,12)
        day.append(d)
        month.append(m)

    for j in range(numbers):
        dayMonth = str(f'{day[j]}{month[j]}')
        birthDays.append(dayMonth)

    print(birthDays)

def repeatCheck():
    result = 'True'
    d = len(birthDays) - 1
    for i in range(d):
        for j in range(d-1):
            #print(birthDays[i],i)
            #print(birthDays[d],d)
            if birthDays[i] == birthDays[d]:
                print(f'Repeat is {birthDays[i]}!')
                result = 'False'
            d = d - 1
            if d == i:
                break
        d = len(birthDays) - 1
    return result

people(366)
print(repeatCheck())