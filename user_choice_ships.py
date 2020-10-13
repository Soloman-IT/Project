import numpy as np
import ships
import random
from random import choice
from ships import list_ship as ls
list_del = []
slov = {
        "А": 0,
        "Б": 1,
        "В": 2,
        "Г": 3,
        "Д": 4,
        "Е": 5,
        "Ж": 6,
        "З": 7,
        "И": 8,
        "К": 9,
       }
def user_board(us_board):
    num_s_1 = 0
    num_s_2 = 0
    print("Пример : В - 5 или В5\n")
    print("Запуск (1) флота")
    for i in range(4):
        print("По очереди(через пробел) вводите координату короблей(1)")
        r = True
        while r:
            str_1 = input()
            for i in range(len(str_1)):
                if str_1[i] in slov:
                    num_s_1 = slov[str_1[i]]

            num =  ["1","2","3","4","5","6","7","8","9","10"]
            for i in (num):
                if str_1.find("{}".format(i)) != -1:
                    num_s_2 = int(i)
            if "10" in str_1:
                num_s_2 = 10
            if us_board[num_s_2-1][num_s_1] not in list_del:
                us_board[num_s_2-1][num_s_1] = 1
                list_del.append([num_s_2-1,num_s_1])
                r = False
        print("      А  Б  В  Г  Д  Е  Ж  З  И  К")
        for i,j in zip(range(len(us_board)),range(len(us_board))):
            if i == 9:
                print(i+1,"|",us_board[j])
                continue
            print(i + 1," |",us_board[j])
    print()        
    print("Не забываем и про остальные части корабля)")
    print()
    print("Запуск (2) флота")
    count = 0
    for i in range(3):
        r = True
        count = 0
        print(i+1," кораблик пошел...")
        for i in range(2):
            r = True
            while r:
                count += 1
                str_1 = input()
                for i in range(len(str_1)):
                    if str_1[i] in slov:
                        num_s_1 = slov[str_1[i]]
                num =  ["1","2","3","4","5","6","7","8","9","10"]
                for i in (num):
                    if str_1.find("{}".format(i)) != -1:
                        num_s_2 = int(i)
                if "10" in str_1:
                    num_s_2 = 10
                print(num_s_2,num_s_1)
                if us_board[num_s_2-1][num_s_1] not in list_del:
                    us_board[num_s_2-1][num_s_1] = 2
                    list_del.append([num_s_2-1,num_s_1])
                    r = False
        print("      А  Б  В  Г  Д  Е  Ж  З  И  К")
        for i,j in zip(range(len(us_board)),range(len(us_board))):
            if i == 9:
                print(i+1,"|",us_board[j])
                continue
            print(i + 1," |",us_board[j])
        count = 0  
    print("\nЗапуск (3) флота")
    for i in range(0,2):
        r = True
        count = 0
        print(i+1," кораблик пошел...")
        for i in range(3):
            r = True
            while r:
                count += 1
                str_1 = input()
                for i in range(len(str_1)):
                    if str_1[i] in slov:
                        num_s_1 = slov[str_1[i]]
                num =  ["1","2","3","4","5","6","7","8","9","10"]
                for i in (num):
                    if str_1.find("{}".format(i)) != -1:
                        num_s_2 = int(i)
                if "10" in str_1:
                    num_s_2 = 10
                if us_board[num_s_2-1][num_s_1] not in list_del:
                    us_board[num_s_2-1][num_s_1] = 3
                    list_del.append([num_s_2-1,num_s_1])
                    r = False
        print("      А  Б  В  Г  Д  Е  Ж  З  И  К")
        for i,j in zip(range(len(us_board)),range(len(us_board))):
            if i == 9:
                print(i+1,"|",us_board[j])
                continue
            print(i + 1," |",us_board[j])
        count = 0
    r = True
    count = 0
    print("Запускается 4 корабль")
    count = 0
    print(i+1," кораблик пошел...")
    for i in range(4):
        r = True
        while r:
            count += 1
            str_1 = input()
            for i in range(len(str_1)):
                if str_1[i] in slov:
                    num_s_1 = slov[str_1[i]]
            num =  ["1","2","3","4","5","6","7","8","9","10"]
            for i in (num):
                if str_1.find("{}".format(i)) != -1:
                    num_s_2 = int(i)
            if "10" in str_1:
                num_s_2 = 10
            if us_board[num_s_2-1][num_s_1] not in list_del:
                us_board[num_s_2-1][num_s_1] = 4
                list_del.append([num_s_2-1,num_s_1])
                r = False
def main():
    user_board(my_board)
if __name__ == "__main__":
    main()