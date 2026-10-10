import random 
max_number = 1000
secert_number = random.randint(1,max_number)
max_attempts = 10
attempts = 0
print(f"you have to pick a secret number between 1 and { max_number}")
print(f"you have {max_attempts} attempts to guess the secret number")
while attempts < max_attempts:
    attempt_left = max_attempts - attempts
    print(f"Attempts left: {attempt_left}")
    guess = int(input("type your guess"))
    attempts += 1
    if guess == secert_number:
        print("congtatulation you won")
        print(F"The secret number was {secert_number}")
        break
    elif guess < secert_number:
        print("go higher")
    else:
        print("go lower")
    if attempts == 5 and guess !=  secert_number:
        if secert_number % 2 == 0:
            print("the secert number is an odd number")
        else:
            print("the secret number is an even number")
if guess != secert_number:
    print(f"Game over the secret number was {secert_number} better luck next time")
print("thaks for playing")