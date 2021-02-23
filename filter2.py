#filter2()
li = ['apple','banana','orange','apple','banana']

def isApple(e):
    return not e == 'apple'
    
li = list(filter(isApple,li))

print(li)