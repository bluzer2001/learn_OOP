

class Counter:

    def __init__(self, n = 0):
        self.count = n

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0
