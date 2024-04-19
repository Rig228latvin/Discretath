from PyQt6.QtWidgets import QMainWindow

from src.components.Widget import Widget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Дискретная математика")
        self.setGeometry(200, 50, 1500, 1000)

        self.central_widget = Widget()
        self.setCentralWidget(self.central_widget)