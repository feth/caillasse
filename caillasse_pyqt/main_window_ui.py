# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Wed Sep  7 14:51:41 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_caillasse(object):
    def setupUi(self, caillasse):
        caillasse.setObjectName(_fromUtf8("caillasse"))
        caillasse.resize(800, 600)
        self.centralwidget = QtGui.QWidget(caillasse)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setAccessibleName(_fromUtf8(""))
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.Persons = QtGui.QWidget()
        self.Persons.setObjectName(_fromUtf8("Persons"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.Persons)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter_2 = QtGui.QSplitter(self.Persons)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.all_persons = QtGui.QTableView(self.splitter_2)
        self.all_persons.setAccessibleName(_fromUtf8(""))
        self.all_persons.setObjectName(_fromUtf8("all_persons"))
        self.one_person = QtGui.QTableView(self.splitter_2)
        self.one_person.setObjectName(_fromUtf8("one_person"))
        self.verticalLayout_3.addWidget(self.splitter_2)
        self.tabs.addTab(self.Persons, _fromUtf8(""))
        self.Activities = QtGui.QWidget()
        self.Activities.setObjectName(_fromUtf8("Activities"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.Activities)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(self.Activities)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.all_activities = QtGui.QTableView(self.splitter)
        self.all_activities.setObjectName(_fromUtf8("all_activities"))
        self.one_activity = QtGui.QTableView(self.splitter)
        self.one_activity.setObjectName(_fromUtf8("one_activity"))
        self.verticalLayout_2.addWidget(self.splitter)
        self.tabs.addTab(self.Activities, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabs)
        caillasse.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(caillasse)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuLoad = QtGui.QMenu(self.menubar)
        self.menuLoad.setObjectName(_fromUtf8("menuLoad"))
        caillasse.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(caillasse)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        caillasse.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(caillasse)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionLoad = QtGui.QAction(caillasse)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionRecent = QtGui.QAction(caillasse)
        self.actionRecent.setObjectName(_fromUtf8("actionRecent"))
        self.actionSave_as = QtGui.QAction(caillasse)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.menuLoad.addAction(self.actionSave)
        self.menuLoad.addAction(self.actionSave_as)
        self.menuLoad.addAction(self.actionLoad)
        self.menuLoad.addAction(self.actionRecent)
        self.menubar.addAction(self.menuLoad.menuAction())

        self.retranslateUi(caillasse)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(caillasse)

    def retranslateUi(self, caillasse):
        caillasse.setWindowTitle(QtGui.QApplication.translate("caillasse", "Caillasse", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.Persons), QtGui.QApplication.translate("caillasse", "Persons", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.Activities), QtGui.QApplication.translate("caillasse", "Activities", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLoad.setTitle(QtGui.QApplication.translate("caillasse", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("caillasse", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("caillasse", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent.setText(QtGui.QApplication.translate("caillasse", "Recent", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("caillasse", "Save a copy", None, QtGui.QApplication.UnicodeUTF8))

