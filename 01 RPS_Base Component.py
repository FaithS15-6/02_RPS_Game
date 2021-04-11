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
rounds_played = 0
choose_instructions = "Please choose rock (r), paper (p), or scissors (s)"

# Ask user for number of round. <enter> for infinite mode
rounds = check_rounds()


end_game = "no"
while end_game == "no":

    # Start of game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continues Mode: Round {}".format(rounds_played + 1)

    else:
        heading = "Round {} of Round {}".format(rounds_played + 1, rounds)

    print(heading)
    choose = input("{} or 'xxx' to end: ".format(choose_instructions))

    # End game if exit code is typed
    if choose == "xxx":
        break


    # Ask user choice and check it's valid
    choose = choice_checker("choose rock / paper / scossors"
                            "(r/p/s:", rps_list)
# Ask user if they want to see their game history.
# if 'yes' show game history

# Show statistics
