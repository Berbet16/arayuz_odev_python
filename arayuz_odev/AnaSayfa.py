# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnaSayfa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AnaSayfa(object):
    def setupUi(self, AnaSayfa):
        AnaSayfa.setObjectName("AnaSayfa")
        AnaSayfa.resize(800, 597)
        self.centralwidget = QtWidgets.QWidget(AnaSayfa)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(230, 10, 561, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setText("")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setText("")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setText("")
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_1.setText("")
        self.label_1.setScaledContents(True)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 100, 200, 400))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.open_image = QtWidgets.QPushButton(self.groupBox)
        self.open_image.setGeometry(QtCore.QRect(15, 50, 170, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.open_image.setFont(font)
        self.open_image.setObjectName("open_image")
        self.desired_image = QtWidgets.QPushButton(self.groupBox)
        self.desired_image.setGeometry(QtCore.QRect(15, 110, 170, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.desired_image.setFont(font)
        self.desired_image.setObjectName("desired_image")
        self.histogram = QtWidgets.QPushButton(self.groupBox)
        self.histogram.setGeometry(QtCore.QRect(15, 170, 170, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.histogram.setFont(font)
        self.histogram.setObjectName("histogram")
        self.equalization = QtWidgets.QPushButton(self.groupBox)
        self.equalization.setGeometry(QtCore.QRect(15, 230, 170, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.equalization.setFont(font)
        self.equalization.setObjectName("equalization")
        self.specification = QtWidgets.QPushButton(self.groupBox)
        self.specification.setGeometry(QtCore.QRect(15, 290, 170, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.specification.setFont(font)
        self.specification.setObjectName("specification")
        AnaSayfa.setCentralWidget(self.centralwidget)

        self.retranslateUi(AnaSayfa)
        self.open_image.clicked.connect(AnaSayfa.RESIM_AC)
        self.desired_image.clicked.connect(AnaSayfa.RESIM_AC2)
        self.histogram.clicked.connect(AnaSayfa.HISTOGRAM)
        self.equalization.clicked.connect(AnaSayfa.EQUALIZATION)
        self.specification.clicked.connect(AnaSayfa.SPECIFICATION)
        QtCore.QMetaObject.connectSlotsByName(AnaSayfa)

    def retranslateUi(self, AnaSayfa):
        _translate = QtCore.QCoreApplication.translate
        AnaSayfa.setWindowTitle(_translate("AnaSayfa", "Ana Sayfa"))
        self.open_image.setText(_translate("AnaSayfa", "Open Image File"))
        self.desired_image.setText(_translate("AnaSayfa", "Open Desired Image"))
        self.histogram.setText(_translate("AnaSayfa", "Histogram"))
        self.equalization.setText(_translate("AnaSayfa", "Equalization"))
        self.specification.setText(_translate("AnaSayfa", "Specification"))

