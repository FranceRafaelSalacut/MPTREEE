class Job:
    def __init__(self, number:int, time:int, size:int):
        self.number = int(number)
        self.time = int(time)
        self.size = int(size)
        self.active = 0

    def p(self):
        return str(self.number) + "\t" + str(self.time) + "\t" + str(self.size)

class Memory:
    def __init__(self, block:int, size:int):
        self.block = int(block)
        self.size = int(size)
        self.current = None
        self.used = 0

    def p(self):
        return str(self.block) + "\t" + str(self.size)


    