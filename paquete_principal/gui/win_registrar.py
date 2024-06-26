# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paquete_principal/gui/win_registrar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_win_registrar(object):
    def setupUi(self, win_registrar):
        win_registrar.setObjectName("win_registrar")
        win_registrar.setEnabled(True)
        win_registrar.resize(468, 443)
        win_registrar.setMouseTracking(True)
        win_registrar.setTabletTracking(True)
        win_registrar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_registrar = QtWidgets.QPushButton(win_registrar)
        self.btn_registrar.setGeometry(QtCore.QRect(310, 380, 101, 31))
        self.btn_registrar.setStyleSheet("background-color:rgb(190, 249, 255)\n"
"")
        self.btn_registrar.setObjectName("btn_registrar")
        self.text_registrar_usuario = QtWidgets.QTextBrowser(win_registrar)
        self.text_registrar_usuario.setGeometry(QtCore.QRect(60, 30, 351, 59))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.text_registrar_usuario.setFont(font)
        self.text_registrar_usuario.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_registrar_usuario.setStyleSheet("background-color:rgb(190, 249, 255)\n"
"")
        self.text_registrar_usuario.setObjectName("text_registrar_usuario")
        self.txt_nombre_usuario = QtWidgets.QTextEdit(win_registrar)
        self.txt_nombre_usuario.setGeometry(QtCore.QRect(50, 150, 381, 31))
        self.txt_nombre_usuario.setStyleSheet("background-color:rgb(190, 249, 255)\n"
"")
        self.txt_nombre_usuario.setObjectName("txt_nombre_usuario")
        self.txt_correo = QtWidgets.QTextEdit(win_registrar)
        self.txt_correo.setGeometry(QtCore.QRect(50, 240, 381, 31))
        self.txt_correo.setStyleSheet("background-color:rgb(190, 249, 255)\n"
"")
        self.txt_correo.setObjectName("txt_correo")
        self.txt_clave = QtWidgets.QTextEdit(win_registrar)
        self.txt_clave.setGeometry(QtCore.QRect(50, 310, 381, 31))
        self.txt_clave.setStyleSheet("background-color:rgb(190, 249, 255)\n"
"")
        self.txt_clave.setObjectName("txt_clave")
        self.lb_clave = QtWidgets.QLabel(win_registrar)
        self.lb_clave.setGeometry(QtCore.QRect(50, 290, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_clave.setFont(font)
        self.lb_clave.setObjectName("lb_clave")
        self.lb_correo = QtWidgets.QLabel(win_registrar)
        self.lb_correo.setGeometry(QtCore.QRect(50, 210, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_correo.setFont(font)
        self.lb_correo.setObjectName("lb_correo")
        self.lb_nom_usuario = QtWidgets.QLabel(win_registrar)
        self.lb_nom_usuario.setGeometry(QtCore.QRect(50, 120, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_nom_usuario.setFont(font)
        self.lb_nom_usuario.setObjectName("lb_nom_usuario")

        self.retranslateUi(win_registrar)
        QtCore.QMetaObject.connectSlotsByName(win_registrar)

    def retranslateUi(self, win_registrar):
        _translate = QtCore.QCoreApplication.translate
        win_registrar.setWindowTitle(_translate("win_registrar", "win_registrar"))
        self.btn_registrar.setText(_translate("win_registrar", "REGISTRAR"))
        self.text_registrar_usuario.setHtml(_translate("win_registrar", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#000000;\">REGISTRAR USUARIO</span></p></body></html>"))
        self.txt_nombre_usuario.setHtml(_translate("win_registrar", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.txt_correo.setHtml(_translate("win_registrar", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.txt_clave.setHtml(_translate("win_registrar", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lb_clave.setText(_translate("win_registrar", "CLAVE:"))
        self.lb_correo.setText(_translate("win_registrar", "CORREO ELECTRONICO:"))
        self.lb_nom_usuario.setText(_translate("win_registrar", "NOMBRE DE USUARIO:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win_registrar = QtWidgets.QWidget()
    ui_registrar = Ui_win_registrar()
    ui_registrar.setupUi(win_registrar)
    win_registrar.show()
    sys.exit(app.exec_())
