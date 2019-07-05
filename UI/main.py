from  formtemplate import Ui_FormTemplate
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore
import sys
import os
import cv2

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

class HandWritingApp(QMainWindow, Ui_FormTemplate):
	def __init__(self):
		QMainWindow.__init__(self)
		Ui_FormTemplate.__init__(self)
		self.setupUi(self)

		# Butons and functions mapped
		self.actionExit.triggered.connect(self.exit)
		self.actionLoad_Template.triggered.connect(self.load_image)
		self.add_field_object.clicked.connect(self.add_new_field)

		# Name and location of each field saved as a csv later
		self.existing_fields = []
		self.locations = []

		# Add a painter on top of the image window
		self.form_image_painter = Image_Painter(self.centralwidget)
		self.form_image_painter.setGeometry(self.form_image.geometry())
		self.form_image_painter.setFrameShape(QtWidgets.QFrame.Panel)
		self.form_image_painter.setFrameShadow(QtWidgets.QFrame.Plain)
		self.form_image_painter.setText("")
		self.form_image_painter.setObjectName("form_image_painter")


	def new_template(self):
		pass
	def load_image(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file',os.getcwd(),"Image files (*.jpg *.png *.gif)")
		if fname:
			self.original_image = cv2.imread(fname[0])
			self.form_image.setPixmap(QPixmap(fname[0]))
			self.form_image.show()

	def add_new_field(self):
		name = self.field_line_edit.text()

		if name not in self.existing_fields:
			self.existing_fields.append(name)
			self.locations.append(self.form_image_painter.get_rect_position())
		else:
			msg = QMessageBox()
			msg.setText("Error")
			msg.setInformativeText("Field name aldready exists")
			msg.setWindowTitle("Error2")
			msg.exec_()


	def exit(self):
		print("Exiting")
		quit(0)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	hwapp = HandWritingApp()
	hwapp.show()
	sys.exit(app.exec_())