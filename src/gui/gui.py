# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 149)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.edit_x = QtGui.QLineEdit(self.centralwidget)
        self.edit_x.setObjectName(_fromUtf8("edit_x"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.edit_x)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.edit_y = QtGui.QLineEdit(self.centralwidget)
        self.edit_y.setObjectName(_fromUtf8("edit_y"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.edit_y)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(20, 275, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pb_Plot_1 = QtGui.QPushButton(self.centralwidget)
        self.pb_Plot_1.setObjectName(_fromUtf8("pb_Plot_1"))
        self.horizontalLayout.addWidget(self.pb_Plot_1)
        self.pb_Plot_2 = QtGui.QPushButton(self.centralwidget)
        self.pb_Plot_2.setObjectName(_fromUtf8("pb_Plot_2"))
        self.horizontalLayout.addWidget(self.pb_Plot_2)
        self.pb_Schliessen = QtGui.QPushButton(self.centralwidget)
        self.pb_Schliessen.setObjectName(_fromUtf8("pb_Schliessen"))
        self.horizontalLayout.addWidget(self.pb_Schliessen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pb_Schliessen, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Gui", None))
        self.label.setText(_translate("MainWindow", "x-Werte", None))
        self.edit_x.setText(_translate("MainWindow", "range(1, 11, 1)", None))
        self.label_2.setText(_translate("MainWindow", "y-Werte", None))
        self.edit_y.setText(_translate("MainWindow", "[1, 2, 7, 2, 5, 4, 6, 2, 0, 5]", None))
        self.pb_Plot_1.setText(_translate("MainWindow", "Plot 1", None))
        self.pb_Plot_2.setText(_translate("MainWindow", "Plot 2", None))
        self.pb_Schliessen.setText(_translate("MainWindow", "Schließen", None))

