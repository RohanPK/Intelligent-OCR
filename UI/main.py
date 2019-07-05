from  formtemplate import Ui_FormTemplate
from painter import Image_Painter
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import cv2

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
		self.form_image_painter.setFrameShape(QFrame.Panel)
		self.form_image_painter.setFrameShadow(QFrame.Plain)
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

	def update_image(self,top_left,bottom_right):
		img_copy = self.original_image.copy()

		top_left = (top_left.x(),top_left.y())
		bottom_right = (bottom_right.x(),bottom_right.y())

		cv2.rectangle(img_copy,top_left,bottom_right,(0,0,255),1)
		cv2.imshow("",img_copy)

	def add_new_field(self):
		name = self.field_line_edit.text()

		if name not in self.existing_fields:
			
			self.existing_fields.append(name)
			self.locations.append(self.form_image_painter.get_rect_position())

			self.listWidget.addItem(name)
			self.update_image(self.locations[-1][0],self.locations[-1][1])

		else:
			msg = QMessageBox()
			msg.setText("Field name already existss")
			msg.setWindowTitle("Error")
			msg.exec_()


	def exit(self):
		print("Exiting")
		quit(0)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	hwapp = HandWritingApp()
	hwapp.show()
	sys.exit(app.exec_())