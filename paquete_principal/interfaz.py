import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class Windowlibreria(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("gui/MainWindowlibreria.ui", self)


        a = uic.loadUi("gui/win_registrar.ui", self)
        b = uic.loadUi("gui/win_iniciar_sesion.ui", self)
        c = uic.loadUi("gui/win_buscar_libro.ui", self)
        d = uic.loadUi("gui/win_seleccionar_libro.ui", self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    winpp = Windowlibreria()
    winpp.show()
    sys.exit(app.exec_())








