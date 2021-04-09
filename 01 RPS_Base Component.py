import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an " \
                      "integer that is morethan 0\n"

        # If infinite mode not chosen, check response
        # Is an interger that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to start of loop

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response

# Main routine goes here

# List of valid responses


yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# if 'yes', show instructions


# ask user for # of rounds then loop...


# Ask user if they want to see their game history.
# if 'yes' show game history

# Show statistics

