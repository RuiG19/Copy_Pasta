class IDataManager(object):
    def readItem(self, index):
        raise NotImplementedError()
    def readAllItems(self):
        raise NotImplementedError()
    def addItem(self, item):
        raise NotImplementedError()
    def removeItem(self, index):
        raise NotImplementedError()
    def editItem(self, index, item):
        raise NotImplementedError()

class TextFileDataManager(IDataManager):
    def __init__(self, filePath):
        self.filePath = filePath
        self.__contentUpdate()

    def readItem(self, index):
        self.__contentUpdate()
        return self.fileContent[index] if len(self.fileContent) > index else ""

    def readAllItems(self):
        self.__contentUpdate()
        return self.fileContent

    def addItem(self, item):
        if isinstance(item, str):
            self.fileContent.append(item)
            self.__fileUpdate()

    def removeItem(self, index):
        if len(self.fileContent) > index:
            self.fileContent.pop(index)
            self.__fileUpdate()

    def editItem(self, index, item):
        if len(self.fileContent) > index and isinstance(item, str):
            self.fileContent[index] = item
            self.__fileUpdate()

    def __fileUpdate(self):
        file = open(self.filePath, "w")
        for i in self.fileContent:
            file.write(i + '\n')
        file.close()

    def __contentUpdate(self):
        file = open(self.filePath, "r")
        self.fileContent = file.read().split('\n')
        self.fileContent.pop() # remove last '\n'
        file.close()

