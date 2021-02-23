#map
li = [1,2,3,4]
def doubler(n):
    return n * 2
li = list(map(doubler, li))

print(li)

#lambda
#li = list(map(lambda n: n*2, li))
#print(li)