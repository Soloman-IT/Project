import numpy as np
import ships
import random
from random import choice
from ships import list_ship as ls
import user_choice_ships as us_ch
from ships_in_boards import ship_in_board
from boards import my_board,bot_board_1,bot_board_2
list_del = []
list_del_2 = []
list_del_3 = []
rand =[]

def main():
    ship_in_board(bot_board_1,*ls)
    print("\n\t\t\t\t\t\tМОРСКОЙ БОЙ")
    if input("\n\n\nПривет, хочешь ли ты сыграть в морской бой?(конечно хочешь) \n(ДА)\n(НЕТ)\n :") == "ДА":
        print("""
              Смотри, 0 - это пустое поле. Для тебя поле бота будет все в 0 а вот так, ничего в жизни простого не бывает
                      1 - это самый маленький корабль
                      2 - это корабль, который занимает 2 клетки
                      3 - это корабль, который занимает 3 клетки
                      4 - это ... считать я думаю ты умеешь
              """)
        print("\nВ данный момент твоя доска с кораблями пуста( и выглядит так :")
        for i in (my_board):
            print(" ".join(map(str,i)))

        if input("Хочешь сам распределить свои корабли ? (ДА) (НЕТ) :") == "ДА":
            us_ch.user_board(my_board)
            print("Так-с ну все готово для игры :) ")
            print("\nТвои ходы будут определяться координатами(В-1 или В1)")
            


        else :
            ship_in_board(my_board,*ls)
            print("Так-с ну все готово для игры :) ")
            print("\nТвои ходы будут определяться координатами(В-1 или В1)")
        from fight import start
        start()
    else:
        print("ок(")
        exit()
if __name__ == "__main__":
    main()