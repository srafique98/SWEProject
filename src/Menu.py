from PySide6.QtWidgets import *
from PySide6.QtGui import QFont
from src.Window import Window


class Menu(Window):
    def __init__(self):
        super().__init__()
        self.menuWindow()

    def menuWindow(self):
        self.label = QLabel("Rayquaza project!", self)
        self.label.setGeometry(50, 100, 900, 100)
        self.label.setVisible(True)
        self.label.setFont(QFont('Arial', 50))
