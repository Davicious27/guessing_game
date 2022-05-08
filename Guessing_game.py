#Import random module for number to guess, and time, for sleep function
from time import sleep
import random

# User input for name

user_name = input("Enter you name, or nickname: ")
#Instructions, and initial message


welcome_msg = """Hi there! """ + user_name + """. Let's play a guessing game.
                 
                 Enter '5' guesses between 1, and 100.
                 If you guess correctly, you win!!!."""


game_rules = """
                Now, the rules of the game: 

                1. You can enter one guess at a time.
                2. You can only enter numbers between '1', and '100'.
                    - If you enter a number outside of the range,
                    you will see an 'OUT OF BOUNDS!' message once
                    the game validates your entrie.
                3. If the difference between your guess, and the 
                   number to gues is > '10', you will see a
                   'WARM' message to the side of the number.
                4. If the difference between your guess, and the 
                   number to gues is < '10', you will see a
                   'COLD' message to the side of the number.
                5. If none of your guesses matches the number to
                   guess, you will lose.
                6. Type Validate to see the number to guess if you lost.
                """


# Generate random number

rand_number = random.randint(1,100)

#Testing purposes only, remove later when playing: 

print(rand_number)

# Start of the game: 
sleep(1)
print(welcome_msg)
sleep(1)
print(game_rules)
sleep(3)


#Game logic: 
i = 5

while i > 0 :
    user_guess = int(input("Enter your guess " + str(i) + " attempts remaining: "))
    absolute_diff = abs(rand_number - user_guess)
    if user_guess == rand_number:
        print("You won!!! The number was " + str(user_guess) + " !!!")
        break
    elif (user_guess < 1) or (user_guess > 100):
        print(str(user_guess) + " OUT OF BOUNDS")
        i = i-1
        continue
    elif absolute_diff > 10:
        print("COLD")
        i = i-1
        continue
    elif absolute_diff <= 10:
        print("WARM")
        i = i-1
        continue