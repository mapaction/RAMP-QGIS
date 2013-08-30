# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_toolbarconfigtool.ui'
#
# Created: Tue Oct 16 20:09:00 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ToolbarConfigTool(object):
    def setupUi(self, ToolbarConfigTool):
        ToolbarConfigTool.setObjectName(_fromUtf8("ToolbarConfigTool"))
        ToolbarConfigTool.resize(425, 327)
        self.groupBox = QtGui.QGroupBox(ToolbarConfigTool)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 401, 241))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_20 = QtGui.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(20, 205, 121, 16))
        self.label_20.setBaseSize(QtCore.QSize(0, 0))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_19 = QtGui.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(20, 145, 101, 16))
        self.label_19.setBaseSize(QtCore.QSize(0, 0))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.txtWWW = QtGui.QLineEdit(self.groupBox)
        self.txtWWW.setGeometry(QtCore.QRect(150, 145, 201, 20))
        self.txtWWW.setObjectName(_fromUtf8("txtWWW"))
        self.txtFirstName = QtGui.QLineEdit(self.groupBox)
        self.txtFirstName.setGeometry(QtCore.QRect(150, 25, 201, 20))
        self.txtFirstName.setObjectName(_fromUtf8("txtFirstName"))
        self.btnDeployConfigPath = QtGui.QToolButton(self.groupBox)
        self.btnDeployConfigPath.setGeometry(QtCore.QRect(360, 205, 25, 19))
        self.btnDeployConfigPath.setObjectName(_fromUtf8("btnDeployConfigPath"))
        self.lblOperationName_2 = QtGui.QLabel(self.groupBox)
        self.lblOperationName_2.setGeometry(QtCore.QRect(20, 115, 101, 16))
        self.lblOperationName_2.setBaseSize(QtCore.QSize(0, 0))
        self.lblOperationName_2.setObjectName(_fromUtf8("lblOperationName_2"))
        self.txtEmail = QtGui.QLineEdit(self.groupBox)
        self.txtEmail.setGeometry(QtCore.QRect(150, 115, 201, 20))
        self.txtEmail.setObjectName(_fromUtf8("txtEmail"))
        self.btnDefaultPath = QtGui.QToolButton(self.groupBox)
        self.btnDefaultPath.setGeometry(QtCore.QRect(360, 175, 25, 19))
        self.btnDefaultPath.setObjectName(_fromUtf8("btnDefaultPath"))
        self.txtDeployConfigPath = QtGui.QLineEdit(self.groupBox)
        self.txtDeployConfigPath.setGeometry(QtCore.QRect(150, 205, 201, 20))
        self.txtDeployConfigPath.setObjectName(_fromUtf8("txtDeployConfigPath"))
        self.txtDefaultPath = QtGui.QLineEdit(self.groupBox)
        self.txtDefaultPath.setGeometry(QtCore.QRect(150, 175, 201, 20))
        self.txtDefaultPath.setObjectName(_fromUtf8("txtDefaultPath"))
        self.label_17 = QtGui.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(20, 55, 101, 16))
        self.label_17.setBaseSize(QtCore.QSize(0, 0))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(20, 85, 101, 16))
        self.label_16.setBaseSize(QtCore.QSize(0, 0))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_18 = QtGui.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(20, 175, 101, 16))
        self.label_18.setBaseSize(QtCore.QSize(0, 0))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.lblOperationName = QtGui.QLabel(self.groupBox)
        self.lblOperationName.setGeometry(QtCore.QRect(20, 25, 101, 16))
        self.lblOperationName.setBaseSize(QtCore.QSize(0, 0))
        self.lblOperationName.setObjectName(_fromUtf8("lblOperationName"))
        self.txtSurname = QtGui.QLineEdit(self.groupBox)
        self.txtSurname.setGeometry(QtCore.QRect(150, 55, 201, 20))
        self.txtSurname.setObjectName(_fromUtf8("txtSurname"))
        self.txtOrganisation = QtGui.QLineEdit(self.groupBox)
        self.txtOrganisation.setGeometry(QtCore.QRect(150, 85, 201, 20))
        self.txtOrganisation.setObjectName(_fromUtf8("txtOrganisation"))
        self.btnCancel = QtGui.QPushButton(ToolbarConfigTool)
        self.btnCancel.setGeometry(QtCore.QRect(250, 290, 75, 23))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.btnCreateSave = QtGui.QPushButton(ToolbarConfigTool)
        self.btnCreateSave.setGeometry(QtCore.QRect(330, 290, 75, 23))
        self.btnCreateSave.setObjectName(_fromUtf8("btnCreateSave"))
        self.label = QtGui.QLabel(ToolbarConfigTool)
        self.label.setGeometry(QtCore.QRect(135, 10, 166, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(ToolbarConfigTool)
        QtCore.QMetaObject.connectSlotsByName(ToolbarConfigTool)
        ToolbarConfigTool.setTabOrder(self.txtFirstName, self.txtSurname)
        ToolbarConfigTool.setTabOrder(self.txtSurname, self.txtOrganisation)
        ToolbarConfigTool.setTabOrder(self.txtOrganisation, self.txtEmail)
        ToolbarConfigTool.setTabOrder(self.txtEmail, self.txtWWW)
        ToolbarConfigTool.setTabOrder(self.txtWWW, self.txtDefaultPath)
        ToolbarConfigTool.setTabOrder(self.txtDefaultPath, self.txtDeployConfigPath)
        ToolbarConfigTool.setTabOrder(self.txtDeployConfigPath, self.btnCreateSave)
        ToolbarConfigTool.setTabOrder(self.btnCreateSave, self.btnCancel)
        ToolbarConfigTool.setTabOrder(self.btnCancel, self.btnDefaultPath)
        ToolbarConfigTool.setTabOrder(self.btnDefaultPath, self.btnDeployConfigPath)

    def retranslateUi(self, ToolbarConfigTool):
        ToolbarConfigTool.setWindowTitle(QtGui.QApplication.translate("ToolbarConfigTool", "MapAction Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ToolbarConfigTool", "Configuration parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("ToolbarConfigTool", "Deployment config path", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("ToolbarConfigTool", "www", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDeployConfigPath.setText(QtGui.QApplication.translate("ToolbarConfigTool", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.lblOperationName_2.setText(QtGui.QApplication.translate("ToolbarConfigTool", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDefaultPath.setText(QtGui.QApplication.translate("ToolbarConfigTool", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("ToolbarConfigTool", "Surname", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("ToolbarConfigTool", "Organisation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("ToolbarConfigTool", "Default path", None, QtGui.QApplication.UnicodeUTF8))
        self.lblOperationName.setText(QtGui.QApplication.translate("ToolbarConfigTool", "First name", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("ToolbarConfigTool", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCreateSave.setText(QtGui.QApplication.translate("ToolbarConfigTool", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ToolbarConfigTool", "Toolbar Configuration", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ToolbarConfigTool = QtGui.QDialog()
    ui = Ui_ToolbarConfigTool()
    ui.setupUi(ToolbarConfigTool)
    ToolbarConfigTool.show()
    sys.exit(app.exec_())

