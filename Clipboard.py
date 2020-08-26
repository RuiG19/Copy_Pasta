import os

class IClipboard(object):
    def copy(self, text: str):
        raise NotImplementedError()
    def past(slef) -> str:
        raise NotImplementedError()

class WindowsClipboard(object):
    def copy(self, text: str):
        command = 'echo|set /p="' + text.strip() + '" | clip'
        os.system(command)
      

    def past(slef) -> str:
        raise NotImplementedError()