import random

num = random.randint(1, 100)
guess = None
score = 0
print(num)
while guess != num:
    if score >= 5:
     break
    guess = input("guess a number between 1 and 100: ")
    guess = int(guess)

    if guess == num:
        print("Correct!")
        score =+ score + 1
        print ("It took you:", score, "guesses!")
        break
    elif guess < num:
        print("Nope, try a bigger? number")
        score =+ 1
    elif guess > num:    
        print("Nope, try a lower number")
        score =+ 1
print ("It took you:", score, "guesses!")
