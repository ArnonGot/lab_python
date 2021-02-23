#เขียนโปรแกรมรับจำนวนเต็ม จากนั้นพิมพ์จำนวนเต็มดังกล่าวออกมาทีละหลัก หลักละ 1 บรรทัด โดยพิมพ์จากหลักหน่วยก่อน

#ตัวอย่างการทำงาน 1 

#Enter number: 12437
#7
#3
#4
#2
#1

#ตัวอย่างการทำงาน 2 

#Enter number: 10000
#0
#0
#0
#0
#1

x = str(input('Enter Number: '))

li = []
for i in x:
    li.append(i)
    
a = int(len(li)) - 1

for j in range(a + 1):
    print(li[a])
    a = a - 1
