import random

snake = [[17, 7], [62, 19], [54, 34], [64, 60], [87, 36], [93, 73], [95, 36], [98, 79]]
ladder = [[1, 38], [4, 14], [9, 31], [28, 84], [21, 42], [51, 67], [72, 91], [80, 99]]
player_name_score = []

try:
    no_players = int(input("Enter No of Players: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

for i in range(1, no_players + 1):
    name = input(f"Enter name of player {i}: ")
    player_name_score.append([name, 0])

while True:
    for j in range(no_players):
        input(f"{player_name_score[j][0]}'s Turn: Press Enter to roll the dice")
        move = random.randint(1, 6)
        print("Dice showed number:", move)
        player_name_score[j][1] += move

        for k in range(len(snake)):
            if player_name_score[j][1] == snake[k][0]:
                print("Oh no! You got bitten...")
                player_name_score[j][1] = snake[k][1]

        for k in range(len(ladder)):
            if player_name_score[j][1] == ladder[k][0]:
                print("Wow! You got a ladder...")
                player_name_score[j][1] = ladder[k][1]

        print(f"Current Score of {player_name_score[j][0]}: {player_name_score[j][1]}")
        print(" ")

        
        if player_name_score[j][1] >= 100:
            print(f"{player_name_score[j][0]} Won!")
            exit()