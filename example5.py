#หอยทากตัวหนึ่ง ตกลงไปในบ่อที่มีความสูง H เมตร มันพยายามจะไต่ให้ถึงปากบ่อ ในเวลากลางวันหอยทากไต่ขึ้นไปได้ U เมตร เวลากลางคืนมันนอนหลับจึงไม่ได้ไต่แต่กลับไถลลงมาเป็นระยะทาง D เมตร ให้เขียนโปรแกรมเพื่อหาว่าหอยทากจะใช้เวลากี่วันในการไต่ออกจากบ่อ (กำหนดให้หอยทากเริ่มไต่ในเวลากลางวัน)

#Example 1

#H: 5
#U: 10
#D: 1
#1 day(s).



#Example 2

#H: 5
#U: 3
#D: 2
#3 day(s).

H = int(input('H: '))
U = int(input('U: '))
D = int(input('D: '))

k = 0
day = 1
while True:
    k = k + U
    if k >= H:
        break
    k = k - D
    day = day + 1
print(day,"day(s).")
