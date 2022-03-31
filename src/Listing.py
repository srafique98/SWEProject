from Window import Window

class Listing(Window):
    def __init__(self):
        uiFile = "../ui/mainwindow.ui"
        super().__init__()
        self.window = super().windowInit(uiFile, self)
        #self.window.show()

