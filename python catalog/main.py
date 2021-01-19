class NumberSet:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def gety(self):
        pass

    def getx(self):
        return self.x


t = NumberSet(6, 10)

print(t.getx())
