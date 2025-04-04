import random

def guess_number_game():
    print("Welcome to the Guess the Number Game!")
    print("I am thinking of a number between 1 and 25.")
    
    
    number_to_guess = random.randint(1, 25)
    
    
    chances = 10
    
    while chances > 0:
        print(f"You have {chances} chances left.")
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number!")
            break
        
        chances -= 1
    
    if chances == 0:
        print(f"Sorry, you've run out of chances. The number was {number_to_guess}.")

# Start the game
guess_number_game()
