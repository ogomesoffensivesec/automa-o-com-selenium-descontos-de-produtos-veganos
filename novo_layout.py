from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QComboBox
#import packages.veginextract.extractfunctions as extractfunctions
from packages.veginextract import vegin
from packages.utils import emailsend


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 325)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(228, 253, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 253, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 253, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 253, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 253, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 253, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 253, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 253, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 253, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gotham Book")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #E4FDE1;\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_gerarPlanilha = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gerarPlanilha.setStyleSheet("\n"
                                             "\n"
                                             "\n"
                                             "QPushButton{\n"
                                             "    border: 2px solid #90CF8E;\n"
                                             "    border-radius: 15px;\n"
                                             "    padding: 10px;\n"
                                             "    background-color:#90CF8E;\n"
                                             "    color:white;\n"
                                             "\n"
                                             "    \n"

                                             "margin-bottom: 10px;\n"
                                             "    margin-top: 10px;\n"
                                             "    margin-right: 30px;\n"
                                             "    margin-left:30px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    border: 2px solid #A7DCA5;\n"
                                             "}\n"
                                             "\n"
                                             "")
        self.btn_gerarPlanilha.setObjectName("btn_gerarPlanilha")
        self.verticalLayout.addWidget(self.btn_gerarPlanilha)
        self.input_email = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        self.input_email.setFont(font)
        self.input_email.setStyleSheet("\n"
                                       "\n"
                                       "\n"
                                       "QLineEdit{\n"
                                       "    border: 2px solid #90CF8E;\n"
                                       "    border-radius: 15px;\n"
                                       "    padding: 10px;\n"
                                       "    background-color:#90CF8E;\n"
                                       "    color:white;\n"

                                       "    margin-bottom: 10px;\n"
                                       "    margin-top: 10px;\n"
                                       "    margin-right: 30px;\n"
                                       "    margin-left:30px;\n"
                                       "}QLineEdit:hover{\n"
                                       "    border: 2px solid #A7DCA5;\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:focus{background-color: #C6EDC3;\n"
                                       "    color: #48684f;\n"
                                       "border: 2px solid #A7DCA5;}\n"
                                       "\n"
                                       "")
        self.input_email.setText("")
        self.input_email.setObjectName("input_email")
        self.verticalLayout.addWidget(self.input_email)
        self.btn_sendEmail = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sendEmail.setStyleSheet("\n"
                                         "\n"
                                         "\n"
                                         "QPushButton{\n"
                                         "    border: 2px solid #90CF8E;\n"
                                         "    border-radius: 15px;\n"
                                         "    padding: 10px;\n"
                                         "    background-color:#90CF8E;\n"
                                         "    color:white;\n"
                                         "\n"
                                         "    \n"

                                         "margin-bottom: 10px;\n"
                                         "    margin-top: 10px;\n"
                                         "    margin-right: 30px;\n"
                                         "    margin-left:30px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border: 2px solid #A7DCA5;\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.btn_sendEmail.setObjectName("btn_sendEmail")
        self.verticalLayout.addWidget(self.btn_sendEmail)
        self.btn_sair = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sair.setStyleSheet("\n"
                                    "\n"
                                    "\n"
                                    "QPushButton{\n"
                                    "    border: 2px solid #90CF8E;\n"
                                    "    border-radius: 15px;\n"
                                    "    padding: 10px;\n"
                                    "    background-color:#90CF8E;\n"
                                    "    color:white;\n"
                                    "\n"
                                    "    \n"

                                    "margin-bottom: 1px;\n"
                                    "    margin-top: 10px;\n"
                                    "    margin-right: 30px;\n"
                                    "    margin-left:30px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "    border: 2px solid #A7DCA5;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.btn_sair.setObjectName("btn_sair")
        self.verticalLayout.addWidget(self.btn_sair)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_sair.clicked.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_sair.clicked.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_gerarPlanilha.clicked.connect(self.extract)
        # self.btn_viewMelhoresOfertas.clicked.connect(self.view)
        self.btn_sendEmail.clicked.connect(self.sendEmail)

    def extract(self):
        vegin.saveInfosinExcelFile()
        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle('Sucesso')
        msg.setText('Arquivo gerado com sucesso!')
        msg.exec()

    def sendEmail(self):
        emailclient = str(self.input_email.text())
        emailsend.sendEmail(emailclient)
        emailclient.clear()
        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle('Sucesso')
        msg.setText('Email enviado com sucesso!')
        msg.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Descontos Veganos"))
        self.btn_gerarPlanilha.setText(
            _translate("MainWindow", "Gerar planilha"))
        self.input_email.setPlaceholderText(_translate("MainWindow", "E-mail"))
        self.btn_sendEmail.setText(_translate("MainWindow", "Enviar planilha"))
        self.btn_sair.setText(_translate("MainWindow", "Fechar"))


[]
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
