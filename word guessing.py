import random
name = input("What is your name? ")
print("Good Luck ! ", name)
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
print("Guess the characters") 
guesses = ''
turns = 12
failed = 0
while turns > 0: 
    print()
    guess = input("Guess a character: ")
    guesses = guesses + guess
    if all(charac in guesses for charac in word):
        print(word)
        print("You Wone!")
        print("The word is " , word)
        break
    elif guess not in word:
        turns = turns - 1
        print("Wrong")
        print("You have" , turns , 'guesses left.')
        continue
    for char in word:
        if char in guesses:
            print(char, end=" ")
        elif char not in guesses:
            print("_")
            failed = failed + 1
if turns == 0: 
    print("You loose")