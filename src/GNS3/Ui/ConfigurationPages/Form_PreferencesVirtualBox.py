# -*- coding: utf-8 -*-
# vim: expandtab ts=4 sw=4 sts=4:

# Form implementation generated from reading ui file 'Form_PreferencesVirtualBox.ui'
#
# Created: Mon Jul  4 16:34:11 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PreferencesVirtualBox(object):
    def setupUi(self, PreferencesVirtualBox):
        PreferencesVirtualBox.setObjectName("PreferencesVirtualBox")
        PreferencesVirtualBox.resize(464, 464)
        self.verticalLayout_17 = QtGui.QVBoxLayout(PreferencesVirtualBox)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.tabWidget = QtGui.QTabWidget(PreferencesVirtualBox)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.P = QtGui.QGroupBox(self.tab)
        self.P.setEnabled(True)
        self.P.setObjectName("P")
        self.gridLayout_7 = QtGui.QGridLayout(self.P)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_3 = QtGui.QLabel(self.P)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEditVBoxwrapperPath = QtGui.QLineEdit(self.P)
        self.lineEditVBoxwrapperPath.setObjectName("lineEditVBoxwrapperPath")
        self.gridLayout_7.addWidget(self.lineEditVBoxwrapperPath, 0, 1, 1, 5)
        self.VBoxwrapperPath_browser = QtGui.QToolButton(self.P)
        self.VBoxwrapperPath_browser.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.VBoxwrapperPath_browser.setObjectName("VBoxwrapperPath_browser")
        self.gridLayout_7.addWidget(self.VBoxwrapperPath_browser, 0, 6, 1, 1)
        self.label_2 = QtGui.QLabel(self.P)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditVBoxwrapperWorkdir = QtGui.QLineEdit(self.P)
        self.lineEditVBoxwrapperWorkdir.setObjectName("lineEditVBoxwrapperWorkdir")
        self.gridLayout_7.addWidget(self.lineEditVBoxwrapperWorkdir, 1, 1, 1, 5)
        self.VBoxwrapperWorkdir_browser = QtGui.QToolButton(self.P)
        self.VBoxwrapperWorkdir_browser.setObjectName("VBoxwrapperWorkdir_browser")
        self.gridLayout_7.addWidget(self.VBoxwrapperWorkdir_browser, 1, 6, 1, 1)
        self.label_6 = QtGui.QLabel(self.P)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 8, 0, 1, 1)
        self.comboBoxBinding = QtGui.QComboBox(self.P)
        self.comboBoxBinding.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.comboBoxBinding.setObjectName("comboBoxBinding")
        self.gridLayout_7.addWidget(self.comboBoxBinding, 8, 1, 1, 6)
        self.label_30 = QtGui.QLabel(self.P)
        self.label_30.setEnabled(False)
        self.label_30.setObjectName("label_30")
        self.gridLayout_7.addWidget(self.label_30, 11, 0, 1, 1)
        self.baseConsole = QtGui.QSpinBox(self.P)
        self.baseConsole.setEnabled(False)
        self.baseConsole.setSuffix(" TCP")
        self.baseConsole.setMinimum(1)
        self.baseConsole.setMaximum(65535)
        self.baseConsole.setObjectName("baseConsole")
        self.gridLayout_7.addWidget(self.baseConsole, 11, 1, 1, 6)
        self.checkBoxEnableVBoxManager = QtGui.QCheckBox(self.P)
        self.checkBoxEnableVBoxManager.setChecked(True)
        self.checkBoxEnableVBoxManager.setObjectName("checkBoxEnableVBoxManager")
        self.gridLayout_7.addWidget(self.checkBoxEnableVBoxManager, 14, 0, 1, 3)
        self.checkBoxVBoxManagerImport = QtGui.QCheckBox(self.P)
        self.checkBoxVBoxManagerImport.setChecked(True)
        self.checkBoxVBoxManagerImport.setObjectName("checkBoxVBoxManagerImport")
        self.gridLayout_7.addWidget(self.checkBoxVBoxManagerImport, 15, 0, 1, 4)
        self.label_5 = QtGui.QLabel(self.P)
        self.label_5.setEnabled(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 16, 0, 1, 2)
        self.lineEditHostExternalVBox = QtGui.QLineEdit(self.P)
        self.lineEditHostExternalVBox.setObjectName("lineEditHostExternalVBox")
        self.gridLayout_7.addWidget(self.lineEditHostExternalVBox, 16, 2, 1, 2)
        self.pushButtonAddExternalVBoxwrapper = QtGui.QPushButton(self.P)
        self.pushButtonAddExternalVBoxwrapper.setObjectName("pushButtonAddExternalVBoxwrapper")
        self.gridLayout_7.addWidget(self.pushButtonAddExternalVBoxwrapper, 16, 4, 1, 1)
        self.pushButtonDeleteExternalVBoxwrapper = QtGui.QPushButton(self.P)
        self.pushButtonDeleteExternalVBoxwrapper.setObjectName("pushButtonDeleteExternalVBoxwrapper")
        self.gridLayout_7.addWidget(self.pushButtonDeleteExternalVBoxwrapper, 16, 5, 1, 2)
        self.label_36 = QtGui.QLabel(self.P)
        self.label_36.setObjectName("label_36")
        self.gridLayout_7.addWidget(self.label_36, 17, 0, 1, 3)
        self.comboBoxExternalVBoxwrappers = QtGui.QComboBox(self.P)
        self.comboBoxExternalVBoxwrappers.setObjectName("comboBoxExternalVBoxwrappers")
        self.gridLayout_7.addWidget(self.comboBoxExternalVBoxwrappers, 17, 3, 1, 4)
        self.checkBoxVBoxWrapperShowAdvancedOptions = QtGui.QCheckBox(self.P)
        self.checkBoxVBoxWrapperShowAdvancedOptions.setObjectName("checkBoxVBoxWrapperShowAdvancedOptions")
        self.gridLayout_7.addWidget(self.checkBoxVBoxWrapperShowAdvancedOptions, 4, 0, 1, 4)
        self.checkBoxVBoxShowAdvancedOptions = QtGui.QCheckBox(self.P)
        self.checkBoxVBoxShowAdvancedOptions.setObjectName("checkBoxVBoxShowAdvancedOptions")
        self.gridLayout_7.addWidget(self.checkBoxVBoxShowAdvancedOptions, 5, 0, 1, 4)
        self.label_35 = QtGui.QLabel(self.P)
        self.label_35.setObjectName("label_35")
        self.gridLayout_7.addWidget(self.label_35, 2, 0, 1, 1)
        self.port = QtGui.QSpinBox(self.P)
        self.port.setEnabled(True)
        self.port.setSuffix(" TCP")
        self.port.setMinimum(1)
        self.port.setMaximum(65535)
        self.port.setObjectName("port")
        self.gridLayout_7.addWidget(self.port, 2, 1, 1, 6)
        self.label_31 = QtGui.QLabel(self.P)
        self.label_31.setObjectName("label_31")
        self.gridLayout_7.addWidget(self.label_31, 3, 0, 1, 1)
        self.baseUDP = QtGui.QSpinBox(self.P)
        self.baseUDP.setEnabled(True)
        self.baseUDP.setSuffix(" UDP")
        self.baseUDP.setMinimum(1)
        self.baseUDP.setMaximum(65535)
        self.baseUDP.setObjectName("baseUDP")
        self.gridLayout_7.addWidget(self.baseUDP, 3, 1, 1, 6)
        self.verticalLayout_2.addWidget(self.P)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.pushButtonTestVBox = QtGui.QPushButton(self.tab)
        self.pushButtonTestVBox.setObjectName("pushButtonTestVBox")
        self.hboxlayout.addWidget(self.pushButtonTestVBox)
        self.labelVBoxStatus = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelVBoxStatus.sizePolicy().hasHeightForWidth())
        self.labelVBoxStatus.setSizePolicy(sizePolicy)
        self.labelVBoxStatus.setText("")
        self.labelVBoxStatus.setObjectName("labelVBoxStatus")
        self.hboxlayout.addWidget(self.labelVBoxStatus)
        self.verticalLayout_2.addLayout(self.hboxlayout)
        spacerItem = QtGui.QSpacerItem(20, 24, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea = QtGui.QScrollArea(self.tab_4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 327, 366))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setEnabled(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.VBoxNIC = QtGui.QComboBox(self.groupBox)
        self.VBoxNIC.setEnabled(True)
        self.VBoxNIC.setObjectName("VBoxNIC")
        self.VBoxNIC.addItem("")
        self.VBoxNIC.addItem("")
        self.VBoxNIC.addItem("")
        self.VBoxNIC.addItem("")
        self.VBoxNIC.addItem("")
        self.gridLayout.addWidget(self.VBoxNIC, 3, 2, 1, 1)
        self.VBoxNICNb = QtGui.QSpinBox(self.groupBox)
        self.VBoxNICNb.setEnabled(True)
        self.VBoxNICNb.setMinimum(0)
        self.VBoxNICNb.setMaximum(7)
        self.VBoxNICNb.setSingleStep(1)
        self.VBoxNICNb.setProperty("value", 6)
        self.VBoxNICNb.setObjectName("VBoxNICNb")
        self.gridLayout.addWidget(self.VBoxNICNb, 2, 2, 1, 1)
        self.label_37 = QtGui.QLabel(self.groupBox)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 2, 0, 1, 1)
        self.VBoxImage = QtGui.QLineEdit(self.groupBox)
        self.VBoxImage.setObjectName("VBoxImage")
        self.gridLayout.addWidget(self.VBoxImage, 1, 2, 1, 1)
        self.VBoxGuestControl_User = QtGui.QLineEdit(self.groupBox)
        self.VBoxGuestControl_User.setObjectName("VBoxGuestControl_User")
        self.gridLayout.addWidget(self.VBoxGuestControl_User, 5, 2, 1, 1)
        self.VBoxGuestControl_Password = QtGui.QLineEdit(self.groupBox)
        self.VBoxGuestControl_Password.setObjectName("VBoxGuestControl_Password")
        self.gridLayout.addWidget(self.VBoxGuestControl_Password, 6, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.VBoxcheckBoxEnableGuestControl = QtGui.QCheckBox(self.groupBox)
        self.VBoxcheckBoxEnableGuestControl.setObjectName("VBoxcheckBoxEnableGuestControl")
        self.gridLayout.addWidget(self.VBoxcheckBoxEnableGuestControl, 4, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 2, 1, 1)
        self.comboBoxNameVBoxImage = QtGui.QComboBox(self.groupBox)
        self.comboBoxNameVBoxImage.setEditable(True)
        self.comboBoxNameVBoxImage.setObjectName("comboBoxNameVBoxImage")
        self.gridLayout.addWidget(self.comboBoxNameVBoxImage, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SaveVBoxImage = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.SaveVBoxImage.setObjectName("SaveVBoxImage")
        self.horizontalLayout.addWidget(self.SaveVBoxImage)
        self.DeleteVBoxImage = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.DeleteVBoxImage.setObjectName("DeleteVBoxImage")
        self.horizontalLayout.addWidget(self.DeleteVBoxImage)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_20 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)
        self.treeWidgetVBoxImages = QtGui.QTreeWidget(self.scrollAreaWidgetContents)
        self.treeWidgetVBoxImages.setObjectName("treeWidgetVBoxImages")
        self.verticalLayout.addWidget(self.treeWidgetVBoxImages)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_7.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_17.addWidget(self.tabWidget)

        self.retranslateUi(PreferencesVirtualBox)
        self.tabWidget.setCurrentIndex(0)
        self.VBoxNIC.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PreferencesVirtualBox)

    def retranslateUi(self, PreferencesVirtualBox):
        PreferencesVirtualBox.setWindowTitle(QtGui.QApplication.translate("PreferencesVirtualBox", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.P.setTitle(QtGui.QApplication.translate("PreferencesVirtualBox", "VBoxwrapper", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Path to VBoxwrapper:", None, QtGui.QApplication.UnicodeUTF8))
        self.VBoxwrapperPath_browser.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Working directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.VBoxwrapperWorkdir_browser.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "IP/host binding:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Base console port:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxEnableVBoxManager.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Enable VBox Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxVBoxManagerImport.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Use VBox Manager when importing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "External VBoxwrapper:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditHostExternalVBox.setToolTip(QtGui.QApplication.translate("PreferencesVirtualBox", "Add several wrappers, to make your GNS3 distributed across several hosts.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddExternalVBoxwrapper.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDeleteExternalVBoxwrapper.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Registered external VBoxwrappers:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxVBoxWrapperShowAdvancedOptions.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Show VBoxWrapper Advanced Options", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxVBoxShowAdvancedOptions.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Show VirtualBox Advanced Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "VBoxwrapper port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Base UDP port:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonTestVBox.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "&Test", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("PreferencesVirtualBox", "General Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("PreferencesVirtualBox", "VirtualBox Guest Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Identifier name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "VM Name / UUID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "NIC model:", None, QtGui.QApplication.UnicodeUTF8))
        self.VBoxNIC.setItemText(0, QtGui.QApplication.translate("PreferencesVirtualBox", "automatic", None, QtGui.QApplication.UnicodeUTF8))
        self.VBoxNIC.setItemText(1, QtGui.QApplication.translate("PreferencesVirtualBox", "e1000", None, QtGui.QApplication.UnicodeUTF8))
        self.VBoxNIC.setItemText(2, QtGui.QApplication.translate("PreferencesVirtualBox", "pcnet2", None, QtGui.QApplication.UnicodeUTF8))
        self.VBoxNIC.setItemText(3, QtGui.QApplication.translate("PreferencesVirtualBox", "pcnet3", None, QtGui.QApplication.UnicodeUTF8))
        self.VBoxNIC.setItemText(4, QtGui.QApplication.translate("PreferencesVirtualBox", "virtio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Number of NICs:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "GuestControl User", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "GuestControl Password", None, QtGui.QApplication.UnicodeUTF8))
        self.VBoxcheckBoxEnableGuestControl.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "Enable GuestControl", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "(experimental feature)", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveVBoxImage.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.DeleteVBoxImage.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("PreferencesVirtualBox", "VirtualBox Virtual Machines", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetVBoxImages.headerItem().setText(0, QtGui.QApplication.translate("PreferencesVirtualBox", "GNS3 Name", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetVBoxImages.headerItem().setText(1, QtGui.QApplication.translate("PreferencesVirtualBox", "Virtual Machine Name or Unique Identifier", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("PreferencesVirtualBox", "VirtualBox Guest", None, QtGui.QApplication.UnicodeUTF8))

