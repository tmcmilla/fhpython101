class Counter:
    def __init__(self):
        self.counter = 0

    def inc(self):
        self.counter = self.counter+1
    def dec(self):
        self.counter = self.counter-1
    def __str__(self):
        return str(self.counter)
