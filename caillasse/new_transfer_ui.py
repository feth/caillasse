# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_transfer.ui'
#
# Created: Sat Sep 10 08:17:04 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_new_transfer(object):
    def setupUi(self, new_transfer):
        new_transfer.setObjectName(_fromUtf8("new_transfer"))
        new_transfer.resize(283, 188)
        self.formLayout = QtGui.QFormLayout(new_transfer)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_giver = QtGui.QLabel(new_transfer)
        self.label_giver.setObjectName(_fromUtf8("label_giver"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_giver)
        self.combo_giver = QtGui.QComboBox(new_transfer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_giver.sizePolicy().hasHeightForWidth())
        self.combo_giver.setSizePolicy(sizePolicy)
        self.combo_giver.setObjectName(_fromUtf8("combo_giver"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.combo_giver)
        self.label_amount = QtGui.QLabel(new_transfer)
        self.label_amount.setObjectName(_fromUtf8("label_amount"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_amount)
        self.spin_amount = QtGui.QDoubleSpinBox(new_transfer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_amount.sizePolicy().hasHeightForWidth())
        self.spin_amount.setSizePolicy(sizePolicy)
        self.spin_amount.setObjectName(_fromUtf8("spin_amount"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.spin_amount)
        self.label_receiver = QtGui.QLabel(new_transfer)
        self.label_receiver.setObjectName(_fromUtf8("label_receiver"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_receiver)
        self.combo_receiver = QtGui.QComboBox(new_transfer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_receiver.sizePolicy().hasHeightForWidth())
        self.combo_receiver.setSizePolicy(sizePolicy)
        self.combo_receiver.setObjectName(_fromUtf8("combo_receiver"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.combo_receiver)
        self.buttonBox = QtGui.QDialogButtonBox(new_transfer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.buttonBox)
        self.text_context = QtGui.QPlainTextEdit(new_transfer)
        self.text_context.setObjectName(_fromUtf8("text_context"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.text_context)
        self.label_context = QtGui.QLabel(new_transfer)
        self.label_context.setObjectName(_fromUtf8("label_context"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_context)

        self.retranslateUi(new_transfer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), new_transfer.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), new_transfer.accept)
        QtCore.QMetaObject.connectSlotsByName(new_transfer)

    def retranslateUi(self, new_transfer):
        new_transfer.setWindowTitle(QtGui.QApplication.translate("new_transfer", "New transfer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_giver.setText(QtGui.QApplication.translate("new_transfer", "Giver", None, QtGui.QApplication.UnicodeUTF8))
        self.label_amount.setText(QtGui.QApplication.translate("new_transfer", "Amount", None, QtGui.QApplication.UnicodeUTF8))
        self.label_receiver.setText(QtGui.QApplication.translate("new_transfer", "Receiver", None, QtGui.QApplication.UnicodeUTF8))
        self.text_context.setToolTip(QtGui.QApplication.translate("new_transfer", "Enter a description of the transfer or reasons for it", None, QtGui.QApplication.UnicodeUTF8))
        self.label_context.setText(QtGui.QApplication.translate("new_transfer", "Context", None, QtGui.QApplication.UnicodeUTF8))

