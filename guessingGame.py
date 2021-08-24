import random


print("Number guessing Game")

#randint function generates the random number between 1 to 9
number=random.randint(1,9)

# number of changes to be given to the user to guess the number
#or it is the inputs given by user into the input box here number of chances are5

chances=0

print("Guess a number (between 1 and 9) :- ")

#while loop to count the number of chances

while chances<5:
    #Enter a number between 1 to 9
    guess=int(input("Enter your guess :- "))

    #compare the user guess with the computer number

    if guess == number:
        print("Congratulation YOU WIN !!")
        break

    elif guess < number:
        print("Your  guess was too low : Guess a number higher than ", guess)

    else:
         print("Your  guess was too high : Guess a number lower than ", guess)

    chances +=1

if not chances < 5:
    print("You Lose !!! The number is :- ", number)    
      