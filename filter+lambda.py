#filter+lambda()
li = ['apple','banana','orange','apple','banana']

li = list(filter(lambda e: not e == 'apple', li))

print(li)