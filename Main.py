from Player import Player
from Cell import cells
from Entity import Entity
from Entities.Door import Door
from Colors import colorprint
from colorama import init, deinit

init()

running = True
player = Player(4,'Default',0,[])

#if no previous save exists
#   create new file

while running:
    cmd = input('>>> ').lower().split(' ')

    # move command
    if(cmd[0] == 'go'):
        if(cmd[1] in cells[player.cell]):
            player.cell = cells[player.cell][cmd[1]]
        else:
            colorprint('you cannot go that way', 'red')

    # take item command
    elif(cmd[0] == 'take'):

        # if the current cell has an item node AND the argument of take is the value of the item node
        if('item' in cells[player.cell] and cmd[1] in cells[player.cell]['item']):
            # add the argument to the players inventory
            player.inventory += cmd[1]
            colorprint('you take the ' + cmd[1], 'green')
            # remove the item node from the current room
            del(cells[player.cell]['item'])

        # if the current cell AND the argument of take is gold
        elif('gold' in cells[player.cell] and cmd[1] == 'gold'):
            player.money += cells[player.cell]['gold']
            colorprint('you take the gold.', 'yellow')
            del(cells[player.cell]['gold'])

        else:
            colorprint('there is no ' + cmd[1] + ' to take', 'red')
    else:
        colorprint('WHAT DO YOU WANT FROM ME?', 'red')

deinit()

# go
#   north
#   south
#	east
#	west
# take
#	<item : string>
#	all
# drop/eat/drink
#	<item : item>
#	all
# give
#   <recipient : feature>
#       <item : item>
#       all
# attack/climb/read/examine/talk/open/close
#	<target : feature>
# inventory
# repeat
# save/load
                                                         
# ____              ___                                    
# `Mb(      db      )d'                                    
#  YM.     ,PM.     ,P                                     
#  `Mb     d'Mb     d' ____    ___ ___  __ ___  __    __   
#   YM.   ,P YM.   ,P  `MM(    )M' `MM 6MM `MM 6MMb  6MMb  
#   `Mb   d' `Mb   d'   `Mb    d'   MM69 "  MM69 `MM69 `Mb 
#    YM. ,P   YM. ,P     YM.  ,P    MM'     MM'   MM'   MM 
#    `Mb d'   `Mb d'      MM  M     MM      MM    MM    MM 
#     YM,P     YM,P       `Mbd'     MM      MM    MM    MM 
#     `MM'     `MM'        YMP      MM      MM    MM    MM 
#      YP       YP          M      _MM_    _MM_  _MM_  _MM_
#                          d'                              
#                      (8),P                               
#                       YMM                                
