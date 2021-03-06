import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an " \
                      "integer that is more than 0\n"

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

# List of valid responses

yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# if 'no', it should show instructions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    print()
    print("**** How to play ****")
    print()
    print("In this game, you can select among rock, paper or scissors inrder to beat the computer's random selections. it is just like playing rock, paper scissors, in real life but this time you're playing against a computer.\n")
    print("To play with rock put 'r' or 'rock, scissors is 's' or 'scissors and paper is 'p' or 'paper'  or if you want to quit, you can type in 'xxx'.")
    print()
    print("****GAME RULES****")
    print()
    print("Rock beats scissors")
    print("Scissors beats paper")
    print("paper beats rock")
    print()
    print("Bonne Chance!!!")

    return ""

# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()


# Ask user for number of rounds then loop...
rounds_played = 0
rounds_lost = 0
rounds_won = 0
rounds_drawn = 0

game_summary = []

chose_instructions = "Please chose rock (r), paper (p), or scissors (s)"

# Ask user for number of round. <enter> for infinite mode
rounds = check_rounds()


end_game = "no"
while end_game == "no":

# loops while rounds played is less than rounds requested

    # Start of game Play Loop
    rounds_played += 1

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continues Mode: Round {}".format(rounds_played)
  
    else:
        heading = "Round {} of Round {}".format(rounds_played, rounds)

    print(heading)

  # Gets the computer shouce
    comp_choice = random.choice(rps_list[:-1])
    print ("Comp Choice: ", comp_choice)

    chose = choice_checker("chose rock / paper / scissors (r/p/s): ", rps_list, "Please chose from rock, Paper / scissors (or xxx to quit).")
    print("you chose", chose)   
     

    # End game if exit code is typed
    if chose == "xxx":
        break

        # End game if round entered is finished

    # compare choices 
    # Compare options between computer choice and User choice 
    # Detemine wins and loss
    # if Choices are the same, it is a tie.

    if comp_choice == chose:
        result = "tie"
        rounds_drawn += 1
        # three ways to win...
    elif comp_choice == "rock" and chose == "paper":
        result = "!!win!!"
    elif comp_choice == "scissors" and chose == "rock":
        result = "!!win!!"
    elif comp_choice == "paper" and chose == "scissors":
        result = "!!win!!"

    # if you don't tie / win, you lose
    else:
        result = "lose"

    # output to user    
    print("User: {} vs Computer: {} - {}".format(chose, comp_choice, result))
    print()

    # add to game history
    outcome ="Round {}: {}".format(rounds_played, result)

    if result == "lost":
        rounds_lost += 1
    elif result == "tie":
        rounds_drawn += 1

    game_summary.append(outcome)



    if rounds!= "" and rounds_played >= rounds - 1:
        break

    # *** rest of loop / game ***
    print("You chose {}". format (chose))


# Ask user if they want to see their game history.
# if 'yes' show game history

# Show game statistics

# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# **** Calculate Game Stats ****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

print()
print("**** Game History ****")
for game in game_summary:
    print(game)

print()

# displays game stats with % values to the nearest whole number 
print("**** Game Statistics ******")
print("Win: {}, ({:.0f}%)\nLoss: {}, ({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_won,
                                                                          percent_win,
                                                                          rounds_lost,
                                                                          percent_lose,
                                                                          rounds_drawn,
                                                                          percent_tie))

# End of Game Statements
print()
print('****End Game Summary ****')
print("Won: {} \t|\t Lost: {} \t|\t Draw: {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing ")
