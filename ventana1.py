import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton


class Ventana1(QMainWindow):

    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        self.setWindowTitle("Formulario de registro")
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
        self.imagenFondo = QPixmap('imagenes/kiti.jpg')

        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)

        self.horizontal = QVBoxLayout()

        self.horizontal.setContentsMargins(30, 30, 30, 30)

        self.ladoIzquierdo = QFormLayout()
        self.letrero1 = QLabel()

        self.letrero1.setText("Informacion del cliente")
        self.letrero1.setFont(QFont('Century', 20))
        self.letrero1.setStyleSheet("color: #000080;")

        self.ladoIzquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()
        self.letrero2.setFixedWidth(340)

        self.letrero2.setText("""
        Por favor ingrese la informacion del cliente
        en el formulario de abajo. Los campos marcados
        con asterisco son obligatorios""")
        self.letrero2.setFont(QFont('Century', 10))
        self.letrero2.setStyleSheet("color: #0E6655; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #0E6655;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")
        self.ladoIzquierdo.addRow(self.letrero2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Nombre Completo*",self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)
        self.ladoIzquierdo.addRow("Contrasena*", self.password)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Cedula de ciudadania*", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Correo electronico*", self.correo)

        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(90)
        self.botonRegistrar.setStyleSheet("""background-color: #CCCCFF;
                                            color: black;
                                            padding: 10px;
                                            margin-top: 40px;""")
        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)
        self.botonLimpiar.setStyleSheet("""background-color: #CCCCFF;
                                                    color: black;
                                                    padding: 10px;
                                                    margin-top: 40px;""")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        self.horizontal.addLayout(self.ladoIzquierdo)
        self.fondo.setLayout(self.horizontal)

    def accion_botonRegistrar(self):
        pass

    def accion_botonLimpiar(self):
        pass

if __name__ == '__main__':
    app = QApplication([])
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec_())