# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formtemplate.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormTemplate(object):
    def setupUi(self, FormTemplate):
        FormTemplate.setObjectName("FormTemplate")
        FormTemplate.resize(817, 842)
        self.centralwidget = QtWidgets.QWidget(FormTemplate)
        self.centralwidget.setObjectName("centralwidget")
        self.form_image = QtWidgets.QLabel(self.centralwidget)
        self.form_image.setGeometry(QtCore.QRect(0, 0, 541, 791))
        self.form_image.setFrameShape(QtWidgets.QFrame.Panel)
        self.form_image.setFrameShadow(QtWidgets.QFrame.Plain)
        self.form_image.setText("")
        self.form_image.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.form_image.setObjectName("form_image")
        self.add_field_object = QtWidgets.QPushButton(self.centralwidget)
        self.add_field_object.setGeometry(QtCore.QRect(690, 500, 89, 25))
        self.add_field_object.setObjectName("add_field_object")
        self.field_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.field_line_edit.setGeometry(QtCore.QRect(550, 500, 121, 25))
        self.field_line_edit.setObjectName("field_line_edit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(550, 0, 251, 431))
        self.listWidget.setObjectName("listWidget")
        FormTemplate.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FormTemplate)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 22))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuEdot = QtWidgets.QMenu(self.menubar)
        self.menuEdot.setObjectName("menuEdot")
        FormTemplate.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FormTemplate)
        self.statusbar.setObjectName("statusbar")
        FormTemplate.setStatusBar(self.statusbar)
        self.actionLoad_Template = QtWidgets.QAction(FormTemplate)
        self.actionLoad_Template.setObjectName("actionLoad_Template")
        self.actionSave_Template = QtWidgets.QAction(FormTemplate)
        self.actionSave_Template.setObjectName("actionSave_Template")
        self.actionExit = QtWidgets.QAction(FormTemplate)
        self.actionExit.setObjectName("actionExit")
        self.actionNew = QtWidgets.QAction(FormTemplate)
        self.actionNew.setObjectName("actionNew")
        self.menuFIle.addAction(self.actionNew)
        self.menuFIle.addAction(self.actionLoad_Template)
        self.menuFIle.addAction(self.actionSave_Template)
        self.menuFIle.addAction(self.actionExit)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuEdot.menuAction())

        self.retranslateUi(FormTemplate)
        QtCore.QMetaObject.connectSlotsByName(FormTemplate)

    def retranslateUi(self, FormTemplate):
        _translate = QtCore.QCoreApplication.translate
        FormTemplate.setWindowTitle(_translate("FormTemplate", "MainWindow"))
        self.add_field_object.setText(_translate("FormTemplate", "Add Field"))
        self.menuFIle.setTitle(_translate("FormTemplate", "File"))
        self.menuEdot.setTitle(_translate("FormTemplate", "Run"))
        self.actionLoad_Template.setText(_translate("FormTemplate", "Load"))
        self.actionSave_Template.setText(_translate("FormTemplate", "Save"))
        self.actionExit.setText(_translate("FormTemplate", "Exit"))
        self.actionNew.setText(_translate("FormTemplate", "New"))


