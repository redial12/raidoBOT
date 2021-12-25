# python number guessing game


import random
import time


# make a start to begin function

beginGame = str(input("Welcome to my Python Number Guessing Game! Hit Enter to begin. "))


def number_game():
    x = random.randint(1, 100)

    # make it so program doesn't crash on incorrect input
    # ask user if they would like to play again (DONE)
    # create a maximum of 10 guesses before game ends (DONE)
    # print number of guesses remaining (DONE)
    # don't allow user to guess same number twice (DONE)
    # don't allow user to guess greater than 100, a decimal/fraction, or less than zero (2/3 DONE)
    # change 1 and 100 to the highest and lowest possible values (DONE)
    # fix play again function (TEMP FIX)
    guess_list = []
    guess = int(input("Guess a number between 1 and 100. "))
    guess_count = 1
    highest = 100
    lowest = 1
    while guess != x and guess_count < 10:
        if guess in guess_list:
            print("You have already guessed " + str(guess) + "!")
        else:
            if x < guess <= 100:
                print("High.")
                if guess <= highest:
                    highest = guess
            elif x < guess:
                print("Number cannot be greater than 100!")
            if 1 <= guess < x:
                print("Low.")
                if lowest <= guess:
                    lowest = guess
            elif guess < x:
                print("Number cannot be less than 1!")
        time.sleep(1)
        print("You have " + str(10 - guess_count) + " guesses remaining.")
        time.sleep(1)
        guess_list.append(guess)
        guess = int(input("Guess a number between " + str(lowest) + " and " + str(highest) + ". "))
        guess_count += 1

    if guess == x:
        print("Correct! The number was " + str(x) + ".")
    else:
        print("Game over. The number was " + str(x) + ".")
    guess_list.append(guess)
    print("You guessed the numbers: " + str(guess_list))


if beginGame == "":
    print("You have 10 guesses to find the number I am thinking of...")
    time.sleep(2)
    play_again = "Y"
    while 1 == 1:
        number_game()
        if str(input("Would you like to play my game again (Y/N)? ")) == "N" or "n":
            break

    print("Goodbye!")
