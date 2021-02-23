#filter1()
li = ['apple','banana','orange','apple','banana']

def isApple(e):
    return e == 'apple'
    
li = list(filter(isApple,li))

print(li)