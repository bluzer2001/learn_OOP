

class Cart:
    def __init__(self):
        self.items = []

    def add(self, price):
        if price <= 0:
            raise ValueError
        self.items.append(price)

    def total(self):
        return sum(self.items)
