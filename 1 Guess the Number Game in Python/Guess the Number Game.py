import random

from sympy import false


def number_guessing_game():
    #Generate a random number between 1 to 10
    target_number = random.randint(1, 10)
    guess_correct = False
    attempts = 1
    print("Welcome to the Number Guess Game ! ")
    print("Please select the number between 1 to 10")

    while attempts<= 3:
        try:
            # Player input for the guess number
            guess = int(input("Enter your guess number: "))

            if guess < target_number:
                print("Too Low! Try Again")
            elif guess > target_number:
                print("Too High! Try Again")
            else:
                # When the player guess the right number
                print(f"Congratulations !!! You have guessed the number {target_number} in {attempts} attempts.")
                guess_correct = True
                break
            #Counter increment
            attempts += 1

        except ValueError:
            print("Invalid Input. Please enter a valid number")

    if not guess_correct:
        print("Sorry you have guessed wrong number for 3 times. \n!!! Better try next time !!!")

number_guessing_game()