import random

user_wins=0
pc_wins=0

choices = ["rock", "paper", "scissors"]

while True:
    user_input= input("Enter rock, paper or scissors and enter q to close the game. ").lower()
    pc_choice= random.randint(0,2)
    # print(pc_choice)
    pc_input = choices[pc_choice]

    if user_input not in choices:
        break

    elif user_input == "rock" and pc_input == "scissors":
        print(f"your input was {user_input} and pc's input was {pc_input}")
        print("You win.")
        user_wins += 1

    elif user_input == "paper" and pc_input == "rock":
        print(f"your input was {user_input} and pc's input was {pc_input}")
        print("You win.")
        user_wins += 1

    elif user_input == "scissors" and pc_input == "paper":
        print(f"your input was {user_input} and pc's input was {pc_input}")
        print("You win.")
        user_wins += 1

    else:
        print(f"your input was {user_input} and pc's input was {pc_input}")
        print("you lose.")
        pc_wins+=1


print("Exiting the game.")
print(f"your score was " , user_wins)
print(f"pc score was " , pc_wins)