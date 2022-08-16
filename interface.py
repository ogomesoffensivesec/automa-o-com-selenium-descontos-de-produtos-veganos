from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QComboBox
#import packages.veginextract.extractfunctions as extractfunctions
from packages.veginextract import vegin
from packages.utils import emailsend


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        MainWindow.setStyleSheet("background-color: #001d3d ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_gerarPlanilha = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gerarPlanilha.setGeometry(QtCore.QRect(45, 30, 221, 41))
        self.btn_gerarPlanilha.setStyleSheet(
            "font: 81 8pt \"Lato Heavy\";\n"  "color: rgb(255, 255, 255);\n"  "alternate-background-color: rgb(0, 86, 161);\n""background-color: #003566;\n""\n")
        self.btn_gerarPlanilha.setObjectName("btn_gerarPlanilha")
        self.btn_sendEmail = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sendEmail.setEnabled(True)
        self.btn_sendEmail.setGeometry(QtCore.QRect(90, 140, 121, 31))
        self.btn_sendEmail.setStyleSheet(
            "font: 81 8pt \"Lato Heavy\";\n""color: rgb(255, 255, 255);\n""alternate-background-color: rgb(0, 86, 161);\n""background-color: #003566;\n""\n""")
        self.btn_sendEmail.setObjectName("btn_sendEmail")
        ''' self.btn_viewMelhoresOfertas = QtWidgets.QPushButton(
            self.centralwidget)
        self.btn_viewMelhoresOfertas.setGeometry(
            QtCore.QRect(45, 320, 221, 41))
        self.btn_viewMelhoresOfertas.setObjectName("btn_viewMelhoresOfertas")'''
        self.btn_sair = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sair.setGeometry(QtCore.QRect(90, 230, 121, 31))
        self.btn_sair.setStyleSheet("font: 81 8pt \"Lato Heavy\";\n"
                                    "alternate-background-color: rgb(0, 86, 161);\n"
                                    "background-color: #003566;\n "
                                    "color : white"
                                    "\n"
                                    "")
        self.btn_sair.setObjectName("btn_sair")
        '''self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(8, 160, 81, 31))
        self.label.setStyleSheet("font: 81 8pt \"Lato Heavy\";\n" "color: rgb(255, 255, 255);\n""\n""\n""")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")'''
        self.input_email = QtWidgets.QLineEdit(self.centralwidget)
        self.input_email.setGeometry(QtCore.QRect(45, 110, 221, 21))
        self.input_email.setStyleSheet(
            "color: black;\n"  "background-color: white;""\n""border: 2px solid white""\n")
        self.input_email.setObjectName("input_email")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
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
        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle('Sucesso')
        msg.setText('Email enviado com sucesso!')
        msg.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "Melhores Descontos", "Melhores Descontos"))
        self.btn_gerarPlanilha.setText(_translate(
            "MainWindow", "Gerar Planilha de Produtos com Desconto"))
        self.btn_sendEmail.setText(_translate(
            "MainWindow", "Enviar por e-mail"))
        '''self.btn_viewMelhoresOfertas.setText( _translate("MainWindow", "Exibir melhores ofertas"))'''
        self.btn_sair.setText(_translate("MainWindow", "Sair"))
        #self.label.setText(_translate("MainWindow", "Insira o e-mail:"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
