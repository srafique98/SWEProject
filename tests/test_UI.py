from src.Menu import Menu
from src.Window import Window
from PySide6.QtWidgets import QApplication
import sys


def test_WindowInit():
    try:
        app = QApplication(sys.argv)
        window = Menu()
        return True
    except:
        return False
