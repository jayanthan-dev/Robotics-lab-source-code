import random

# Step 1: Generate a random number between 1 and 100
target_number = random.randint(1, 100)

# Step 2: Prompt user repeatedly until the correct guess
print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100:")

while True:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess == target_number:
            print("🎉 Correct Guess! You Win!")
            break
        elif guess > target_number:
            print("Too High. Try again.")
        else:
            print("Too Low. Try again.")
    except ValueError:
        print("Please enter a valid number.")
