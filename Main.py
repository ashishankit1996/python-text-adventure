from Player import Player
from Cell import cells
from Game import title, clear
from Colors import colorprint
from colorama import init, deinit
from pathlib import Path

init()

running = True

player = Player(0,'',0,[],0)

player.load()

#title()

#if a previous save exists
if(Path('save').is_file()):
	print('Previous save found. Load this game?')
	yesno = input('>>> ')


player.save()

clear()


#LOOP

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
			colorprint('you take the gold', 'yellow')
			del(cells[player.cell]['gold'])

		else:
			colorprint('there is no ' + cmd[1] + ' to take', 'red')
	
	elif(cmd[0] == 'save'):

		pass

	elif(cmd[0] == 'quit'):
		break
		

	else:
		colorprint('I dont know how to do that.', 'red')

deinit()
savefile.close()

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
# save/load

#sator
#arepo
#tenet
#opera
#rotas
