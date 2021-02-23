#ให้เขียนโปรแกรมรับจำนวนเต็ม N และ K จากนั้นพิมพ์เลขตั้งแต่ 1 ถึง N ที่ K หารลงตัว 

#Sample output

#Enter N: 10
#Enter K: 3
#3
#6
#9

N = int(input('Enter N: '))
K = int(input('Enter K: '))

for i in range(1,N+1):
    if i % K == 0:
        print(i)
    #if not i % K:
        #print(i)