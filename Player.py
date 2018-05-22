from Cell import cells

class Player:
	cell = 0
	name = ''
	money = 0
	inventory = []
	HP = 100

	def __init__(self,_cell,_name,_money,_inventory,_HP):
		self.cell = _cell
		self.name = _name
		self.money = _money
		self.inventory = _inventory
		self.HP = _HP

	def save(self, filename = 'save'):
		
		file = open(filename, 'w')
		
		#print(' '.join(format(ord(x), 'b') for x in self.cell))
		print(' '.join(format(ord(x), 'b') for x in self.name))
		#print(' '.join(format(ord(x), 'b') for x in self.money))
		#print(' '.join(format(ord(x), 'b') for x in self.inventory))
		#print(' '.join(format(ord(x), 'b') for x in self.HP))
		file.close()



	def load(self, filename = 'save'):
		file = open(filename, 'r')

		lines = file.readlines()
		#self.cell = lines[0]

		print(lines[0])
		#self.name = ''.join([chr(int(x, 2)) for x in list(lines[1].split(' '))])

		file.close()
