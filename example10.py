#ให้เขียนรับตัวเลขฐาน 2 จากผู้ใช้ จากนั้นแปลงให้เป็นเลขฐานสิบ

#ตัวอย่างการทำงาน 1 

#Enter binary number: 10110
#22

#ตัวอย่างการทำงาน 2 

#Enter binary number: 110
#6

#**คำใบ้: อย่าลืมว่าเราสามารถพิจารณาสตริงเป็นรายการของตัวอักษรได้ 

x = str(input('Enter number: '))
li = []
for i in x:
    li.append(i)
d = int(len(li)) - 1
vSum = 0
for i in range(d + 1):
    y = int(li[d]) * (2 ** i)
    d = d - 1
    vSum = vSum + y
print(vSum)
    
