import random
from time import sleep

print('Welcome to the number guessing game!')
print('I am picking a number between 1 and 100...')
sleep(1.5)
correct_num = random.randint(1,100)

user_guess = int(input('Enter your guess: '))

num_of_guesses = 1

while user_guess != correct_num:
    sleep(1)
    num_of_guesses += 1
    if user_guess > correct_num:
        print('\nWrong! You need to guess lower...')
        #sleep(1)
        user_guess = int(input('Guess again: '))
    else:
        print('\nWrong! You need to guess higher...')
        #sleep(1)
        user_guess = int(input('Guess again: '))

sleep(0.5)
print(f'Your guess is Correct! The correct number is {correct_num}. Number of tries: {num_of_guesses}')

