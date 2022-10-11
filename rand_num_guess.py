#!/usr/bin/env python3
# Created By: Minab Berhane
# Date: Oct 09, 2022
# This program guesses a random number between 0-9
import random


def main():
    # introduce the purpose for this code
    print("welcome to my number guessing game")
    print("you will be guessing a number between 0 to 9")
    user_input = int(input("please input a number: "))

    # a number between 0 and 9
    random_variable = random.randint(0, 9)
    if user_input == random_variable:
        print("congratulation")
    else:
        print("sorry, your guess was {} you got that wrong the right answer is {}".format(user_input, random_variable))


if __name__ == "__main__":
    main()
