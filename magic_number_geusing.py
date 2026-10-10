import random 
print("MAGIC NUMBER GUESSING GAME")
max_number = 100
secret_number = random.randint(1,max_number)
attempts = 0 
max_attempts = 10
print(f"You have to pick a secret number between 1 and {max_number} ")
print(f"You have {max_attempts} attempts to guess it.")
while attempts < max_attempts:
    attempts_left = max_attempts - attempts
    print(f"attempts left: {attempts_left}")
    guess = int(input("enter your guess."))
    attempts += 1
    if guess == secret_number:
        print("congratulations you won.")
        print(f"you guessed {secret_number} in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("go higher")
    else:
        print("go lower")
    if attempts == 5 and guess != secret_number:
        if secret_number % 2 == 0:
            print("The number is an even number")
        else:
            print("The number is an odd number")

if guess != secret_number:
    print(f"Game over the secret number was {secret_number} better luck next time.")
print("Thanks for playing.")
    
    
