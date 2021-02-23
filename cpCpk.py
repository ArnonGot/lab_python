partName = input('PART NAME/NO.: ')
control = input('INSP. ITEM: ')
maxTol = float(input('UPPER LEVEL: '))
minTol = float(input('LOWER LEVEL: '))
tol = maxTol - minTol
mean = (maxTol+minTol)/2
print(f'T(TOLARANCE): {tol}')
print(f'MEANSIZE: {mean}')
# input value
data = []
count = 0
while count < 30:
    x = float(input(f'No.{count+1}: '))
    data.append(x)
    count = count + 1
# average, sigma
avg =  sum(data) / len(data)
s = 0
for j in data:
    y = (j - avg) * (j - avg)
    s = s + y
import math
sigma = math.sqrt(s/29)
print('X-BAR: %.3f' %(avg))
print('SIGMA(n-1) %.4f' %(sigma))
# cp, cpkUp, cpkLow, cpk
cp = tol / (6 * sigma)
print('Cp=T/6S: %.2f' %(cp))
cpkUp = (maxTol-avg)/ (3 * sigma)
print('Cpk up: %.2f' %(cpkUp))
cpkLow = (avg-minTol)/ (3 * sigma)
print('Cpk low: %.2f' %(cpkLow))
if cpkUp > cpkLow :
    cpk = cpkLow
    print('Cpk: %.2f' %(cpk))
else: 
    cpk = cpkUp
    print('Cpk: %.2f' %(cpk))
# judge
if cp > 1.33 and cpk > 1.33:
    print(f'JUDGE: O')
else: 
    print(f'JUDGE: X')

