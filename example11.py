#ให้เขียนฟังก์ชัน verify_digits(x) ที่รับจำนวนเต็มบวก x จากนั้นคืนค่าเป็น True ก็ต่อเมื่อเลขในแต่ละหลักของ x เมื่อเขียนเป็นเลขฐานสิบ ไม่มีตัวใดซ้ำกันเลย และคืนค่าเป็น False เมื่อมีตัวเลขที่ซ้ำกัน 

#ตัวอย่างการทำงานใน Python Shell

#>>> verify_digits(12345)
#True
#>>> verify_digits(1242)
#False
#>>> verify_digits(938401)
#True
#>>> verify_digits(194842)
#False

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

print(verify_digits(12345))
print(verify_digits(1242))
print(verify_digits(938401))
print(verify_digits(194842))