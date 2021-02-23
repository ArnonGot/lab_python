#เขียนโปรแกรมรับอินพุตเข้ามา 2 ค่า
#ค่าแรก เป็น ตัวอักษร
#ค่าที่ 2 เป็น ค่าตัวเลขจำนวนเต็ม >= 1 (บอกจำนวน Row และ Column ที่เท่ากัน)
#ให้แสดงในรูปแบบที่ตัวอย่าง Sample Input/Output
#โดยกำหนดให้การแสดงผลตัวเลขหรือตัวอักษรให้แสดงในช่องขนาด 3 ช่องชิดขวา และท้ายบรรทัดไม่มี Space
#Sample Input 1:
#* 6
#Sample Output 1:
 #*  1  *  2  *  3
 #4  *  5  *  6  *
 #*  7  *  8  *  9
 #10  * 11  * 12  *
 #* 13  * 14  * 15
 #16  * 17  * 18  *
#Sample Input 2:
#$ 4
#Sample Output 2:
 #$  1  $  2
 #3  $  4  $
 #$  5  $  6
 #7  $  8  $
  
def table(sign,row,no):
    print(f'Sample Input {no}:')
    print(sign,row)
    x = []
    y = sign
    a = int(row)/2
    for i in range(int(a)):
        x.append(y)
    print(f'Sample Output {no}:')
    z = 0
    h = 0
    s = 0
    while True:
        for _ in x:
            print('',_,end=f' {h+1}')
            h = h + 1
            z = z + 1
            if z == a:
                break
        print('\r')        
        for _ in x:
            print('',f'{h+1}',end=f' {_}')
            h = h + 1
            z = z + 1
            if z == a:
                break
        print('\r') 
        s = s + 1
        if s == a:
            break

table('*',6,1)
table('$',4,2)