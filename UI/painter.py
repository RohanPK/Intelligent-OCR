from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *

class Image_Painter(QtWidgets.QLabel):
	def __init__(self,window):
		QtWidgets.QLabel.__init__(self,window)
		# Stores mouse position before and after click
		self.begin = QtCore.QPoint()
		self.end = QtCore.QPoint()

	def paintEvent(self, event):
		qp = QPainter(self)
		br = QBrush(QColor(100, 10, 10, 40))  
		qp.setBrush(br)   
		qp.drawRect(QtCore.QRect(self.begin, self.end))       

	def mousePressEvent(self, event):
		self.begin = event.pos()
		self.end = event.pos()
		self.update()

	def mouseMoveEvent(self, event):
		self.end = event.pos()
		self.update()

	def mouseReleaseEvent(self, event):
		self.end = event.pos()
		self.update()

	def get_rect_position(self):
		return (self.begin,self.end)
