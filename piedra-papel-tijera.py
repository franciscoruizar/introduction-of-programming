import random

rock = 1
paper = 2
scissors = 3

tries = 3
human_wins = 0
bot_wins = 0

for item in range(0, tries):
    print("==============================")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    human = int(input("Eligir opcion: "))
    print("==============================")

    bot = random.randint(1, 3)

    print("===================")
    print("Intento: ", item)
    print("Bot: ", bot)
    print("===================")

    if human == rock:
        if bot == paper:
            bot_wins += 1
        elif bot == scissors:
            human_wins += 1
    elif human == paper:
        if bot == rock:
            human_wins += 1
        elif bot == scissors:
            bot_wins += 1
    elif human == scissors:
        if bot == paper:
            human_wins += 1
        elif bot == rock:
            bot_wins += 1

if human_wins > bot_wins:
    print("Ha ganado!!")
elif human_wins < bot_wins:
    print("Ha perdido!!")
elif human_wins == bot_wins:
    print("Empate!!")
