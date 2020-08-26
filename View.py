from Controller import *
import tkinter
import threading

class View(object):
    def __init__(self, controller, window):
        self.controller = controller
        self.window = window
        self.window.resizable(False, False)
        
        self.mainFrame = tkinter.Frame(self.window)
        self.mainFrameGrid = self.mainFrame.grid()

    
    def updateView(self, items):

        for child in self.mainFrame.winfo_children():
            child.destroy()


        row_counter = 0
        for item in items:
            tkinter.Label(self.mainFrame, text =item).grid(row = row_counter, column = 0, columnspan= 4, sticky="w")
            tkinter.Button(self.mainFrame, text ="Copy", command= lambda index = row_counter: self.copyCallback(index)).grid(row = row_counter, column = 4)
            tkinter.Button(self.mainFrame, text ="Remove", command= lambda index = row_counter: self.removeCallback(index)).grid(row = row_counter, column = 5)
            row_counter += 1

        # entry_title = tkinter.Entry(self.mainFrame).grid(row = row_counter, column = 0)
        self.entry_content = tkinter.Entry(self.mainFrame)
        self.entry_content.grid(row = row_counter, column = 0, columnspan= 4, sticky="nwes")
        tkinter.Button(self.mainFrame, text ="Add", command= lambda : self.addCallback()).grid(row = row_counter, column = 4, columnspan= 2, sticky="nwes")
      

    def addCallback(self, ):
        item = self.entry_content.get()
        self.controller.onAddEvent(item)
    
    def removeCallback(self, index):
        self.controller.onRemoveEvent(index)

    def copyCallback(self, index):
        self.controller.onCopyEvent(index)

    