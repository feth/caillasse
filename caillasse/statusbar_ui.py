# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statusbar.ui'
#
# Created: Sat Sep 10 17:21:42 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_statusbar(object):
    def setupUi(self, statusbar):
        statusbar.setObjectName(_fromUtf8("statusbar"))
        statusbar.resize(408, 51)
        self.horizontalLayout = QtGui.QHBoxLayout(statusbar)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.info = QtGui.QLabel(statusbar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy)
        self.info.setObjectName(_fromUtf8("info"))
        self.horizontalLayout.addWidget(self.info)
        self.icon = QtGui.QLabel(statusbar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setObjectName(_fromUtf8("icon"))
        self.horizontalLayout.addWidget(self.icon)

        self.retranslateUi(statusbar)
        QtCore.QMetaObject.connectSlotsByName(statusbar)

    def retranslateUi(self, statusbar):
        statusbar.setWindowTitle(QtGui.QApplication.translate("statusbar", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.info.setText(QtGui.QApplication.translate("statusbar", "info", None, QtGui.QApplication.UnicodeUTF8))
        self.icon.setText(QtGui.QApplication.translate("statusbar", "icon", None, QtGui.QApplication.UnicodeUTF8))

