# The secret number is set to 7, as requested.
CORRECT_NUMBER = 7

# Initialize the user's guess to an incorrect value (e.g., 0) 
# so the 'while' loop condition is True at the start.
user_guess = 0 

print("--- Simple Number Guesser ---")
print("Guess the secret number between 1 and 10.")

# The loop runs repeatedly WHILE the user's guess is NOT equal to the correct number.
while user_guess != CORRECT_NUMBER:
    
    # 1. Get input from the user (we assume valid integer input for simplicity).
    guess_input = input("Enter your guess: ")
    
    # Convert the input string to an integer
    user_guess = int(guess_input)
    
    # 2. Check the condition using if/else
    if user_guess == CORRECT_NUMBER:
        # If the guess is correct, this message is printed.
        print("Correct! You guessed it 🎯")
        # The loop condition (user_guess != CORRECT_NUMBER) is now False, 
        # so the loop will automatically stop after this iteration.
        
    else:
        # If the guess is incorrect, this message is printed.
        print("Try again! 😔")

print("Game Over.")
