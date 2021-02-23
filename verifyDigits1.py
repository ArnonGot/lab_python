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

print(verify_digits(12345))
print(verify_digits(1242))
print(verify_digits(938401))
print(verify_digits(194842))
