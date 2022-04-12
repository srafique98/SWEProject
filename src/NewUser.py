from src.Window import Window
from src.db_client import DB_Client
from PySide6.QtWidgets import *
from PySide6 import QtCore
from src.Job import Job


class Listing(Window):
    def __init__(self):
        uiFile = "ui/signup.ui"
        super().__init__()
        self.window = super().windowInit(uiFile, self)