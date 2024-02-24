import random
import sys
from random import randint
def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius! babe')
            return True

    else:
        print('hey idiot, i said 1 to 10 ')
        return False

if __name__ == '__main__':
    answer = random.randint(1,10)



    while True:
        try:

            guess = int(input("guess a number 1 to 10\n"))
            if (run_guess(guess,answer)):
                print(f" obrigado por jogar")


        except ValueError:
            print('please enter a number')
        continue

