# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_IDSPage.ui'
#
# Created: Fri Jan  4 19:08:03 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_IDSPage(object):
    def setupUi(self, IDSPage):
        IDSPage.setObjectName(_fromUtf8("IDSPage"))
        IDSPage.resize(419, 453)
        IDSPage.setWindowTitle(QtGui.QApplication.translate("IDSPage", "IDS configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(IDSPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_17 = QtGui.QLabel(IDSPage)
        self.label_17.setText(QtGui.QApplication.translate("IDSPage", "IDS Image 1 (hda):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 2)
        self.lineEditImage1 = QtGui.QLineEdit(IDSPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditImage1.sizePolicy().hasHeightForWidth())
        self.lineEditImage1.setSizePolicy(sizePolicy)
        self.lineEditImage1.setObjectName(_fromUtf8("lineEditImage1"))
        self.gridLayout.addWidget(self.lineEditImage1, 0, 2, 1, 1)
        self.pushButtonImage1Browser = QtGui.QPushButton(IDSPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonImage1Browser.sizePolicy().hasHeightForWidth())
        self.pushButtonImage1Browser.setSizePolicy(sizePolicy)
        self.pushButtonImage1Browser.setMaximumSize(QtCore.QSize(31, 27))
        self.pushButtonImage1Browser.setText(QtGui.QApplication.translate("IDSPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonImage1Browser.setObjectName(_fromUtf8("pushButtonImage1Browser"))
        self.gridLayout.addWidget(self.pushButtonImage1Browser, 0, 3, 1, 1)
        self.label_18 = QtGui.QLabel(IDSPage)
        self.label_18.setText(QtGui.QApplication.translate("IDSPage", "IDS Image 2 (hdb):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 1, 0, 1, 2)
        self.lineEditImage2 = QtGui.QLineEdit(IDSPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditImage2.sizePolicy().hasHeightForWidth())
        self.lineEditImage2.setSizePolicy(sizePolicy)
        self.lineEditImage2.setObjectName(_fromUtf8("lineEditImage2"))
        self.gridLayout.addWidget(self.lineEditImage2, 1, 2, 1, 1)
        self.pushButtonImage2Browser = QtGui.QPushButton(IDSPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonImage2Browser.sizePolicy().hasHeightForWidth())
        self.pushButtonImage2Browser.setSizePolicy(sizePolicy)
        self.pushButtonImage2Browser.setMaximumSize(QtCore.QSize(31, 27))
        self.pushButtonImage2Browser.setText(QtGui.QApplication.translate("IDSPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonImage2Browser.setObjectName(_fromUtf8("pushButtonImage2Browser"))
        self.gridLayout.addWidget(self.pushButtonImage2Browser, 1, 3, 1, 1)
        self.label_24 = QtGui.QLabel(IDSPage)
        self.label_24.setText(QtGui.QApplication.translate("IDSPage", "RAM:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout.addWidget(self.label_24, 2, 0, 1, 1)
        self.spinBoxRamSize = QtGui.QSpinBox(IDSPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxRamSize.sizePolicy().hasHeightForWidth())
        self.spinBoxRamSize.setSizePolicy(sizePolicy)
        self.spinBoxRamSize.setSuffix(QtGui.QApplication.translate("IDSPage", " MiB", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxRamSize.setMaximum(100000)
        self.spinBoxRamSize.setSingleStep(4)
        self.spinBoxRamSize.setProperty("value", 96)
        self.spinBoxRamSize.setObjectName(_fromUtf8("spinBoxRamSize"))
        self.gridLayout.addWidget(self.spinBoxRamSize, 2, 2, 1, 2)
        self.label_37 = QtGui.QLabel(IDSPage)
        self.label_37.setText(QtGui.QApplication.translate("IDSPage", "Number of NICs:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout.addWidget(self.label_37, 3, 0, 1, 1)
        self.spinBoxNics = QtGui.QSpinBox(IDSPage)
        self.spinBoxNics.setMinimum(0)
        self.spinBoxNics.setMaximum(100000)
        self.spinBoxNics.setSingleStep(1)
        self.spinBoxNics.setProperty("value", 6)
        self.spinBoxNics.setObjectName(_fromUtf8("spinBoxNics"))
        self.gridLayout.addWidget(self.spinBoxNics, 3, 2, 1, 2)
        self.label_26 = QtGui.QLabel(IDSPage)
        self.label_26.setText(QtGui.QApplication.translate("IDSPage", "NIC model:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout.addWidget(self.label_26, 4, 0, 1, 1)
        self.comboBoxNIC = QtGui.QComboBox(IDSPage)
        self.comboBoxNIC.setEnabled(True)
        self.comboBoxNIC.setObjectName(_fromUtf8("comboBoxNIC"))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(0, QtGui.QApplication.translate("IDSPage", "ne2k_pci", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(1, QtGui.QApplication.translate("IDSPage", "i82551", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(2, QtGui.QApplication.translate("IDSPage", "i82557b", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(3, QtGui.QApplication.translate("IDSPage", "i82559er", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(4, QtGui.QApplication.translate("IDSPage", "rtl8139", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(5, QtGui.QApplication.translate("IDSPage", "e1000", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(6, QtGui.QApplication.translate("IDSPage", "pcnet", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.addItem(_fromUtf8(""))
        self.comboBoxNIC.setItemText(7, QtGui.QApplication.translate("IDSPage", "virtio", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout.addWidget(self.comboBoxNIC, 4, 2, 1, 2)
        self.label_8 = QtGui.QLabel(IDSPage)
        self.label_8.setText(QtGui.QApplication.translate("IDSPage", "Qemu Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.lineEditOptions = QtGui.QLineEdit(IDSPage)
        self.lineEditOptions.setEnabled(True)
        self.lineEditOptions.setObjectName(_fromUtf8("lineEditOptions"))
        self.gridLayout.addWidget(self.lineEditOptions, 5, 2, 1, 2)
        self.checkBoxKVM = QtGui.QCheckBox(IDSPage)
        self.checkBoxKVM.setEnabled(True)
        self.checkBoxKVM.setText(QtGui.QApplication.translate("IDSPage", "Use KVM (Linux hosts only)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxKVM.setObjectName(_fromUtf8("checkBoxKVM"))
        self.gridLayout.addWidget(self.checkBoxKVM, 6, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(20, 281, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 4)

        self.retranslateUi(IDSPage)
        self.comboBoxNIC.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(IDSPage)

    def retranslateUi(self, IDSPage):
        pass

