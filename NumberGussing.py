import random

Number=random.randint(1,100)
while True:
    print("GUESS THE NUMBER BETWEEN 1 AND 100")
    try:
        guess=int(input())
        if guess==Number:
            print("YOU GUESSED IT RIGHT")
            break
        elif guess >Number:
            print("TOO HIGH")
        elif guess < Number:
            print("TOO LOW")
        else:
            print("TRY AGAIN")
    except Exception as e:
        print("Please enter a valid number",e)