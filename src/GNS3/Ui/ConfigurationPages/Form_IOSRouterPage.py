#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_IOSRouterPage.ui'
#
# Created: Tue Sep 25 17:40:54 2007
#      by: PyQt4 UI code generator 4-snapshot-20070701
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_IOSRouterPage(object):
    def setupUi(self, IOSRouterPage):
        IOSRouterPage.setObjectName("IOSRouterPage")
        IOSRouterPage.resize(QtCore.QSize(QtCore.QRect(0,0,397,309).size()).expandedTo(IOSRouterPage.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(IOSRouterPage)
        self.vboxlayout.setObjectName("vboxlayout")

        self.tabWidget = QtGui.QTabWidget(IOSRouterPage)
        self.tabWidget.setObjectName("tabWidget")

        self.General = QtGui.QWidget()
        self.General.setObjectName("General")

        self.gridlayout = QtGui.QGridLayout(self.General)
        self.gridlayout.setObjectName("gridlayout")

        self.label_5 = QtGui.QLabel(self.General)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,0,0,1,1)

        self.comboBoxIOS = QtGui.QComboBox(self.General)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxIOS.sizePolicy().hasHeightForWidth())
        self.comboBoxIOS.setSizePolicy(sizePolicy)
        self.comboBoxIOS.setObjectName("comboBoxIOS")
        self.gridlayout.addWidget(self.comboBoxIOS,0,1,1,2)

        self.label_18 = QtGui.QLabel(self.General)
        self.label_18.setObjectName("label_18")
        self.gridlayout.addWidget(self.label_18,1,0,1,1)

        self.lineEditStartupConfig = QtGui.QLineEdit(self.General)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditStartupConfig.sizePolicy().hasHeightForWidth())
        self.lineEditStartupConfig.setSizePolicy(sizePolicy)
        self.lineEditStartupConfig.setObjectName("lineEditStartupConfig")
        self.gridlayout.addWidget(self.lineEditStartupConfig,1,1,1,1)

        self.pushButtonStartupConfig = QtGui.QPushButton(self.General)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonStartupConfig.sizePolicy().hasHeightForWidth())
        self.pushButtonStartupConfig.setSizePolicy(sizePolicy)
        self.pushButtonStartupConfig.setMaximumSize(QtCore.QSize(31,27))
        self.pushButtonStartupConfig.setObjectName("pushButtonStartupConfig")
        self.gridlayout.addWidget(self.pushButtonStartupConfig,1,2,1,1)

        self.label_13 = QtGui.QLabel(self.General)
        self.label_13.setObjectName("label_13")
        self.gridlayout.addWidget(self.label_13,2,0,1,1)

        self.spinBoxConsolePort = QtGui.QSpinBox(self.General)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxConsolePort.sizePolicy().hasHeightForWidth())
        self.spinBoxConsolePort.setSizePolicy(sizePolicy)
        self.spinBoxConsolePort.setMinimum(0)
        self.spinBoxConsolePort.setMaximum(65535)
        self.spinBoxConsolePort.setProperty("value",QtCore.QVariant(0))
        self.spinBoxConsolePort.setObjectName("spinBoxConsolePort")
        self.gridlayout.addWidget(self.spinBoxConsolePort,2,1,1,2)

        self.label = QtGui.QLabel(self.General)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,3,0,1,1)

        self.comboBoxMidplane = QtGui.QComboBox(self.General)
        self.comboBoxMidplane.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxMidplane.sizePolicy().hasHeightForWidth())
        self.comboBoxMidplane.setSizePolicy(sizePolicy)
        self.comboBoxMidplane.setObjectName("comboBoxMidplane")
        self.gridlayout.addWidget(self.comboBoxMidplane,3,1,1,2)

        self.label_2 = QtGui.QLabel(self.General)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,4,0,1,1)

        self.comboBoxNPE = QtGui.QComboBox(self.General)
        self.comboBoxNPE.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxNPE.sizePolicy().hasHeightForWidth())
        self.comboBoxNPE.setSizePolicy(sizePolicy)
        self.comboBoxNPE.setObjectName("comboBoxNPE")
        self.gridlayout.addWidget(self.comboBoxNPE,4,1,1,2)

        spacerItem = QtGui.QSpacerItem(331,16,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem,5,0,1,3)
        self.tabWidget.addTab(self.General,"")

        self.MemoriesDisks = QtGui.QWidget()
        self.MemoriesDisks.setObjectName("MemoriesDisks")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.MemoriesDisks)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.groupBox_2 = QtGui.QGroupBox(self.MemoriesDisks)
        self.groupBox_2.setObjectName("groupBox_2")

        self.gridlayout1 = QtGui.QGridLayout(self.groupBox_2)
        self.gridlayout1.setObjectName("gridlayout1")

        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridlayout1.addWidget(self.label_7,0,0,1,1)

        self.spinBoxRamSize = QtGui.QSpinBox(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxRamSize.sizePolicy().hasHeightForWidth())
        self.spinBoxRamSize.setSizePolicy(sizePolicy)
        self.spinBoxRamSize.setMaximum(4096)
        self.spinBoxRamSize.setSingleStep(4)
        self.spinBoxRamSize.setProperty("value",QtCore.QVariant(128))
        self.spinBoxRamSize.setObjectName("spinBoxRamSize")
        self.gridlayout1.addWidget(self.spinBoxRamSize,0,1,1,1)

        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridlayout1.addWidget(self.label_8,1,0,1,1)

        self.spinBoxRomSize = QtGui.QSpinBox(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxRomSize.sizePolicy().hasHeightForWidth())
        self.spinBoxRomSize.setSizePolicy(sizePolicy)
        self.spinBoxRomSize.setMaximum(4096)
        self.spinBoxRomSize.setSingleStep(4)
        self.spinBoxRomSize.setProperty("value",QtCore.QVariant(4))
        self.spinBoxRomSize.setObjectName("spinBoxRomSize")
        self.gridlayout1.addWidget(self.spinBoxRomSize,1,1,1,1)

        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridlayout1.addWidget(self.label_9,2,0,1,1)

        self.spinBoxNvramSize = QtGui.QSpinBox(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxNvramSize.sizePolicy().hasHeightForWidth())
        self.spinBoxNvramSize.setSizePolicy(sizePolicy)
        self.spinBoxNvramSize.setMaximum(4096)
        self.spinBoxNvramSize.setSingleStep(4)
        self.spinBoxNvramSize.setProperty("value",QtCore.QVariant(128))
        self.spinBoxNvramSize.setObjectName("spinBoxNvramSize")
        self.gridlayout1.addWidget(self.spinBoxNvramSize,2,1,1,1)
        self.vboxlayout1.addWidget(self.groupBox_2)

        self.groupBox_6 = QtGui.QGroupBox(self.MemoriesDisks)
        self.groupBox_6.setObjectName("groupBox_6")

        self.gridlayout2 = QtGui.QGridLayout(self.groupBox_6)
        self.gridlayout2.setObjectName("gridlayout2")

        self.label_10 = QtGui.QLabel(self.groupBox_6)
        self.label_10.setObjectName("label_10")
        self.gridlayout2.addWidget(self.label_10,0,0,1,1)

        self.spinBoxPcmciaDisk0Size = QtGui.QSpinBox(self.groupBox_6)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxPcmciaDisk0Size.sizePolicy().hasHeightForWidth())
        self.spinBoxPcmciaDisk0Size.setSizePolicy(sizePolicy)
        self.spinBoxPcmciaDisk0Size.setSingleStep(4)
        self.spinBoxPcmciaDisk0Size.setObjectName("spinBoxPcmciaDisk0Size")
        self.gridlayout2.addWidget(self.spinBoxPcmciaDisk0Size,0,1,1,1)

        self.label_11 = QtGui.QLabel(self.groupBox_6)
        self.label_11.setObjectName("label_11")
        self.gridlayout2.addWidget(self.label_11,1,0,1,1)

        self.spinBoxPcmciaDisk1Size = QtGui.QSpinBox(self.groupBox_6)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxPcmciaDisk1Size.sizePolicy().hasHeightForWidth())
        self.spinBoxPcmciaDisk1Size.setSizePolicy(sizePolicy)
        self.spinBoxPcmciaDisk1Size.setSingleStep(4)
        self.spinBoxPcmciaDisk1Size.setObjectName("spinBoxPcmciaDisk1Size")
        self.gridlayout2.addWidget(self.spinBoxPcmciaDisk1Size,1,1,1,1)
        self.vboxlayout1.addWidget(self.groupBox_6)

        spacerItem1 = QtGui.QSpacerItem(20,21,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem1)
        self.tabWidget.addTab(self.MemoriesDisks,"")

        self.Slots = QtGui.QWidget()
        self.Slots.setObjectName("Slots")

        self.gridlayout3 = QtGui.QGridLayout(self.Slots)
        self.gridlayout3.setObjectName("gridlayout3")

        self.label_6 = QtGui.QLabel(self.Slots)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridlayout3.addWidget(self.label_6,0,0,1,1)

        self.comboBoxSlot0 = QtGui.QComboBox(self.Slots)
        self.comboBoxSlot0.setObjectName("comboBoxSlot0")
        self.gridlayout3.addWidget(self.comboBoxSlot0,0,1,1,1)

        self.label_12 = QtGui.QLabel(self.Slots)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridlayout3.addWidget(self.label_12,1,0,1,1)

        self.comboBoxSlot1 = QtGui.QComboBox(self.Slots)
        self.comboBoxSlot1.setObjectName("comboBoxSlot1")
        self.gridlayout3.addWidget(self.comboBoxSlot1,1,1,1,1)

        self.label_15 = QtGui.QLabel(self.Slots)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.gridlayout3.addWidget(self.label_15,2,0,1,1)

        self.comboBoxSlot2 = QtGui.QComboBox(self.Slots)
        self.comboBoxSlot2.setObjectName("comboBoxSlot2")
        self.gridlayout3.addWidget(self.comboBoxSlot2,2,1,1,1)

        self.label_19 = QtGui.QLabel(self.Slots)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.gridlayout3.addWidget(self.label_19,3,0,1,1)

        self.comboBoxSlot3 = QtGui.QComboBox(self.Slots)
        self.comboBoxSlot3.setObjectName("comboBoxSlot3")
        self.gridlayout3.addWidget(self.comboBoxSlot3,3,1,1,1)

        self.label_23 = QtGui.QLabel(self.Slots)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setObjectName("label_23")
        self.gridlayout3.addWidget(self.label_23,4,0,1,1)

        self.comboBoxSlot4 = QtGui.QComboBox(self.Slots)
        self.comboBoxSlot4.setObjectName("comboBoxSlot4")
        self.gridlayout3.addWidget(self.comboBoxSlot4,4,1,1,1)

        self.label_26 = QtGui.QLabel(self.Slots)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setObjectName("label_26")
        self.gridlayout3.addWidget(self.label_26,5,0,1,1)

        self.comboBoxSlot5 = QtGui.QComboBox(self.Slots)
        self.comboBoxSlot5.setObjectName("comboBoxSlot5")
        self.gridlayout3.addWidget(self.comboBoxSlot5,5,1,1,1)

        self.label_28 = QtGui.QLabel(self.Slots)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setObjectName("label_28")
        self.gridlayout3.addWidget(self.label_28,6,0,1,1)

        self.comboBoxSlot6 = QtGui.QComboBox(self.Slots)
        self.comboBoxSlot6.setObjectName("comboBoxSlot6")
        self.gridlayout3.addWidget(self.comboBoxSlot6,6,1,1,1)

        spacerItem2 = QtGui.QSpacerItem(20,31,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout3.addItem(spacerItem2,7,1,1,1)
        self.tabWidget.addTab(self.Slots,"")

        self.Advanced = QtGui.QWidget()
        self.Advanced.setObjectName("Advanced")

        self.gridlayout4 = QtGui.QGridLayout(self.Advanced)
        self.gridlayout4.setObjectName("gridlayout4")

        self.checkBoxDeleteFiles = QtGui.QCheckBox(self.Advanced)
        self.checkBoxDeleteFiles.setObjectName("checkBoxDeleteFiles")
        self.gridlayout4.addWidget(self.checkBoxDeleteFiles,0,0,1,2)

        self.checkBoxMapped = QtGui.QCheckBox(self.Advanced)
        self.checkBoxMapped.setChecked(True)
        self.checkBoxMapped.setObjectName("checkBoxMapped")
        self.gridlayout4.addWidget(self.checkBoxMapped,1,0,1,1)

        spacerItem3 = QtGui.QSpacerItem(121,23,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout4.addItem(spacerItem3,1,1,1,1)

        self.label_25 = QtGui.QLabel(self.Advanced)
        self.label_25.setObjectName("label_25")
        self.gridlayout4.addWidget(self.label_25,2,0,1,1)

        self.lineEditConfreg = QtGui.QLineEdit(self.Advanced)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditConfreg.sizePolicy().hasHeightForWidth())
        self.lineEditConfreg.setSizePolicy(sizePolicy)
        self.lineEditConfreg.setObjectName("lineEditConfreg")
        self.gridlayout4.addWidget(self.lineEditConfreg,2,1,1,1)

        self.label_3 = QtGui.QLabel(self.Advanced)
        self.label_3.setObjectName("label_3")
        self.gridlayout4.addWidget(self.label_3,3,0,1,1)

        self.lineEditMAC = QtGui.QLineEdit(self.Advanced)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditMAC.sizePolicy().hasHeightForWidth())
        self.lineEditMAC.setSizePolicy(sizePolicy)
        self.lineEditMAC.setObjectName("lineEditMAC")
        self.gridlayout4.addWidget(self.lineEditMAC,3,1,1,1)

        self.label_31 = QtGui.QLabel(self.Advanced)
        self.label_31.setObjectName("label_31")
        self.gridlayout4.addWidget(self.label_31,4,0,1,1)

        self.spinBoxExecArea = QtGui.QSpinBox(self.Advanced)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxExecArea.sizePolicy().hasHeightForWidth())
        self.spinBoxExecArea.setSizePolicy(sizePolicy)
        self.spinBoxExecArea.setMaximum(4096)
        self.spinBoxExecArea.setSingleStep(4)
        self.spinBoxExecArea.setProperty("value",QtCore.QVariant(64))
        self.spinBoxExecArea.setObjectName("spinBoxExecArea")
        self.gridlayout4.addWidget(self.spinBoxExecArea,4,1,1,1)

        self.label_22 = QtGui.QLabel(self.Advanced)
        self.label_22.setObjectName("label_22")
        self.gridlayout4.addWidget(self.label_22,5,0,1,1)

        self.spinBoxIomem = QtGui.QSpinBox(self.Advanced)
        self.spinBoxIomem.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxIomem.sizePolicy().hasHeightForWidth())
        self.spinBoxIomem.setSizePolicy(sizePolicy)
        self.spinBoxIomem.setMaximum(100)
        self.spinBoxIomem.setSingleStep(5)
        self.spinBoxIomem.setProperty("value",QtCore.QVariant(5))
        self.spinBoxIomem.setObjectName("spinBoxIomem")
        self.gridlayout4.addWidget(self.spinBoxIomem,5,1,1,1)

        spacerItem4 = QtGui.QSpacerItem(262,41,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout4.addItem(spacerItem4,6,1,1,1)
        self.tabWidget.addTab(self.Advanced,"")
        self.vboxlayout.addWidget(self.tabWidget)

        self.retranslateUi(IOSRouterPage)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(IOSRouterPage)

    def retranslateUi(self, IOSRouterPage):
        IOSRouterPage.setWindowTitle(QtGui.QApplication.translate("IOSRouterPage", "Router configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("IOSRouterPage", "IOS image:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("IOSRouterPage", "Startup-config:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonStartupConfig.setText(QtGui.QApplication.translate("IOSRouterPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("IOSRouterPage", "Console port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("IOSRouterPage", "Midplane:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("IOSRouterPage", "NPE:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.General), QtGui.QApplication.translate("IOSRouterPage", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("IOSRouterPage", "Memories", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("IOSRouterPage", "RAM size:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxRamSize.setSuffix(QtGui.QApplication.translate("IOSRouterPage", " MB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("IOSRouterPage", "ROM size:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxRomSize.setSuffix(QtGui.QApplication.translate("IOSRouterPage", " MB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("IOSRouterPage", "NVRAM size:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxNvramSize.setSuffix(QtGui.QApplication.translate("IOSRouterPage", " MB", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("IOSRouterPage", "Disks", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("IOSRouterPage", "PCMCIA disk0 size:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxPcmciaDisk0Size.setSuffix(QtGui.QApplication.translate("IOSRouterPage", " MB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("IOSRouterPage", "PCMCIA disk1 size:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxPcmciaDisk1Size.setSuffix(QtGui.QApplication.translate("IOSRouterPage", " MB", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MemoriesDisks), QtGui.QApplication.translate("IOSRouterPage", "Memories and disks", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("IOSRouterPage", "slot0:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("IOSRouterPage", "slot1:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("IOSRouterPage", "slot2:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("IOSRouterPage", "slot3:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("IOSRouterPage", "slot4:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("IOSRouterPage", "slot5:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("IOSRouterPage", "slot6:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Slots), QtGui.QApplication.translate("IOSRouterPage", "Slots", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxDeleteFiles.setText(QtGui.QApplication.translate("IOSRouterPage", "Delete nvram/flash/log files when stopping emulation", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxMapped.setText(QtGui.QApplication.translate("IOSRouterPage", "Use mmap", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("IOSRouterPage", "confreg:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditConfreg.setText(QtGui.QApplication.translate("IOSRouterPage", "0x2102", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("IOSRouterPage", "Base MAC :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("IOSRouterPage", "exec area:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxExecArea.setSuffix(QtGui.QApplication.translate("IOSRouterPage", " MB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("IOSRouterPage", "iomem :", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxIomem.setSuffix(QtGui.QApplication.translate("IOSRouterPage", " %", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Advanced), QtGui.QApplication.translate("IOSRouterPage", "Advanced", None, QtGui.QApplication.UnicodeUTF8))
