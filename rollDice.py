from secrets import randbelow
from time import sleep

print("Rolling dice...")

time = 320

for i in range(8):
    n = randbelow(6) + 1
    print("\r%d" % n, end = "")
    sleep(time / 1000)
    time = time - 40

print("\nDone")