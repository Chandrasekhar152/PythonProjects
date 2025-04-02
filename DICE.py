import random
while True:
    print("DO YOU WANT TO ROLL THE DICE? (Y/N)")
    if input().upper()=="Y":  
        a=random.randint(1,6)
        b=random.randint(1,6)
        print(f"your roll is {a} and {b} total {a+b}")
    else:
        print("Invalid input")
    