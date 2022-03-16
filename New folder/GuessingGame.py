import random


def Guess():
    random_number = random.randint(1, 1000)
    guess = 0
    number_of_tries = 10
    print('Welcome to the Guessing Game!! You have ten guesses to get the hidden number, waste them not!\n'
          'May the odds be in your favor!')
    
    while number_of_tries != 0:
        guess = input("Enter your guess: ")
        while guess.isdigit() != True:
            guess = input("Enter your guess: ")
            
        number_of_tries -= 1
        guess = int(guess)
        
        if number_of_tries == 0 and guess != random_number:
            print('You guessed wrong, and you are out of guesses')
        elif guess < random_number:
            print(f'Shoot! Try again, your guess is a bit low, aim a bit higher. You have {number_of_tries} guesses left\n')
        elif guess > random_number:
            print(f'Try again, aim a little lower this time. You have {number_of_tries} guesses left\n')
        elif guess == random_number:
            print('Congrats! You guessed right!')
            return
    print('\nYou guessed wrong!!!\n'
          f'The number is {random_number}')

