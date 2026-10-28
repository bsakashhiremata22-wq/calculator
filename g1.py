import random

print("\n-------->>>   Welcome to the Number Guessing Game!    <<<--------\n")

number = random.randint(1, 100)
attempts = 0

while True:
    
    print(f"You have total {10 - attempts} attempts to guess the number.")

    try:
        guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid integer!\n")
        continue

    if guess<1 or guess>100:
        print(f'Your guess {guess} is invalid\n')
        continue
    
    attempts += 1

    if attempts == 10 :
            print("\nSorry, you've used all your attempts. The number was:", number)
            break
    
    if guess < number:
        print("Too low! Try a bigger number.\n")

    elif guess > number:
        print("Too high! Try a smaller number.\n")


    else:
        print("\nCongratulations! You guessed correctly.")
        print("The number was:", number)
        print("Attempts taken:", attempts)
        break