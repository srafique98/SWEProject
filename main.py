import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from src.Menu import Menu


def main():
    app = QApplication(sys.argv)
    window = Menu()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()