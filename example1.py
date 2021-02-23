#ร้านขายหนังสือร้านหนึ่ง พยายามเพิ่มยอดขายโดยการเสนอโปรโมชั่นพิเศษ ถ้าคุณซื้อหนังสือมากกว่า 3 เล่ม ที่มีมูลค่ารวมเกิน 500 บาท คุณจะได้ส่วนลด 10% 
#ให้เขียนโปรแกรมรับจำนวนหนังสือที่ซื้อและราคารวม จากนั้นคำนวณราคาที่ต้องจ่าย 

#Sample output1

#How many books: 2
#How much: 1000
#You have to pay 1000 bath.

#Sample output2

#How many books: 5
#How much: 500
#You have to pay 500 bath.

#Sample output3

#How many books: 5
#How much: 600
#You have to pay 540 bath.


x = int(input('How many books: '))
y = int(input('How much: '))

discount = int(y * 0.10)

if x > 3 and y > 500:
    y = y - discount
    print(f'You have to pay {y} bath.')

else :
    print(f'You have to pay {y} bath.')
    