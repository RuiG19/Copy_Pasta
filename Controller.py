from Clipboard import WindowsClipboard
from DataManager import *
from Model import *
from View import *

class Controller(object):
    def __init__(self, dataManager: IDataManager, window):
        self.clipboard = WindowsClipboard()
        self.model = Model(dataManager)
        self.view = View(self, window)
    
    def start(self):
        self.view.updateView(self.model.readAllItems())

    def onCopyEvent(self, index):
        self.clipboard.copy(self.model.readItem(index))

    def onRemoveEvent(self, index):
        self.view.updateView(self.model.removeItem(index))

    def onAddEvent(self, item):
        self.view.updateView(self.model.addItem(item))

