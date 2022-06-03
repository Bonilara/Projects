import math
import random
import sys

n = 0
user_count = 0
com_count = 0
def check(c):
    # checks for the input value three times before ending game or moving on
    for t in range(3):
        if t != 0:
            c = int(input('Try again, Enter a number between 1 and 20:'))
        if c < 0 or c > 20:
            print('invalid input!')

        else:
            return c
    print('Game over!')
    sys.exit()









def guess(u_val):
    # compares random number to user input
    x = random.randint(1, 20)
    print(x)
    if x == u_val:
        print('Correct! You win!')
    else:
        for i in range(2):
            if i == 0:
                print('Wrong Guess! You have two more tries')
                n1 = check(int(input('Enter another number:')))
            if n1 == x:
                print('Correct! You win!')
                break
            elif i == 1:
                print('Wrong Guess! You have one more try')
                n2 = check(int(input('Enter another number:')))
                if n2 == x:
                    print('Correct! You win!')
                else:
                    print('You are out of guesses, You lose this round!')
                    break


def main():
    try:
        # catches exeption if any character other than a number is entered
        user_guess = int(input('Enter a number between 1 and 20:'))
        n = check(user_guess)
    except Exception:
        # Ends code if wrong input is entered
        print('Invalid input! You can only input a number')
        sys.exit()
    guess(n)
if __name__ == "__main__":
    main()


