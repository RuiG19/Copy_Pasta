from DataManager import *

class Model(object):
    def __init__(self, dataManager: IDataManager):
        self.dataManager = dataManager

    def readItem(self, index):
        return self.dataManager.readItem(index)

    def readAllItems(self):
        return self.dataManager.readAllItems()

    def removeItem(self, index):
        self.dataManager.removeItem(index)
        return self.dataManager.readAllItems()

    def addItem(self, item):
        self.dataManager.addItem(item)
        return self.dataManager.readAllItems()