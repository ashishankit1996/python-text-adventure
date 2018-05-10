from Feature import Door
from Colors import *
from colorama import init, deinit

init()

door1 = Door(True)
print(door1._open)
print(door1.poop())

print('\033[94m' + 'succ' + '\033[0m')

deinit()

# go
#   north
#   south
#	east
#	west
# take/drop/eat/drink
#	<item name>[quantity|all]
#	all
# give
#   <recipient : feature>
#       <item : item>
#       all
# attack/climb/read/examine/talk/open/close
#	<feature>
# again
# save/load
