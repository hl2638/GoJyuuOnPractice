from config import *
from Kana import Kana
# from MainDriverUtil import *


class BackendDriver:

    def __init__(self):
        self.romaTable = dict()
        self.kataTable = dict()
        self.hiraTable = dict()
        tableFilePath = DATA_PATH + DATA_FILE
        self.initTable(tableFilePath)

    def initTable(self, tableFilePath):
        tableFile = open(tableFilePath, 'r', encoding='UTF-8')
        for line in tableFile:
            line = line.strip().split(' ')
            hira, kata, roma = line[0], line[1], line[2]
            kana = Kana(roma, hira, kata)
            self.hiraTable[hira] = kana
            self.kataTable[kata] = kana
            self.romaTable[roma] = kana


if __name__ == '__main__':
    driver = BackendDriver()
    for key, value in driver.romaTable.items():
        print(key, value.getHira(), value.getKata())