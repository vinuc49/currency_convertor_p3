import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# constant to hold pixilated view of paper
PAPER = [
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
]

# constant to hold pixilated view of rock
ROCK = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
]

# constant to hold pixilated view of scissors
SCISSORS = [
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]


class Game:
    """
    A class to help encapsulate the Rock Paper Scissors Game
    ...
    Attributes
    ----------
    myName : str
        name of user playing the game, default is Player 1
    comp_wins : int
        reflects number of computer wins, default is 0
    player_wins : int
        reflects number of player wins, default is 0
    games_played : int
        reflects games played, default is 0
    user_choice : str
        reflects user's choice for a match, default is None, 'r', 'p', 's' are
        expected settings
    computer_option : str
        reflects computer's choice, default is None, 'r', 'p', 's' are expected
    Methods
    -------
    rules()
        Prints the rules of the game then takes user to first collection
        of input
    get_user_choice()
        Collects the user's choice for their turn of the game
    get_computer_option()
        Randomly sets the computer's choice for their turn of the game
    display_match_results()
        recaps the number of wins for player vs computer
    who_won()
        Displays pixelated output of computer then user and recaps the match
        results with a win, loss tie message.
    new_round()
        resets user_choice and comp_choice to None and starts the play method
    play_again()
        asks user if they want to play another round, starts the new round or
        quits the game
    play()
        gathers user's choice, sets computer's choice, calls who_won, displays
        results, calls, play_again
    """

    def __init__(self, myName="Player 1", comp_wins=0, player_wins=0, games_played=0):  # noqa
        """
                Parameters
                ----------
                myName : str, optional
                    The name of the users (default is 'Player 1')
                comp_wins : int, optional
                    The number of computer wins for this player (default is 0)
                player_wins : int, optional
                    The number of players wins for this game  (default is 0)
                games_played : int, optional
                    The number of matches played for this game for this user
                    (default is 0)
                """
        self.myName = myName
        if len(self.myName) < 1:
            self.myName = "Player 1"
        self.comp_wins = comp_wins
        self.player_wins = player_wins
        self.games_played = games_played
        self.user_choice = None
        self.computer_option = None

    def rules(self):
        """
        Prints the rules of the game.
        Calls Play Game.
        """
        print(Fore.MAGENTA + Back.WHITE + "Game Rules")
        print("Enter 'R' for Rock")
        print("Enter 'P' for Paper")
        print("Enter 'S' for Scissors")
        print("If preferred, you can type the full word.")
        print("Rock beats Scissors")
        print("Scissors beats Paper")
        print("Paper beats Rock\n")
        print(Fore.MAGENTA + Back.WHITE + "Now it's time to play!")
        self.play()

    def get_user_choice(self):
        """
        Asks user for their choice.
        Transforms input to lower case
        Strips leading and trailing whitespace
        Accepts rock and r for rock and sets user_choice to r
        Accepts scissors s for scissors and sets user_choice to s
        Accepts paper and p for paper and sts user_choice to p
        Otherwise prompts for input until valid
        """
        user_choice = input(
            "Choose Rock, Paper or Scissors: \n \t r: rock \n \t p: paper \n \t s: scissors \n").lower().strip()  # noqa
        if user_choice in ["rock", "r"]:
            self.user_choice = "r"
        elif user_choice in ["paper", "p"]:
            self.user_choice = "p"
        elif user_choice in ["scissors", "s"]:
            self.user_choice = "s"
        else:
            print(
               Fore.RED + "Uh Oh, I don't think you've played this game before. Please try again.")  # noqa

    def get_computer_option(self):
        """
        randomly gets an integer between 1 and 3
        if 1, sets comp_choice to r
        if 2, sets comp_choice to p
        """
        computer_option = random.randint(1, 3)
        if computer_option == 1:
            self.computer_option = "r"
        elif computer_option == 2:
            self.computer_option = "p"
        else:
            self.computer_option = "s"

    def display_match_results(self):
        """
        Displays match results.
        Adds match results.
        """
        print("")
        print(Fore.YELLOW + "Player wins: " + str(self.player_wins))
        print(Fore.BLUE + "Computer wins: " + str(self.comp_wins))
        print("")

    def who_won(self):
        """
        Calls constant for pixalated views.
        Prints win / lose message.
        """
        print("COMPUTER             " + self.myName.upper())
        comp_symbol = ROCK
        if self.computer_option == "p":
            comp_symbol = PAPER
        elif self.computer_option == "s":
            comp_symbol = SCISSORS
        user_symbol = ROCK
        if self.user_choice == "p":
            user_symbol = PAPER
        elif self.user_choice == "s":
            user_symbol = SCISSORS
        for num, line in enumerate(comp_symbol):
            print(line + "    " + user_symbol[num])

        self.games_played += 1
        if self.user_choice == "r":
            if self.computer_option == "r":
                print(
                    Fore.YELLOW + "You chose rock. The computer chose rock too. Congrats, you tied.")  # noqa

            elif self.computer_option == "p":
                print(Fore.RED + "You chose rock. The computer chose paper. Oh no, you lose.")  # noqa
                self.comp_wins += 1

            elif self.computer_option == "s":
                print(Fore.GREEN + "You chose rock. The computer chose scissors. Woo hoo!! You win!")  # noqa
                self.player_wins += 1

        elif self.user_choice == "p":

            if self.computer_option == "r":
                print(
                    Fore.GREEN + "You chose paper. The computer chose rock. Woo hoo!! You win!.")  # noqa
                self.player_wins += 1

            elif self.computer_option == "p":
                print(
                    Fore.YELLOW + "You chose paper. The computer chose paper too. Congrats, you tied.")  # noqa

            elif self.computer_option == "s":
                print(
                    Fore.RED + "You chose paper. The computer chose scissors. Oh no, you lose.")  # noqa
                self.comp_wins += 1

        elif self.user_choice == "s":

            if self.computer_option == "r":
                print(
                    Fore.RED + "You chose scissors. The computer chose rock. Oh no, you lose.")  # noqa
                self.comp_wins += 1

            elif self.computer_option == "p":
                print(
                    Fore.GREEN + "You chose scissors. The computer chose paper. Woo hoo!! You win!.")  # noqa
                self.player_wins += 1

            elif self.computer_option == "s":
                print(
                   Fore.YELLOW + "You chose scissors. The computer chose scissors too. Congrats, you tied.")  # noqa

    def new_round(self):
        """
        Resets user choice to none.
        Resets computer to none.
        Calls play to restart.
        """
        self.user_choice = None
        self.computer_option = None
        self.play()

    def play_again(self):
        """
        Gives you option of playing again
        Calls New Round if yes chosen.
        If no chosen prints goodbye message.
        Displays final scores.
        """
        user_choice = input(
            "Do you want to play again? \n \t y: yes \n \t  n: no \n").lower().strip()  # noqa
        if user_choice in ["y", "yes"]:
            self.new_round()
        elif user_choice in ["n", "no"]:

            print("Goodbye " + self.myName + "!\n")
            print(Fore.MAGENTA + Back.WHITE + "Final Score")
            self.display_match_results()
            return False
        else:
            print("invalid_input")
            self.play_again()

    def play(self):
        """
        Calls user choice.
        Calls computer choice.
        Calls user options & messages.
        Calls score tracker.
        Calls play again option.
        """
        self.get_user_choice()
        self.get_computer_option()
        self.who_won()
        self.display_match_results()
        self.play_again()


def main():
    """
    Prints welcome messgae and requests name.
    Prompts rule option and calls rules.
    Calls the game play option.
    Prints error message if wrong option is chosen.
    """
    print("Hello! What is your username?")
    myName = input().strip()

    game = Game(myName)
    print(Fore.YELLOW + "Hello, " + game.myName)
    print("If this is your first time here, please check out our rules.")
    while True:
        user_choice = input(
            "Type 'Start' To Begin or Type 'Help' For The Rules.\n \t s: start \n \t h: help\n").lower().strip()  # noqa
        if user_choice in ["help", "h"]:
            return game.rules()

        elif user_choice in ["start", "s", "y", "yes"]:
            return game.play()
        else:
            print(Fore.RED + "Uh Oh, I don't think you've played this game before. Please try again.")  # noqa


# if __name__ == 'main':
#     main()
main()