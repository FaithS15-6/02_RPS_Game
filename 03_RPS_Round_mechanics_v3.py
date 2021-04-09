# Main routine more efficient than v2


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter>  \ or an integer that is more than zero"
        if response !="":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response

# Main Routine goes here...


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
        heading = "Continues Mode: \ Round {}".format(rounds_played + 1)

    else:
        heading = "Round {} of \ Round {}".format(rounds_played + 1, rounds)

    print(heading)
    choose = input("{} or 'xxx' to end: ".format(choose_instructions))

    # End game if exit code is typed
    if choose == "xxx":
        break
