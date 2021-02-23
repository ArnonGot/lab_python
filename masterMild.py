#ในเกมมาสเตอร์มายด์ เราต้องการสุ่มเลขตั้งต้นที่ไม่มีเลขหลักใดซ้ำกันเลย การสุ่มดังกล่าวทำได้ไม่ยากถ้าเราสามารถตรวจสอบว่าตัวเลข 4 หลักที่เราได้สุ่มมานั้นมีหลักซ้ำกันหรือไม่ 

import random as rd
li = []
for i in range(4):
    x = rd.randint(0,10)
    li.append(x)    
print(li)
result = 'True'
d = len(li) - 1
for i in range(d):
    #print('n',i)
    for j in range(d+1):
        print(li[i])
        print(li[d])
        if li[i] == li[d]:
            result = 'false'
        d = d - 1
        if d == i:
            break       
    d = len(li) - 1
print(result)