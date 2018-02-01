class MyLength:
    length = 0
    unit = "mile"
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit



    def equals(self, inputLength):
        return inputLength.length == self.length and inputLength.unit == self.unit;