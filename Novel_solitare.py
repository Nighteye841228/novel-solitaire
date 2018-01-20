# -*- coding: UTF-8 -*-
import random

def novel(x,y):
    
    flag = 1
    number = -1
    dragon = [[None] * x for i in range(4)]
    dragon_check = [[None] * 3 for i in range(x)]
    dragon_check2 = [[None] * 3 for i in range(x)]
    protect = 0
           

    for i in range(4):
        pick = range(x)
        for j in range(x):
            
            if(i==0):
                dragon[i][j]= j

            else:
                number = pick[0]
                while( number==j or flag==1 ):
                    random.shuffle(pick)
                    number = pick[0]
                    for item in range(3):
                        if(dragon_check[number][item]==dragon[i-1][j] or dragon_check2[number][item]==j): 
                            flag = 1
                            break 
                        else:
                            flag = 0
                    protect += 1
                    if (protect>x*1000):
                        novel(x,y)
                else:
                    dragon[i][j]=number
                    pick.pop(0)
                    dragon_check[number].pop(0)
                    dragon_check2[number].pop(0)
                    dragon_check[number].append(dragon[i-1][j])
                    dragon_check2[number].append(j)
                    
                    flag = 1
            


    for i in range(4):
       for j in range(x):
            dragon[i][j] += 1
    if(len(y)>0):
        print('\n'.join([''.join(['{0:3} {1:>10}'.format(item,playerList[item]) for item in row]) for row in dragon]))
    else:
        print('\n'.join([''.join(['{0:3}'.format(item) for item in row]) for row in dragon]))
    exit()
    


player = int(raw_input("輸入玩家數量: "))
checkPlayerName = raw_input("需要增加玩家編號對應碼嗎？ (y/n) ")
playerList = {}
if(checkPlayerName == "y" or checkPlayerName == "yes"):
    for i in range(player):
        playerOrder = raw_input("輸入玩家編號: ")
        playerName = raw_input("輸入玩家暱稱: ")
        playerList[int(playerOrder)] = str(playerName)
novel(player,playerList)
