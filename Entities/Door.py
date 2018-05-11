from Entity import Entity

class Door(Entity):

	_open = False

	def __init__(self, name, openOrClosed):
		self._name = name
		self._open = openOrClosed

	def open(self):
		self._open = True

	def close(self):
		self._open = False
