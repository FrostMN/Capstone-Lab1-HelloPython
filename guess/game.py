from random import randint
import guess.valid as valid


class Game:

    limit = int

    def __init__(self, limit=10):
        self.limit = limit

    def run_game(self):

        choice = -1

        while not valid.menu_choice(choice):
            if choice == 3:
                return 0
            menu_string = \
                "Guess the Number: \n" \
                "  1 - Guess The Computers Number\n" \
                "  2 - The Computers Guess Your Number\n" \
                "  3 - Quit\n"

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
        min = 1
        max = 100
        number = randint(min, max)
        guessed = False
        guesses = 0
        while not guessed:
            print("Please guess a number between " + str(min) + " and " + str(max) + ".")
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
                print("Please enter a valid number between " + str(min) + " and " + str(max) + ".")
        print("your guess of " + str(number) + " was correct!")
        print("you guessed it in only " + str(guesses) + " guesses!")

    def computer_guesses_number(self):
        print("not yet implemented")
