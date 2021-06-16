import time
import random

from phrasehunter.phrase import Phrase


class Game:
    def __init__(self):
        self.active_phrase = None
        self.missed = 0
        self.phrases = [
            "Knowledge is power",
            "Whatever you do do it well",
            "What we think we become",
            "Turn your wounds into wisdom",
            "And still I rise"
        ]
        self.guesses = []

    def start(self):
        self.welcome()
        self.active_phrase = Phrase(self.get_random_phrase())
        while self.missed < 5:
            if not self.active_phrase.check_complete():
                self.active_phrase.display()
                user_guess = self.get_guess()
                if self.active_phrase.check_letter(user_guess):
                    print("Great! {} was correct".format(user_guess))
                else:
                    print("Oops! {} is not in the phrase. {} out of 5 lives remaining!".format(user_guess, 4-self.missed))
                    self.missed += 1
                print()
            else:
                break
        self.game_over()

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("└[∵┌]└[ ∵ ]┘[┐∵]┘")
        print("Welcome to Phrase Hunter!")
        time.sleep(0.5)
        print("You'll get a random phrase from a pool of {}".format(len(self.phrases)))
        time.sleep(0.5)
        print("Guess individual letters that make up the phrase")
        time.sleep(0.5)
        print("Ready? Let's go!")
        time.sleep(1)

    def get_guess(self):
        user_guess = (input("Guess a letter: ")).lower()
        #  add validation here later
        self.guesses.append(user_guess)
        return user_guess

    def game_over(self):
        if self.missed < 5:
            print("Well done! You guessed the phrase: {}".format(self.active_phrase.phrase))
        else:
            print("You guessed incorrect 5 times. Game over!")
            print("The phrase was: {}".format(self.active_phrase.phrase))
        print("Thanks for playing. See you next time!")
        print("└[∵┌]└[ ∵ ]┘[┐∵]┘")