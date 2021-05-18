# checks that users answer yes / no to a question
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


#  Shows instructions on how to play (returns "")
def instructions():
    print("**** How to play ****")
    print("The instructions to this game are very easy. ")
  
    print("GOOD LUCK! & *HAVE FUN*...")
    return ""
 