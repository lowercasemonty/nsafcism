import random

# select the number to be guessed
target_number = random.randint(1,10)
guess = 1

# loop through each guess attempt
while True:
    if guess < 4:
        curr_guess = int(input("Guess " + str(guess) + ": Enter a number between 1 and 10: "))
        
        if curr_guess < 1 or curr_guess > 10:
            print("Your number is outside the valid range")
            continue
        
        else:
            if (curr_guess == target_number):
                print("You are correct!")
                break
            elif (curr_guess < target_number):
                print("Your number is too low")
            else:
                print("Your number is too high")
            
            guess += 1
            
    elif guess >= 4:
        print("Sorry, but you have run out of attempts")
        break

# show that the game is complete       
print("---- Game over ----")
