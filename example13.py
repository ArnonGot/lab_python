#เขียนโปรแกรมรับอินพุตเข้ามา 3 ค่า
#ค่าแรก เป็น ตัวอักษรที่ต้องการให้แสดง
#ค่าที่ 2 เป็นจำนวน Row (จำนวนเต็มมีค่า >= 1)
#ค่าที่ 3 เป็นจำนวน Column (จำนวนเต็มมีค่า >= 1)
#ให้แสดงในรูปแบบที่ตัวอย่าง Sample Input/Output โดยระหว่างตัวอักษรในบรรทัดเดียวกันให้คั่นด้วย Space และ ท้ายบรรทัดมี 1 Space
#Sample Input 1:
# 4 5
#Sample Output 1:
# # # # #
# # # # #
# # # # #
# # # # #
#Sample Input 2:
#= 6 2
#Sample Output 2:
#= =
#= =
#= =
#= =
#= =
#= =

def table(sign,row,col,no):
    print(f'Sample Input {no}:')
    print(sign,row,col)
    x = []
    y = sign
    for i in range(col):
        x.append(y)
    print(f'Sample Output {no}:')
    z = 0
    while True:
        for _ in x:
            print(_,end=" ")
        print('\r')
        z = z + 1
        if z == row:
            break

table('#',4,5,1)
table('=',6,2,2)
        



