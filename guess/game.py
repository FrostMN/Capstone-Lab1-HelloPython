from random import randint
import guess.valid as valid


class Game:

    limit = int

    def __init__(self, limit=100):
        self.limit = limit

    def run(self):

        choice = -1

        while not valid.menu_choice(choice):
            if choice == 3:
                return 0
            menu_string = \
                "Guess the Number: \n" \
                "\t1 - Guess The Computers Number\n" \
                "\t2 - The Computers Guess Your Number\n" \
                "\t3 - Quit\n"

            print(menu_string)
            choice = input("What would you like to do?\n")

        choice = int(choice)

        if choice == 1:
            self.guess_computers_number()
        if choice == 2:
            self.computer_guesses_number()
        if choice == 3:
            print("guit")

    def guess_computers_number(self):
        min_number = 1
        max_number = self.limit
        number = randint(min_number, max_number)
        guessed = False
        guesses = 0
        while not guessed:
            print("Please guess a number between " + str(min_number) + " and " + str(max_number) + ".")
            guess = input("Your guess: ")
            guesses += 1

            if valid.guess(guess):
                guess = int(guess)
                if number == guess:
                    guessed = True
                if number < guess:
                    print("you need to guess lower!")
                if number > guess:
                    print("you need to guess higher!")
            else:
                print("Please enter a valid number between " + str(min_number) + " and " + str(max_number) + ".")
        print("your guess of " + str(number) + " was correct!")
        print("you guessed it in only " + str(guesses) + " guesses!")

    def computer_guesses_number(self):
        guessed = False
        guesses = 1
        lower_limit = 0
        upper_limit = 100
        print("think of a number between 1 and 100 (inclusive).")
        input("hit enter when ready.")
        guess = self.first_guess()
        while not guessed:
            answer = self.guess_correct(guess)
            if answer == 1:
                print("I guessed your number: " + str(guess))
                print("in only " + str(guesses) + " guesses!")
                return 0
            guess, lower_limit, upper_limit = self.guess_number(answer, guess, lower_limit, upper_limit)
            guesses += 1
            if lower_limit == upper_limit:
                print("I think you fibbed to me,")
                print("if you're not gonna play fair I quit")
                return 0

    # picks a number between 45 and 55 for computers first guess
    def first_guess(self):
        return 45 + randint(0, 10)

    # asks if the guess was correct
    def guess_correct(self, guess):
        choice = -1
        while not valid.menu_choice(choice):
            print("is your number " + str(guess) + "?\n\t1 - yes\n\t2 - too low\n\t3 - too high")
            choice = input("please input number: ")
        choice = int(choice)
        return choice

    # does a version of binary search to guess the players number
    # returns a 3 filed tuple that gets unpacked into vars the game uses
    def guess_number(self, answer, guess, lower, upper):
        if answer == 2:
            new_guess = guess + (upper - guess) // 2
            print(guess)
            return new_guess, guess, upper
        else:
            new_guess = lower + (guess - lower) // 2
            return new_guess, lower, guess
