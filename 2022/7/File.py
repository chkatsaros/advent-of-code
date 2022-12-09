class File:
    def __init__(self, name, size = 0):
        self.name = name
        self.size = size
    def getName(self):
        return self.name
    def getSize(self):
        return self.size