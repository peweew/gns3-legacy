# -*- coding: utf-8 -*-
# vim: expandtab ts=4 sw=4 sts=4:
#
# Copyright (C) 2007 GNS-3 Dev Team
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation;
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
# Contact: contact@gns3.net
#

import sys, platform
import GNS3.Globals as globals
from PyQt4 import QtGui, QtCore
from GNS3.Config.Objects import systemGeneralConf
from GNS3.Ui.ConfigurationPages.Form_PreferencesGeneral import Ui_PreferencesGeneral
from GNS3.Utils import translate, fileBrowser
from GNS3.Config.Config import ConfDB

class UiConfig_PreferencesGeneral(QtGui.QWidget, Ui_PreferencesGeneral):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        Ui_PreferencesGeneral.setupUi(self, self)

        self.langs = globals.GApp.translator.getAvailables()
        for lang in self.langs:
            lang_code = lang[0]
            lang_name = lang[1]
            lang_displayText = u"%s (%s)" % (lang_name, lang_code)
            self.langsBox.addItem(lang_displayText)
        
        self.connect(self.ProjectPath_browser, QtCore.SIGNAL('clicked()'), self.__setProjectPath)
        self.connect(self.IOSPath_browser, QtCore.SIGNAL('clicked()'), self.__setIOSPath)
        self.loadConf()

    def loadConf(self):

        if globals.GApp.systconf.has_key('general'):
            self.conf = globals.GApp.systconf['general']
        else:
            self.conf = systemGeneralConf()
    
        curr_lang_code = self.conf.lang

        # Set the languages comboBox the the right value.
        idx = 0
        for i in self.langs:
            if i[0] == curr_lang_code:
                self.langsBox.setCurrentIndex(idx)
            idx += 1
                
        # Defaults terminal command
        if self.conf.term_cmd == '':
            if sys.platform.startswith('darwin'):
                self.conf.term_cmd = unicode("/usr/bin/osascript -e 'tell application \"terminal\" to do script with command \"telnet %h %p ; exit\"'",  'utf-8')
            elif sys.platform.startswith('win'):
                # ugly method to detect Vista (Vista doesn't have telnet)
                if platform.uname()[3][0] == '6':
                    self.conf.term_cmd = unicode("putty.exe -telnet %h %p",  'utf-8')
                else:
                    self.conf.term_cmd = unicode("start telnet %h %p",  'utf-8')
            else:
                self.conf.term_cmd = unicode("xterm -T %d -e 'telnet %h %p' >/dev/null 2>&1 &",  'utf-8')

        self.lineEditTermCommand.setText(self.conf.term_cmd)
        self.ProjectPath.setText(self.conf.project_path)
        self.IOSPath.setText(self.conf.ios_path)
            
        # GUI settings
        if self.conf.status_points == True:
            self.checkBoxShowStatusPoints.setCheckState(QtCore.Qt.Checked)
        else:
            self.checkBoxShowStatusPoints.setCheckState(QtCore.Qt.Unchecked)
        if self.conf.manual_connection == True:
            self.checkBoxManualConnections.setCheckState(QtCore.Qt.Checked)
        else:
            self.checkBoxManualConnections.setCheckState(QtCore.Qt.Unchecked)

    def saveConf(self):

        new_idx = self.langsBox.currentIndex()
        if new_idx != -1:
            new_lang_code = self.langs[new_idx][0]
            self.conf.lang = unicode(new_lang_code, 'utf-8')
            globals.GApp.translator.switchLangTo(new_lang_code)
        
        # GUI settings
        if self.checkBoxShowStatusPoints.checkState() == QtCore.Qt.Checked:
            self.confstatus_points = True
        else:
            self.conf.status_points = False
        if self.checkBoxManualConnections.checkState() == QtCore.Qt.Checked:
            self.conf.manual_connection = True
        else:
            self.conf.manual_connection = False
    
        self.conf.project_path = unicode(self.ProjectPath.text(),  'utf-8')
        self.conf.ios_path = unicode(self.IOSPath.text(),  'utf-8')
        self.conf.term_cmd = unicode(self.lineEditTermCommand.text(),  'utf-8')
        
        globals.GApp.systconf['general'] = self.conf
        ConfDB().sync()

    def __setProjectPath(self):
    
        fb = fileBrowser(translate('UiConfig_PreferencesGeneral', 'Project Directory'))
        path = fb.getDir()

        if path is not None:
            self.ProjectPath.setText(path)
        
    def __setIOSPath(self):
    
        fb = fileBrowser(translate('UiConfig_PreferencesGeneral', 'IOS Directory'))
        path = fb.getDir()

        if path is not None:
            self.IOSPath.setText(path)

