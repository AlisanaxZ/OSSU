import random
def test(guess, num):
    if guess**2 == num:
        answer = guess
        print(answer)
    else:
        div = num/guess
        average = (guess + div)/2
        guess = average
        test(guess, num)
    
def square_root(num):
    answer = 0
    guess = random.randint(1,num)
    answer = test(guess, num)
square_root(9)