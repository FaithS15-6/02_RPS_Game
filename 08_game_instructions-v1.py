# Function go here...
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
    print("**** How to play ****")
    print()
    print("In this game, you can select among rock, paper or scissors inrder to beat the computer's random selections. it is just like playing rock, paper scissors, in real life but this time you're playing against a computer.")
    print("To play with rock put 'r' or 'rock, scissors is 's' or 'scissors and paper is 'p' or 'paper'")
    print()
    print("****GAME RULES****")
    print()
    print("Rock beats scissors")
    print("Scissors beats paper")
    print("paper beats rock")

    return ""

# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print("program Continues")
