from Cell import cells

class Player:
    _cell = 0
    _name = ''
    _money = 0
    _inventory = []

    def __init__(self,_cell,_name,_money,_inventory):
        self.cell = _cell
        self.name = _name
        self.money = _money
        self.inventory = _inventory
