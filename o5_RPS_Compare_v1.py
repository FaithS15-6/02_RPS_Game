# RPS Component 3 - Compare user choice and computer choice
rps_list = ["rock  ", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1


        result = ""

        # compare options

        if comp_choice == user_choice:
            result = "tie"
        elif comp_choice == "rock" and user_choice == "paper":
            result = "Win"
        if comp_choice == "paper" and user_choice == "rock":
            result = "loose"

        print("User: {} vs Computer: {} - {}".format(user_choice, comp_choice, result))

        comp_index += 1

    