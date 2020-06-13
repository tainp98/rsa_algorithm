import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QMessageBox,
                             QInputDialog, QApplication)
import sys
from rsa import RSA

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.label1 = QLabel('threshold',self)
        self.label1.move(20,20)
        self.label1.setFont(QFont('Arial',10))
        self.le1 = QLineEdit(self)
        self.le1.move(130, 22)

        self.labelac = QLabel('error 1/4^',self)
        self.labelac.move(330,20)
        self.labelac.setFont(QFont('Arial',10))
        self.leac = QLineEdit(self)
        self.leac.move(390, 22)

        self.label2 = QLabel('input text',self)
        self.label2.move(20,76)
        self.label2.setFont(QFont('Arial',10))
        self.le2 = QLineEdit(self)
        self.le2.move(130, 72)
        self.le2.resize(900,25)

        self.btn1 = QPushButton('output', self)
        self.btn1.move(20, 120)
        self.btn1.clicked.connect(self.showDialog)

        self.labelp = QLabel('p',self)
        self.labelp.move(130,120)
        self.labelp.setFont(QFont('Arial',10))
        self.lep = QLineEdit(self)
        self.lep.move(140, 122)
        self.lep.resize(60,20)

        self.labelq = QLabel('q',self)
        self.labelq.move(220,120)
        self.labelq.setFont(QFont('Arial',10))
        self.leq = QLineEdit(self)
        self.leq.move(230, 122)
        self.leq.resize(60,20)

        self.labeln = QLabel('n',self)
        self.labeln.move(300,120)
        self.labeln.setFont(QFont('Arial',10))
        self.len = QLineEdit(self)
        self.len.move(310, 122)
        self.len.resize(80,20)

        self.labele = QLabel('e',self)
        self.labele.move(410,120)
        self.labele.setFont(QFont('Arial',10))
        self.lee = QLineEdit(self)
        self.lee.move(420, 122)
        self.lee.resize(60,20)

        self.labeld = QLabel('d',self)
        self.labeld.move(500,120)
        self.labeld.setFont(QFont('Arial',10))
        self.led = QLineEdit(self)
        self.led.move(510, 122)
        self.led.resize(60,20)

        self.label3 = QLabel('plaintext',self)
        self.label3.move(20,176)
        self.label3.setFont(QFont('Arial',10))
        self.le3 = QLineEdit(self)
        self.le3.move(130, 172)
        self.le3.resize(900,25)

        self.label4 = QLabel('ciphertext',self)
        self.label4.move(20,226)
        self.label4.setFont(QFont('Arial',10))
        self.le4 = QLineEdit(self)
        self.le4.move(130, 226)
        self.le4.resize(900,25)

        self.label5 = QLabel('decrypt ciphertext',self)
        self.label5.move(20,276)
        self.label5.setFont(QFont('Arial',10))
        self.le5 = QLineEdit(self)
        self.le5.move(130, 272)
        self.le5.resize(900,25)
        self.setGeometry(50, 50, 1050, 650)
        self.setWindowTitle('RSA_Algorithm')
        

        self.btn2 = QPushButton('clear', self)
        self.btn2.move(20, 320)
        self.btn2.clicked.connect(self.showDialog2)
        self.show()
    def showDialog(self):
        
        self.anchor = int(self.le1.text())
        self.accuracy = int(self.leac.text())
        if(self.anchor < self.accuracy):
            QMessageBox.about(self,"ERROR","need threshold > accuracy")
        else:
            self.text = self.le2.text()
            rsa1 = RSA(self.anchor,self.accuracy,self.text)
            rsa1.create_key()
            self.ciphertext = rsa1.encrypt([rsa1.e,rsa1.n],rsa1.text)
            self.plaintext = rsa1.decrypt([rsa1.d,rsa1.n],self.ciphertext)
            self.ciphertext = [chr(a) for a in self.ciphertext]
            a = ''.join(self.ciphertext)
            self.le3.setText(str(self.text))
            self.le4.setText(str(a))
            self.le5.setText(str(self.plaintext))
            self.lep.setText(str(rsa1.p))
            self.leq.setText(str(rsa1.q))
            self.len.setText(str(rsa1.n))
            self.lee.setText(str(rsa1.e))
            self.led.setText(str(rsa1.d))
    def showDialog2(self):
        self.le3.setText('')
        self.le4.setText('')
        self.le5.setText('')
        self.lep.setText('')
        self.leq.setText('')
        self.len.setText('')
        self.lee.setText('')
        self.led.setText('')

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()