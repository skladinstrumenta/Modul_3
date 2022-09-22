"""This module collects all settings and constants of game
"""
from pickle import TRUE
from game_exceptions import ExitGame

# Lives of Player
PL_LIVES = 5
# game difficulty factor
HARD = 5

def validator_input(name):
    """checking for the correctness of entering commands, \
    in case of an incorrect command name, an input error message is displayed, \
    and we ask you to repeat the input \
        str: START
    """
    print(f"Welcome {name.title()} to the game!")
    valid = True
    while valid:
        start_str = input("\nPlease enter 'START', 'EXIT' or 'HELP'____:  ").lower()
        if start_str == "start":
            valid = False
            return "start"
        elif start_str == "exit":
            valid = False
            raise ExitGame
        elif start_str == "help":
            print(command_help())
        else:
            print("Wrong command entered, to see a list of commands, type 'HELP'")

def command_help():
    """helper function to list commands
    """
    print("""
command 'START' - start to play the game
command 'EXIT' - Exit from game
command 'HELP' - information about commands""")

def valid_input_value():
    """Сhecking for the correctness of entering a number. \
    Returns:
        int: digit 1, 2 or 3
    """
    valid = True
    while valid:
        try:
            numb = int(input("enter WIZARD (1), WARRIOR (2) or ROGUE (3):  "))
        except ValueError:
            print("The input must be a digit! Сan be re-entered")
            continue
        if numb in [1, 2, 3]:
            valid = False
            return numb
        else:
            print("Value does not satisfy input requirements. Try entering again")

def validator_mode():
    """checking for the correctness of entering the letter \
    The input must only either N or H\
    """
    valid = TRUE
    while valid:
        mode = input("\nWhat mode do you want to play in: \
Normal(N) or Hard(H)\n\
Enter mode 'N' or 'H':   ").upper()
        if mode in ["N", "H"]:
            valid = False
            return mode
        else:
            print("Invalid input, please try again!")
