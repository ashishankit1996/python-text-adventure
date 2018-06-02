from Cell import cells
from Game import resize

class Player:
	name = ''
	cell = 0
	money = 0
	HP = 100
	inventory = []

	def __init__(self,_name,_cell,_money,_HP,_inventory):
		self.name = _name
		self.cell = _cell
		self.money = _money
		self.HP = _HP
		self.inventory = _inventory

	def save(self, filename = 'save'):
		file = open(filename, 'w+')
		file.write(self.name + '\n')
		file.write(str(self.cell) + '\n')
		file.write(str(self.money) + '\n')
		file.write(str(self.HP) + '\n')
		file.write('{\n')
		for item in self.inventory:
			file.write('\t' + item + '\n')
		file.write('}\n')
		file.close()

	def load(self, filename = 'save'):
		file = open(filename, 'r')
		lines = file.readlines()

		self.name = lines[0]
		self.cell = int(lines[1])
		self.money = int(lines[2])
		self.HP = int(lines[3])

		#resize list to fit all items

		resize(self.inventory, len(lines), '')
		for x in range(5,len(lines)-1):
			self.inventory[x-5] = lines[x][1:]

		file.close()

	def create(self, startingCell = 4):
		playerIsSatisfied = ''
		while(not playerIsSatisfied == 'yes'):
			print('What is your name?')
			self.name = input('>>> ')
			print('Your name is ' + self.name + '?')
			playerIsSatisfied = input('>>> ').lower()
		self.cell = startingCell
		self.money = 0
		self.HP = 100
		self.inventory = []
