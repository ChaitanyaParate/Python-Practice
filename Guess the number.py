import random
import math
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
x = random.randint(lower , upper)
count = 0
limit = round(math.log2(upper - lower))
print("You have" , limit , "tries" )
while True:
    while count < limit:
        guess = int(input("Enter your guess: "))
        if guess == x: 
            print("Your guess is right") 
            print("You wone in" , count , "tries")
            break
        elif guess > x and guess < upper:
            print("You guessed a higher number")
            count = count + 1
            continue
        elif guess < x and guess > lower:
            print("You guessed a lower number")
            count = count + 1
            continue
        elif guess < lower: 
            print("Out of the limit")
            continue
        elif guess > upper: 
            print("Out of the limit")
    if count == limit: 
        print("Try again") 
        print("Number was: ",x)
        break