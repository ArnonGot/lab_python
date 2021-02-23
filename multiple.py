from time import sleep

def multiple(m):
    
    print(f"multiple {m}...")
    time = 400
    
    for i in range(13):
        n = m * i 
        print(f"\n {m} x {i} = {n}")
        sleep(time / 650)
        time = time - 10
    print("\nDone")

multiple(12)