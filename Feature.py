from abc import ABC, abstractmethod

class Feature(ABC):
	name = ''
	
	def give(self, item):
		print("You try to give the " + self.name + " the ")

	def attack(self):
		pass
	
	def climb(self):
		pass
		
	def read(self):
		pass
	@abstractmethod
	def examine(self):
		pass
	@abstractmethod
	def talk(self):
		pass
	@abstractmethod
	def open(self):
		pass
	@abstractmethod
	def close(self):
		pass

	def poop(self):
		print("proop")

class Door(Feature):

	_open = False

	def poop(self):
		print("not proop")

	def __init__(self, openOrClosed):
		self._open = openOrClosed

	def open(self):
		self._open = True

	def close(self):
		self._open = False

	def give(self):
		print("")

	def attack(self):
		print("")

	def climb(self):
		print("")

	def read(self):
		print("")

	def examine(self):
		print("")
		
	def talk(self):
		print("")




door1 = Door(True)
print(door1._open)
