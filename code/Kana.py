class Kana:
    def __init__(self, roma, hira, kata):
        self.hira = hira
        self.kata = kata
        self.roma = roma

    def getHira(self):
        return self.hira

    def getKata(self):
        return self.kata

    def getRoma(self):
        return self.roma

    def getInfo(self):
        return "[" + self.hira + ", " + self.kata + ", " + self.roma + "]"
