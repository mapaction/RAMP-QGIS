# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mapactiontools.ui'
#
# Created: Fri Oct 12 11:55:56 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MapActionTools(object):
    def setupUi(self, MapActionTools):
        MapActionTools.setObjectName(_fromUtf8("MapActionTools"))
        MapActionTools.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(MapActionTools)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.pushButton = QtGui.QPushButton(MapActionTools)
        self.pushButton.setGeometry(QtCore.QRect(180, 100, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(MapActionTools)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MapActionTools.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MapActionTools.reject)
        QtCore.QMetaObject.connectSlotsByName(MapActionTools)

    def retranslateUi(self, MapActionTools):
        MapActionTools.setWindowTitle(QtGui.QApplication.translate("MapActionTools", "MapActionTools", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MapActionTools", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

