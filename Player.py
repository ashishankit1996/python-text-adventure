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

    def save(self):
        print(' '.join(format(ord(x), 'b') for x in self.cell))
        print(' '.join(format(ord(x), 'b') for x in self.name))
        print(' '.join(format(ord(x), 'b') for x in self.money))
        print(' '.join(format(ord(x), 'b') for x in self.inventory))
        print(' '.join(format(ord(x), 'b') for x in self.HP))
