
'''
link used to copy the special characters from the prints

#https://textkool.com/en/ascii-art-generator?hl=controlled%20smushing&vl=default&font=Pagga&text=papel

'''


import time
import random

#-----------------------------------------------------------------------------------------------------

#VARIABLES

print_STONE = ("░█▀▀░▀█▀░█▀█░█▀█░█▀▀\n░▀▀█░░█░░█░█░█░█░█▀▀\n░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀▀")

print_PAPER = ("░█▀█░█▀█░█▀█░█▀▀░█▀▄\n░█▀▀░█▀█░█▀▀░█▀▀░█▀▄\n░▀░░░▀░▀░▀░░░▀▀▀░▀░▀")

print_SCISSOR = ("░█▀▀░█▀▀░▀█▀░█▀▀░█▀▀░█▀█░█▀▄\n░▀▀█░█░░░░█░░▀▀█░▀▀█░█░█░█▀▄\n░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀\n")

print_victory = ("┈┈┈┈╭╮╭╮\n┈┈┈┈┃┃┃┃\n┈┈┈┈┃┃┃┃\n┈┈┈┈┃┗┛┣┳╮\n┈┈┈╭┻━━┓┃┃\n┈┈┈┃╲┏━╯┻┫\n┈┈┈╰╮╯┊┊╭╯\n")

print_lose = ("──▒▒▒▒▒────▄████▄─────\n─▒─▄▒─▄▒──███▄█▀──────\n─▒▒▒▒▒▒▒─▐████──█──█──\n─▒▒▒▒▒▒▒──█████▄──────\n─▒─▒─▒─▒───▀████▀─────\n")

#----------------------------------------------------------------

bot_choice_list = ['STONE', 'PAPER', 'SCISSOR']
player_name = ""
player_victory = []
bot_victory = []
draw = []


def score_game():
    sum_player_victory = sum(player_victory)
    sum_bot_victory = sum(bot_victory)
    sum_draw = sum(draw)
    print('########  SCORE ########')
    print(f'YOU  - {sum_player_victory}')
    print(f'BOT  - {sum_bot_victory}')
    print(f'DRAW - {sum_draw}')
    print('########  SCORE ########')

def preparation_of_the_game():

    print('░▀▀█░█▀█░█░█░█▀▀░█▀█░█▀█░█▀█░░░▀█▀░█▀▀░█▀▄░█▄█░▀█▀░█▀█░█▀█░█░░\n░░░█░█░█░█▀▄░█▀▀░█░█░█▀▀░█░█░░░░█░░█▀▀░█▀▄░█░█░░█░░█░█░█▀█░█░░\n░▀▀░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░░░▀▀▀░░░░▀░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀▀\n')

    global player_name # Here i call the empty global variable, but below i change it

    player_name = input("██████████ ENTER YOUR NAME TO START THE GAME ██████████\n██████████ PLAYER NAME:")

    time.sleep(1)

    print("\nSTARTING THE GAME...")
    time.sleep(2)

    print(f'┌─────       ─────┐\n > WELCOME, {player_name} <\n└─────       ─────┘')

    print("LET'S GO!\n")
    time.sleep(3)

    print("██████████ A BOT ENTERED THE GAME TOO  ██████████\n")
    time.sleep(3)

def running_the_game():

    while True:
        print("-" *  87)
        user_choice = input(" >>>>> TYPE STONE, PAPER or SCISSOR. TO EXIT PRESS 'CTRL + C': ").upper()
        print("-" *  87)
        bot_choice = random.choice(bot_choice_list).upper()

        if user_choice not in bot_choice_list:
            print(" ***** Please, type a valid option ***** ")
            time.sleep(2)
            return True

        if user_choice == 'STONE':
            print(f'\n██████████ YOUR MOVE, {player_name} ██████████ \n')
            print(print_STONE)

        elif user_choice == 'PAPER':
            print(f'\n██████████ YOUR MOVE, {player_name} ██████████\n')
            print(print_PAPER)

        elif user_choice == 'SCISSOR':
            print(f'\n██████████ YOUR MOVE, {player_name} ██████████\n')
            print(print_SCISSOR)

# -------------------------------------------------------------------
        if bot_choice == 'STONE':
            print('\n██████████ BOT MOVE ██████████\n')
            print(print_STONE)

        if bot_choice == 'PAPER':
            print('\n██████████ BOT MOVE ██████████\n')
            print(print_PAPER)

        if bot_choice == 'SCISSOR':
            print('\n██████████ BOT MOVE ██████████\n')
            print(print_SCISSOR)

# --------------------------------------------------------------------

        if user_choice == 'STONE' and bot_choice == 'STONE':
            print('\n██████████ MATCH RESULT ██████████\n')
            print(f'┌─────       ─────┐\n     > DRAW <\n└─────       ─────┘')
            draw.append(1)
            
        elif user_choice == 'PAPER' and bot_choice == 'PAPER':
            print('\n██████████ MATCH RESULT ██████████\n')
            print(f'┌─────       ─────┐\n     > DRAW <\n└─────       ─────┘')
            draw.append(1)

        elif user_choice == 'SCISSOR' and bot_choice == 'SCISSOR':
            print('\n██████████ MATCH RESULT ██████████\n')
            print(f'┌─────       ─────┐\n     > DRAW <\n└─────       ─────┘')
            draw.append(1)

        elif user_choice == 'STONE' and bot_choice == 'SCISSOR':
            print('\n██████████ MATCH RESULT ██████████\n')
            print(print_victory)
            print(f'┌─────                 ─────┐\n > YOU WIN, {player_name}. CONGRATULATIONS!! <\n└─────                 ─────┘')
            player_victory.append(1)


        elif user_choice == 'PAPER' and bot_choice == 'STONE':
            print('\n██████████ MATCH RESULT ██████████\n')
            print(print_victory)
            print(f'┌─────                 ─────┐\n > YOU WIN, {player_name}. CONGRATULATIONS!! <\n└─────                 ─────┘')
            player_victory.append(1)
                      

        elif user_choice == 'SCISSOR' and bot_choice == 'PAPER':
            print('\n██████████ MATCH RESULT ██████████\n')
            print(print_victory)
            print(f'┌─────                 ─────┐\n > YOU WIN, {player_name}. CONGRATULATIONS!! <\n└─────                 ─────┘')
            player_victory.append(1)

        else:
            print('\n██████████ MATCH RESULT ██████████\n')
            print(print_lose)
            print(f'┌─────      ─────┐\n   > OPS, YOU LOSE, {player_name} <\n└─────      ─────┘')
            bot_victory.append(1)

        score_game()

# -------------------------------------------------------------------

preparation_of_the_game()
while True:
    running_the_game()

# -------------------------------------------------------------------

