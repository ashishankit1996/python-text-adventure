from Entity import Entity
from Entities.Door import Door
from Colors import colortext
from colorama import init, deinit

init()

door1 = Door('steel door', True)

print(colortext('█\tblue', 'blue'))
print(colortext('█\tcyan', 'cyan'))
print(colortext('█\tgreen', 'green'))
print(colortext('█\tyellow', 'yellow'))
print(colortext('█\tred', 'red'))
print(colortext('█\tmagenta', 'magenta'))

print(door1.examine())

deinit()

# go
#   north
#   south
#	east
#	west
# take/drop/eat/drink
#	<item : item>
#	all
# give
#   <recipient : feature>
#       <item : item>
#       all
# attack/climb/read/examine/talk/open/close
#	<target : feature>
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
