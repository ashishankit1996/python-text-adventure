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
