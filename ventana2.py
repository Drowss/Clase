import math
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QWidget, QButtonGroup, QGridLayout, QScrollArea

class Ventana2(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.Anterior = anterior
        # creacion de la ventana
        self.setWindowTitle("Usuarios Registrados")
        self.setWindowIcon(QtGui.QIcon('imagenes/kiticono.jpg'))
        self.ancho = 900
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap('imagenes/stui.jpg')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        # creacion de layout horizontal para la distribucion
        self.vertical = QVBoxLayout()

        # hacemos los labels informativos
        self.letrero1 = QLabel()
        self.letrero1.setText("Usuario registrado")
        self.letrero1.setFont(QFont("Arial", 20))
        self.letrero1.setStyleSheet('color: black;')

        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet('background-color:transparent;')
        self.scrollArea.setWidgetResizable(True)

        self.fondo.setLayout(self.vertical)



if __name__ == '__main__':
    app = QApplication([])
    ventana2 = Ventana2()
    ventana2.show()
    sys.exit(app.exec_())