#ในเกมมาสเตอร์มายด์ เราต้องการสุ่มเลขตั้งต้นที่ไม่มีเลขหลักใดซ้ำกันเลย เราจะนำฟังก์ชัน verify_digits จากข้อที่แล้วที่เราได้เขียนไว้มาสร้างเป็นฟังก์ชันสำหรับสุ่มตัวเลขคำตอบของเกมนี้

#ในการสุ่มตัวเลข 4 หลักเราจะใช้ฟังก์ชัน randint ในโมดูล random ฟังก์ชัน randint(a,b) จะคืนค่าเป็นเลขสุ่มที่มีค่าเป็นไปได้ตั้งแต่ a ถึง b (รวม a และ b ด้วย) ดูตัวอย่างการใช้งานที่ เอกสารนี้

#ให้เขียนฟังก์ชัน rand_answer() ที่คืนค่าเป็นจำนวนเต็ม 4 หลัก (นั่นคือต้องมีค่าอย่างน้อย 1000 แต่มีค่าไม่เกิน 9999) ที่ไม่มีหลักใด ๆ ที่ซ้ำกันเลย

#ตัวอย่างการทำงาน (แสดงใน Python shell)

#>>> randanswer()
#1324
#>>> randanswer()
#8503
#>>> rand_answer()
#6359

#หมายเหตุ: ฟัง์กชันของนิสิตไม่จำเป็นต้องตอบตรงกับตัวอย่าง
# You CAN use function verify_digits but you do not have to write it.

import random as rd
x = rd.randint(1000,9999)

def verify_digits(x):
    li = []
    for i in str(x):
        li.append(i)
    result = 'True'
    d = len(li) - 1
    for j in range(d):
        for k in range(d+1):
            if li[j] == li[d]:
                result = 'False'
            d = d - 1
            if d == j:
                break
        d = len(li) - 1
    return result
    
def randanswer(verify_digits):
    if verify_digits(x) == 'True':
        return x
      
print(randanswer(verify_digits))

