#เขียนโปรแกรมรับจำนวนเต็มบวก 1 จำนวน จากนั้นให้แสดงผลลัพธ์เป็นจำนวนเต็มดังกล่าวที่เขียนอยู่ในรูปของตัวเลขฐาน สอง

#ตัวอย่างการทำงาน 1 

#Enter number: 19
#10011

#ตัวอย่างการทำงาน 2 

#Enter number: 6
#110

convert = []
x = int(input('Enter number: '))
while x != 0:
    for i in range(100000):
        n = 2 * i
        if x - n == 0:
            convert.append(0)
            x = int(n/2)
        elif x - n == 1:
            convert.append(1)
            x = int(n/2)
        elif x == 0 or x== 1:
            break
d = int(len(convert))-1
for _ in range(d+1):
    print(convert[d], end="")
    d = d - 1
            
        