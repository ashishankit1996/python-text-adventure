class Feature:
    variable = "member variable"

    def function(self):
        print("member function")

class Door(Feature):

    _open = False

    def __init__(self, openOrClosed):
        self._open = openOrClosed

    def open(self):
        self._open = True

    def close(self):
        self._open = False


door1 = Door(True)
print(door1._open)
