import random
options = ["r", "p", "s"]
computer_choice = random.choice(options)
player_choice = input("What do you play? Rock, Paper or Scissors? ").lower()[0]

def respell_choice(option):
    if option == "r":
        return "Rock"
    elif option == "p":
        return "Paper"
    elif option == "s":
        return "Scissors"

print(f"Your choice: {respell_choice(player_choice)}")
print(f"Computer's choice: {respell_choice(computer_choice)}")
player_dict = {
    "computer": respell_choice(computer_choice),
    "player": respell_choice(player_choice)
}
def win_checker(players_dict):
    response = "Draw"
    choice_list = []
    for player in players_dict:
        choice_list.append(players_dict[player])
        if "Paper" in choice_list and "Scissors" in choice_list:
            response = "Scissors"
        elif "Paper" in choice_list and "Rock" in choice_list:
            response = "Paper"
        elif "Scissors" in choice_list and "Rock" in choice_list:
            response = "Rock"

    if response != "Draw":
        for player in players_dict:
            if players_dict[player] == response:
                print(f"{player} wins")
    elif response == "Draw":
        print("Draw")


win_checker(player_dict)











