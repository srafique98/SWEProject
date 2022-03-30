from PySide6.QtWidgets import *
from Menu import Menu
import sys


def main():
	app = QApplication(sys.argv)
	window = Menu()
	window.show()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()
