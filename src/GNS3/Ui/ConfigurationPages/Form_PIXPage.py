# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_PIXPage.ui'
#
# Created: Mon Sep 10 03:32:27 2012
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PIXPage(object):
    def setupUi(self, PIXPage):
        PIXPage.setObjectName(_fromUtf8("PIXPage"))
        PIXPage.resize(419, 453)
        self.gridLayout = QtGui.QGridLayout(PIXPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_17 = QtGui.QLabel(PIXPage)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.lineEditImage = QtGui.QLineEdit(PIXPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditImage.sizePolicy().hasHeightForWidth())
        self.lineEditImage.setSizePolicy(sizePolicy)
        self.lineEditImage.setObjectName(_fromUtf8("lineEditImage"))
        self.gridLayout.addWidget(self.lineEditImage, 0, 1, 1, 1)
        self.pushButtonImageBrowser = QtGui.QPushButton(PIXPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonImageBrowser.sizePolicy().hasHeightForWidth())
        self.pushButtonImageBrowser.setSizePolicy(sizePolicy)
        self.pushButtonImageBrowser.setMaximumSize(QtCore.QSize(31, 27))
        self.pushButtonImageBrowser.setObjectName(_fromUtf8("pushButtonImageBrowser"))
        self.gridLayout.addWidget(self.pushButtonImageBrowser, 0, 2, 1, 1)
        self.label_24 = QtGui.QLabel(PIXPage)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout.addWidget(self.label_24, 1, 0, 1, 1)
        self.spinBoxRamSize = QtGui.QSpinBox(PIXPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxRamSize.sizePolicy().hasHeightForWidth())
        self.spinBoxRamSize.setSizePolicy(sizePolicy)
        self.spinBoxRamSize.setMaximum(100000)
        self.spinBoxRamSize.setSingleStep(4)
        self.spinBoxRamSize.setProperty(_fromUtf8("value"), 128)
        self.spinBoxRamSize.setObjectName(_fromUtf8("spinBoxRamSize"))
        self.gridLayout.addWidget(self.spinBoxRamSize, 1, 1, 1, 2)
        self.label_37 = QtGui.QLabel(PIXPage)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout.addWidget(self.label_37, 2, 0, 1, 1)
        self.spinBoxNics = QtGui.QSpinBox(PIXPage)
        self.spinBoxNics.setMinimum(0)
        self.spinBoxNics.setMaximum(100000)
        self.spinBoxNics.setSingleStep(1)
        self.spinBoxNics.setProperty(_fromUtf8("value"), 6)
        self.spinBoxNics.setObjectName(_fromUtf8("spinBoxNics"))
        self.gridLayout.addWidget(self.spinBoxNics, 2, 1, 1, 2)
        self.label_26 = QtGui.QLabel(PIXPage)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout.addWidget(self.label_26, 3, 0, 1, 1)
        self.comboBoxNIC = QtGui.QComboBox(PIXPage)
        self.comboBoxNIC.setEnabled(True)
        self.comboBoxNIC.setObjectName(_fromUtf8("comboBoxNIC"))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBoxNIC, 3, 1, 1, 2)
        self.label_8 = QtGui.QLabel(PIXPage)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.lineEditOptions = QtGui.QLineEdit(PIXPage)
        self.lineEditOptions.setEnabled(True)
        self.lineEditOptions.setObjectName(_fromUtf8("lineEditOptions"))
        self.gridLayout.addWidget(self.lineEditOptions, 4, 1, 1, 2)
        self.label_20 = QtGui.QLabel(PIXPage)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout.addWidget(self.label_20, 5, 0, 1, 1)
        self.lineEditKey = QtGui.QLineEdit(PIXPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditKey.sizePolicy().hasHeightForWidth())
        self.lineEditKey.setSizePolicy(sizePolicy)
        self.lineEditKey.setObjectName(_fromUtf8("lineEditKey"))
        self.gridLayout.addWidget(self.lineEditKey, 5, 1, 1, 2)
        self.label_21 = QtGui.QLabel(PIXPage)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout.addWidget(self.label_21, 6, 0, 1, 1)
        self.lineEditSerial = QtGui.QLineEdit(PIXPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSerial.sizePolicy().hasHeightForWidth())
        self.lineEditSerial.setSizePolicy(sizePolicy)
        self.lineEditSerial.setObjectName(_fromUtf8("lineEditSerial"))
        self.gridLayout.addWidget(self.lineEditSerial, 6, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 281, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 1, 1, 1)

        self.retranslateUi(PIXPage)
        self.comboBoxNIC.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(PIXPage)

    def retranslateUi(self, PIXPage):
        PIXPage.setWindowTitle(QtGui.QApplication.translate("PIXPage", "Firewall configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("PIXPage", "PIX Image:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonImageBrowser.setText(QtGui.QApplication.translate("PIXPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("PIXPage", "RAM:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxRamSize.setSuffix(QtGui.QApplication.translate("PIXPage", " MiB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("PIXPage", "Number of NICs:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("PIXPage", "NIC model:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(0, QtGui.QApplication.translate("PIXPage", "ne2k_pci", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(1, QtGui.QApplication.translate("PIXPage", "i82551", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(2, QtGui.QApplication.translate("PIXPage", "i82557b", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(3, QtGui.QApplication.translate("PIXPage", "i82559er", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(4, QtGui.QApplication.translate("PIXPage", "rtl8139", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(5, QtGui.QApplication.translate("PIXPage", "e1000", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(6, QtGui.QApplication.translate("PIXPage", "pcnet", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(7, QtGui.QApplication.translate("PIXPage", "virtio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("PIXPage", "Qemu Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("PIXPage", "Key:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("PIXPage", "Serial:", None, QtGui.QApplication.UnicodeUTF8))

