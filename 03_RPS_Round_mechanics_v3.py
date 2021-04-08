# Functions used to check input is valid


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

round_played = 0
choose_instructions = "Please choose rock (r), paper (p), or scissors (s)"

# ask user for number of round. <enter> for infinite mode
rounds = check_rounds()

end_game = "no
while end_game == "no":
