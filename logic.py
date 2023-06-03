class Game:
    def __init__(self):
        self.day = 0
        self.money = 0
        self.protestSize = 1
    def eval(self,day,money,size):
        self.day = day
        self.money = money
        self.protestSize = size