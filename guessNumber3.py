import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            random_number = random.randint(low,high)
        else:
            random_number = low#could also be high b/c low = high
        feedback = input(f'Is {random_number} too high (h), too low (l), or correct (c)')
        if feedback == 'h':
            high = random_number - 1
        elif feedback == 'l':
            low = random_number + 1
    print(f'Yay!, The computer guessed your number, {random_number} correctly!')
    
computer_guess(1000)