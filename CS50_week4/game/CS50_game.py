import random  # albo from random import randint

while True:
    try:
        n = int(input("Level: "))
        number = random.randint(1, n)
        print(number)
        break
    except ValueError:
        continue

while True:
    try:
        guess = int(input("Guess: "))
        if guess == number:
            print("Just Right!")
            break
        elif guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")

    except ValueError:
        continue
