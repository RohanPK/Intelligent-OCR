from  UI.formtemplate import Ui_FormTemplate
from UI.painter import Image_Painter
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import cv2
import numpy as np
import pickle

class HandWritingApp(QMainWindow, Ui_FormTemplate):
	def __init__(self):
		QMainWindow.__init__(self)
		Ui_FormTemplate.__init__(self)
		self.setupUi(self)

		# Height and width
		self.height = self.form_image.height()
		self.width = self.form_image.width()

		self.setFixedSize(817, 842)

		# Buttons and functions mapped
		self.actionNew.triggered.connect(self.new_template)
		self.actionLoadImage.triggered.connect(self.load_image)
		self.actionExit.triggered.connect(self.exit)

		self.actionSaveTemplate.triggered.connect(self.save_template)
		self.actionLoadTemplate.triggered.connect(self.load_template)

		self.menuRun.triggered.connect(self.start_detection)


		self.add_field_object.clicked.connect(self.add_new_field)
		self.removeButton.clicked.connect(self.remove_field)

		# Name,location and type of each field saved as a csv later
		self.existing_fields = []
		self.locations = []
		self.field_type = []

		# Add a painter on top of the image window
		self.form_image_painter = Image_Painter(self.centralwidget)
		self.form_image_painter.setGeometry(self.form_image.geometry())
		self.form_image_painter.setFrameShape(QFrame.Panel)
		self.form_image_painter.setFrameShadow(QFrame.Plain)
		self.form_image_painter.setText("")
		self.form_image_painter.setObjectName("form_image_painter")


		default_image_path = "image.png"

		# Load default image
		self.original_image = cv2.imread(default_image_path)
		self.display_image = self.original_image.copy()

		blank = QPixmap(default_image_path)
		self.form_image.setPixmap(blank)
		self.form_image.show()

	def new_template(self):
		self.existing_fields = []
		self.locations = []
		self.field_type = []
		self.tableWidget.setRowCount(0)
		origin = QPoint(0,0)
		self.display_image = self.original_image.copy()
		self.update_image(origin,origin)

	def save_template(self):
		fname =  QFileDialog.getSaveFileName()
		with open(fname[0]+'.pickle', 'wb') as handle:
			pickle.dump((self.original_image,self.existing_fields,self.locations,self.field_type), handle, protocol=pickle.HIGHEST_PROTOCOL)

	def load_template(self):
		self.new_template()
		fname = QFileDialog.getOpenFileName(self, 'Open file',os.getcwd(),"Template files (*.pickle)")
		if fname[0] != "":
			self.original_image,self.existing_fields,self.locations,self.field_type = pickle.load(open(fname[0],'rb'))
			self.display_image = self.original_image.copy()

			for index,item in enumerate(self.existing_fields):
				rowPosition = self.tableWidget.rowCount()
				self.tableWidget.insertRow(rowPosition)
				self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(self.existing_fields[index]))
				self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(self.field_type[index]))

				self.form_image_painter.reset_position()
				self.update_image(self.locations[index][0], self.locations[index][1])

	def remove_field(self):
		selected_row_indexes = self.tableWidget.selectionModel().selectedIndexes()

		for index in selected_row_indexes:
			row_number = index.row()

			self.existing_fields.pop(row_number)
			self.locations.pop(row_number)
			self.field_type.pop(row_number)

			self.tableWidget.removeRow(row_number)

			self.display_image = self.original_image.copy()
			img = self.display_image
			qtimage = QImage(img, img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888)
			self.form_image.setPixmap(QPixmap(qtimage))
			self.form_image.show()

			for index,name in enumerate(self.existing_fields):
				self.update_image(self.locations[index][0],self.locations[index][1])

	def load_image(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file',os.getcwd(),"Image files (*.jpg *.png *.gif)")
		if fname:
			self.original_image = cv2.imread(fname[0])
			self.display_image = self.original_image.copy()
			self.form_image.setPixmap(QPixmap(fname[0]))
			self.form_image.show()

	def update_image(self,top_left,bottom_right):
		img = self.display_image

		top_left = (top_left.x(),top_left.y())
		bottom_right = (bottom_right.x(),bottom_right.y())

		cv2.rectangle(img,top_left,bottom_right,(0,0,255),1)


		qtimage = QImage(img, img.shape[1],img.shape[0], img.shape[1] * 3,QImage.Format_RGB888)
		self.form_image.setPixmap(QPixmap(qtimage))
		self.form_image.show()


	def add_new_field(self):
		name = self.field_line_edit.text()

		if name not in self.existing_fields:
			
			self.existing_fields.append(name)
			self.locations.append(self.form_image_painter.get_rect_position())

			if self.radio_single_line.isChecked():
				self.field_type.append("Line")
			else:
				self.field_type.append("Paragraph")

			rowPosition = self.tableWidget.rowCount()
			self.tableWidget.insertRow(rowPosition)
			self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(name))
			self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(self.field_type[-1]))

			self.form_image_painter.reset_position()
			self.update_image(self.locations[-1][0],self.locations[-1][1])

		else:
			msg = QMessageBox()
			msg.setText("Field name already exists")
			msg.setWindowTitle("Error")
			msg.exec_()

	def start_detection(self):
		fname = QFileDialog.getOpenFileName(self, 'Open folder',os.getcwd(),"Directory (*.dir)")

		if fname[0] != "":
			print(fname)


	def exit(self):
		print("Exiting")
		quit(0)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	hwapp = HandWritingApp()
	hwapp.show()
	sys.exit(app.exec_())