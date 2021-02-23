#คำนวณฟังก์ชัน
#ให้เขียนฟังก์ชัน func(x) ที่คำนวณค่า 

#ตัวอย่างการทำงานใน Python Shell 

#>>> print(func(0))
#0.0
#>>> print(func(10))
#106.696700846
#>>> print(func(20))
#451.779774682

#ตรวจสอบว่าอยู่ใต้เส้นโค้งหรือไม่
#เขียนฟังก์ชัน under(x,y) เพื่อตรวจสอบว่า จุด (x,y) อยู่ใต้เส้นของฟังก์ชัน f(x) ที่เขียนด้วยฟังก์ชัน func หรือไม่ ให้ฟังก์ชัน under คือค่าเป็น Boolean

#ในการเขียนฟังก์ชันดังกล่าวให้เรียกใช้ฟังก์ชัน func ตามที่ได้เขียนไว้จากข้อที่แล้ว แต่ในการตอบไม่ต้องใส่ฟังก์ชันดังกล่าวลงไป

#ตัวอย่างของโปรแกรมหลักที่เรียกใช้ฟังก์ชันดังกล่าว 

#x = float(input("Enter X: "))
#y = float(input("Enter Y: "))
#if under(x,y):
    #print("It is.")
#else:
    #print("It is not.")


#ตัวอย่างการทำงาน 1 
#Enter X: 0
#Enter Y: 0
#It is not.

#ตัวอย่างการทำงาน 2 

#Enter X: 10
#Enter Y: 100
#It is.
#(ไม่ต้องเขียน main program ฟังก์ชัน func(x) ได้ถูกเขียนไว้แล้วใช้ได้เลย)

def func(x):
    y = x**2*(2-2**(-x/100))
    return y

def under(x,y):
    if func(x) > y:
        return True
    return False

def area(a,b):
    n = 0
    for x in range(int(math.pow(10,4))):
        xx = random.randint(int(a),int(b))
        y = random.randint(0,int(func(b)))
        if xx >= a and xx <= b:
           if under(xx,y):
               n = n+1
    sum = (b-a)*func(b)*(n/int(math.pow(10,4)))
    return sum
    
func(0)