# NUMBER-GUESSER

import random

num = random.randint(1,100)

tries = 0
while True:
    user_input = int(input("enter your number between 1-100 "))
    tries+=1

    if user_input==num:
        print("congratulations you guessed the correct number in",tries)
        break
    elif user_input>num:
        print("you are guessing a little higher")    
    elif user_input<num:
        print("you are guessing a little lower")    

