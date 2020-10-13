import random
from random import choice
from Game import bot_board_1,my_board,bot_board_2
from user_choice_ships import slov
list_del_1 = []
def rep_func(func):
    func(input())
def rep_func_nostr(func):
    func()
def us_choice_str(us_string):

    for i in range(len(us_string)):
        if us_string[i] in slov:
            num_s_1 = slov[us_string[i]]

    num =  ["1","2","3","4","5","6","7","8","9","10"]
    for i in (num):
        if us_string.find("{}".format(i)) != -1:
            num_s_2 = int(i)
    if "10" in us_string:
        num_s_2 = 10
    if bot_board_1[num_s_2-1][num_s_1] != "X":
            if bot_board_1[num_s_2-1][num_s_1] == 0:
                bot_board_2[num_s_2-1][num_s_1] = "X"
                bot_board_1[num_s_2-1][num_s_1] = "X"
                list_del_1.append([num_s_2-1,num_s_1])
                print("Промах....")
                us_step = False
            if bot_board_1[num_s_2-1][num_s_1] == 1:
                bot_board_2[num_s_2-1][num_s_1] = "X"
                bot_board_1[num_s_2-1][num_s_1] = "X"
                list_del_1.append([num_s_2-1,num_s_1])
                print("Попал!!!")
                rep_func(us_choice_str)
                us_step = False
            if bot_board_1[num_s_2-1][num_s_1] == 2:
                bot_board_2[num_s_2-1][num_s_1] = "X"
                bot_board_1[num_s_2-1][num_s_1] = "X"
                list_del_1.append([num_s_2-1,num_s_1])
                print("Попал!!!")
                rep_func(us_choice_str)
                us_step = False
            if bot_board_1[num_s_2-1][num_s_1] == 3:
                bot_board_2[num_s_2-1][num_s_1] = "X"
                bot_board_1[num_s_2-1][num_s_1] = "X"
                list_del_1.append([num_s_2-1,num_s_1])
                print("Попал!!!")
                rep_func(us_choice_str)
                us_step = False
            if bot_board_1[num_s_2-1][num_s_1] == 4:
                bot_board_2[num_s_2-1][num_s_1] = "X"
                bot_board_1[num_s_2-1][num_s_1] = "X"  
                list_del_1.append([num_s_2-1,num_s_1])
                print("Попал!!!")
                rep_func(us_choice_str)
                us_step = False 
    else:
        print("Ты уже стрелял туда =_=\n Попробуй снова")
        rep_func(us_choice_str)
def bot_random_str():
    num_s_1 = random.randint(0,9)
    num_s_2 = random.randint(0,9)
    if my_board[num_s_1][num_s_2] == 0 :
        my_board[num_s_1][num_s_2] = "X"
        print("\nБот промахнулся")
        bot_step = False 
    if my_board[num_s_1][num_s_2] == 1 :
        my_board[num_s_1][num_s_2] = "X"
        bot_step = False
        print("\nБот попал в твой корабль")
        rep_func_nostr(bot_random_str)
    if my_board[num_s_1][num_s_2] == 2 :
        my_board[num_s_1][num_s_2] = "X"
        bot_step = False
        print("\nБот попал в твой корабль")
        rep_func_nostr(bot_random_str)
    if my_board[num_s_1][num_s_2] == 3 :
        my_board[num_s_1][num_s_2] = "X"
        bot_step = False
        print("\nБот попал в твой корабль")
        rep_func_nostr(bot_random_str)
    if my_board[num_s_1][num_s_2] == 4 :
        my_board[num_s_1][num_s_2] = "X"
        bot_step = False
        print("\nБот попал в твой корабль")
        rep_func_nostr(bot_random_str)
def start():
    game = True
    while game:
        us_step = True
        while us_step :
            print("\n\t\tТВОЙ ХОД")
            us_choice_str(input())
            us_step = False
        for i in range(len(my_board)):
            for j in range(len(my_board)):
                if my_board[i][j] == 1 or my_board[i][j] == 2 or my_board[i][j] == 3 or my_board[i][j] == 4:
                    f_sh = 1
        if  f_sh == 0:
            print("Ты проиграл")
            game = False
        bot_step = True
        while bot_step:
            print("\n\t\tХОД БОТА")
            bot_random_str()
            bot_step = False
        f_sh_1 =0
        for i in range(len(bot_board_1)):
            for j in range(len(bot_board_1)):
                if  bot_board_1[i][j] == 1 or bot_board_1[i][j] == 2 or bot_board_1[i][j] == 3 or bot_board_1[i][j] == 4:
                    f_sh_1 = 1
        print("ЭТО ДОСКА БОТА\n")
        print("     А Б В Г Д Е Ж З И К")
        for k,j in zip(range(len(my_board)),range(len(my_board))):
            if k == 9:
                print(k+1,"|"," ".join(map(str,bot_board_2[j])))
                continue
            print(k + 1," |"," ".join(map(str,bot_board_2[j])))
        print("\nЭТО ДОСКА ИГРОКА\n")
        print("     А Б В Г Д Е Ж З И К")
        for k,j in zip(range(len(my_board)),range(len(my_board))):
            if k == 9:
                print(k+1,"|"," ".join(map(str,my_board[j])))
                continue
            print(k + 1," |"," ".join(map(str,my_board[j])))



        if f_sh_1 == 0:
            print("КРАСАВЕЕЕЦ!!! Ты выиграл")
            game = False
def main():
    start()
if __name__ == "__main__":
    main()
