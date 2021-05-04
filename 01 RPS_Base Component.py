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


# Functions go here
def choice_checker (question, options, error):

    valid = False
    while not valid :

        # Ask user for choice
        response = input(question).lower()

        for item in options:
            if response == item[0]:
                return item
            elif response == item:
                return item

        print(error)

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

# loops while rounds played is less than rounds requested
while end_game == "no":

    # Start of game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continues Mode: Round {}".format(rounds_played + 1)
  
    else:
        heading = "Round {} of Round {}".format(rounds_played + 1, rounds)

    print(heading)

    choose = choice_checker("choose rock / paper / scissors (r/p/s): ", rps_list, "Please choose from rock, Paper / scissors (or xxx to quit).")
    print("you choose", choose)   


    # get computer choice 
    comp_choice = random.choice(rps_list[:-1])
    print ("Comp Choice: ", comp_choice)
      

      # compare choices 

    # End game if exit code is typed
    if choose == "xxx":
        break

        # End game if round entered is finished

    if rounds!= "" and rounds_played >= rounds - 1:
        break

    # *** rest of loop / game ***
    print("You chose {}". format (choose))

    rounds_played += 1

# Ask user if they want to see their game history.
# if 'yes' show game history

# Show statistics
