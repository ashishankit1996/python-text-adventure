from abc import ABC

class Entity(ABC):
	_name = ''
	
	def give(self, item):
		return 'you try to give the ' + item.name + ' to the ' + self._name + ', but it doesnt work.'

	def attack(self):
		return 'you try to attack the ' + self._name + ', but fail miserably.'
	
	def climb(self):
		return 'you try to climb the ' + self._name + ', but you can\'t.'
		
	def read(self):
		return 'you try to read the ' + self._name + ', but there is nothing to read.'

	def examine(self):
		return 'you examine the ' + self._name + '. you see nothing out of the ordinary.'

	def talk(self):
		return 'you greet the ' + self._name + '. it seems a little shy.'

	def open(self):
		return 'you try to open the ' + self._name + ', but it doesn\'t work.' 

	def close(self):
		return 'you try to close the ' + self._name + ', but it doesn\'t work.'
