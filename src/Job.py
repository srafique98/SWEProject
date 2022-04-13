from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Signal as QtSignal


class Job(QWidget):
	clicked = QtSignal()

	def __init__(self, jobTitle, salary, sector):
		super().__init__()
		self.vert = QVBoxLayout()
		self.vert.setStretch(0, 0)
		self.vert.setSpacing(0)
		self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

		self.jobFont = QFont("Segoe UI", 9)
		self.salaryFont = QFont("Segoe UI", 9)
		self.sectorFont = QFont("Segoe UI", 9)

		self.jobTitle = QLabel(jobTitle)
		self.jobTitle.setFont(self.jobFont)

		self.salary = QLabel(salary)
		self.salary.setFont(self.salaryFont)
		self.salary.setIndent(16)

		self.sector = QLabel(sector)
		self.sector.setFont(self.sectorFont)
		self.sector.setIndent(16)

		self.vert.addWidget(self.jobTitle)
		self.vert.addWidget(self.salary)
		self.vert.addWidget(self.sector)
		self.setLayout(self.vert)

	def getLayout(self):
		return self.vert

	def mousePressEvent(self, e):
		self.clicked.emit()
		print("does it work")
		print(QMouseEvent.pos)
		

