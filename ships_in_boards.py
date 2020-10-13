import numpy as np
import ships
import random
from random import choice
from ships import list_ship as ls 
list_del = []
list_del_2 = []
list_del_3 = []
dict_1 = {}
rand =[]
bot_board = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
            ]
def ship_in_board(bot_board,*args):
    for i in range(len(args)):
        if i in range(0,4):
            num_x = random.randint(0,9)
            num_y = random.randint(0,9)
            if [num_x,num_y]  in list_del:
                r = True
                while r:
                    num_y = random.randint(0,9)
                    num_x = random.randint(0,9)
                    if [num_x,num_y] not in list_del:
                        r = False
                    bot_board[num_x][num_y] = 1
                continue
            bot_board[num_x][num_y] = 1
            list_del.append([num_x,num_y])
        if i in range(4,7):
            e = True
            while e :
                num_x = random.randint(0,9)
                num_y = random.randint(0,9)
                if bot_board[num_x][num_y] not in [1,2,3] and num_x-1 != -1 and bot_board[num_x-1][num_y] not in [1,2,3]:
                    
                    list_del_3.append([num_x-1,num_y])
                if bot_board[num_x][num_y] not in [1,2,3] and num_x+1 != 10 and bot_board[num_x+1][num_y] not in [1,2,3]:
                    list_del_3.append([num_x+1,num_y])
                if bot_board[num_x][num_y] not in [1,2,3] and num_y-1 != -1 and bot_board[num_x][num_y-1] not in [1,2,3]:
                    list_del_3.append([num_x,num_y-1])
                 
                if bot_board[num_x][num_y] not in [1,2,3] and num_y+1 != 10 and bot_board[num_x][num_y+1] not in [1,2,3] :
                    list_del_3.append([num_x,num_y+1])
                  
                if len(list_del_3) != 0:
                    e = False
                    break
            
            rand = random.choice(list_del_3)
            bot_board[num_x][num_y] = 2
            x = rand[0]
            y = rand[1]
            bot_board[x][y] = 2
            list_del_3.clear()
        if i in range(7,9):
            e = True
            while e :
                num_x = random.randint(0,9)
                num_y = random.randint(0,9)

                if bot_board[num_x][num_y] not in [1,2,3] and num_x-1 != -1 and bot_board[num_x-1][num_y] not in [1,2,3] and num_x-2 not in [-1,-2] and bot_board[num_x-2][num_y] not in [1,2,3]:
                 
                    list_del_3.append([num_x-1,num_y,num_x-2,num_y])
                if bot_board[num_x][num_y] not in [1,2,3] and num_x+1 != 10 and bot_board[num_x+1][num_y] not in [1,2,3] and num_x+2 not in [10,11] and bot_board[num_x-2][num_y] not in [1,2,3]:
                    list_del_3.append([num_x+1,num_y,num_x+2,num_y])
                
                if bot_board[num_x][num_y] not in [1,2,3] and num_y-1 != -1 and bot_board[num_x][num_y-1] not in [1,2,3] and num_y-2 not in [-1,-2] and bot_board[num_x][num_y-2] not in [1,2,3]:
                    list_del_3.append([num_x,num_y-1,num_x,num_y-2])
                   
                if bot_board[num_x][num_y] not in [1,2,3] and num_y+1 != 10 and bot_board[num_x][num_y+1] not in [1,2,3] and num_y+2 not in [10,11] and bot_board[num_x][num_y+2] not in [1,2,3]:
                    list_del_3.append([num_x,num_y+1,num_x,num_y+2])
                    
                if len(list_del_3) != 0:
                    e = False
                    break
        
            rand = random.choice(list_del_3)
           
            list_del_3.clear()
            bot_board[num_x][num_y] = 3
            bot_board[rand[0]][rand[1]] = 3
            bot_board[rand[2]][rand[3]] = 3
        if i == 9:
            e = True
            while e :
                num_x = random.randint(0,9)
                num_y = random.randint(0,9)
                if bot_board[num_x][num_y] not in [1,2,3] and num_x-1 != -1 and bot_board[num_x-1][num_y] not in [1,2,3] and num_x-2 not in [-1,-2] and bot_board[num_x-2][num_y] not in [1,2,3] and num_x-3 not in [-1,-2,-3] and bot_board[num_x-3][num_y] not in [1,2,3]:
                   
                    list_del_3.append([num_x-1,num_y,num_x-2,num_y,num_x-3,num_y])
                if bot_board[num_x][num_y] not in [1,2,3] and num_x+1 != 10 and bot_board[num_x+1][num_y] not in [1,2,3] and num_x+2 not in [10,11] and bot_board[num_x+2][num_y] not in [1,2,3] and num_x+3 not in [10,11,12] and bot_board[num_x+3][num_y] not in [1,2,3]:
                    list_del_3.append([num_x+1,num_y,num_x+2,num_y,num_x+3,num_y])
                 
                if bot_board[num_x][num_y] not in [1,2,3] and num_y-1 != -1 and bot_board[num_x][num_y-1] not in [1,2,3] and num_y-2 not in [-1,-2] and bot_board[num_x][num_y-2] not in [1,2,3] and num_y-3 not in [-1,-2,-3] and bot_board[num_x][num_y-3] not in [1,2,3]:
                    list_del_3.append([num_x,num_y-1,num_x,num_y-2,num_x,num_y-3])
                   
                if bot_board[num_x][num_y] not in [1,2,3] and num_y+1 != 10 and bot_board[num_x][num_y+1] not in [1,2,3] and num_y+2 not in [10,11] and bot_board[num_x][num_y+2] not in [1,2,3] and num_y+3 not in [10,11,12] and bot_board[num_x][num_y+3] not in [1,2,3]:
                    list_del_3.append([num_x,num_y+1,num_x,num_y+2,num_x,num_y+3])
                
                if len(list_del_3) != 0:
                    e = False
                    break
            rand = random.choice(list_del_3)
            list_del_3.clear()
            bot_board[num_x][num_y] = 4
            bot_board[rand[0]][rand[1]] = 4
            bot_board[rand[2]][rand[3]] = 4
            bot_board[rand[4]][rand[5]] = 4
def main():
    ship_in_board(bot_board,*ls)
if __name__ == "__main__":
    main()