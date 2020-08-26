from DataManager import TextFileDataManager
from Controller import *

dataManager = TextFileDataManager("data\copy_pasta_data.txt")

window = tkinter.Tk()
window.title("Copy Pasta")

#window.iconbitmap("assets/pasta.ico")

copy_pasta = Controller(dataManager, window)
copy_pasta.start()

window.mainloop()
