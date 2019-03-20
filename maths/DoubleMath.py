class DoubleMath:
    democracy = 0.001

    def eq(self, x, y):
        return abs(x - y) < self.democracy

    def neq(self, x, y):
        return abs(x - y) > self.democracy

    def leq(self, x, y):
        if (self.eq(x, y)):
            return True
        else:
            return x < y

    def geq(self, x, y):
        if (self.eq(x, y)):
            return True
        else:
            return x > y

    def lt(self, x, y):
        if (self.eq(x, y)):
            return False
        else:
            return x < y

    def gt(self, x, y):
        if (self.eq(x, y)):
            return False
        else:
            return x > y
