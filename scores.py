#student point
points = []
n = int(input(('Please enter number of subject (1-7) ')))
print(f'The program score of {n} students')
for i in range(n):
    p = int(input((f'Student{i+1} : ')))
    points.append(p)

print('\nAverage :',sum(points)/len(points))
print('Maximum of score :',max(points))
print('Minimum of score :',min(points))
