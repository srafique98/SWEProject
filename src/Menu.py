from Window import Window
from Listing import Listing


class Menu(Window):
    def __init__(self):
        uiFileName = "../ui/mainmenu.ui"
        super().__init__()
        self.window = super().windowInit(uiFileName, self)
        self.window.startButton.clicked.connect(self.start)
        #self.window.show()


    def start(self):
        self.close()
        self.nextWindow = Listing()
        super().nextWindow(self.window)
