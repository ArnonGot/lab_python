import random as rd
x = rd.randint(1000,9999)

def verify_digits(x):
    li = []
    for i in str(x):
        li.append(i)
    result = 'True'
    d = len(li) - 1
    for j in range(d):
        for _ in range(d+1):
            if li[j] == li[d]:
                result = 'False'
            d = d - 1
            if d == j:
                break
        d = len(li) - 1
    return result

def randanswer(verify_digits):
    if verify_digits(x) == 'True':
        return x

print(randanswer(verify_digits))

