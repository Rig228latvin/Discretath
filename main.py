import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, \
    QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        menu_widget = QListWidget()
        for i in range(1, 13):
            task = QListWidgetItem(f"задача {i}")
            task.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            menu_widget.addItem(task)

        text_widget = QLabel("")
        button = QPushButton("Дать решение")

        menu_widget.setStyleSheet("""
            QListWidget {
                color: #FFFFFF;
                background-color: #33373B;
                border: none;
                font-size: 16px;
            }

            QListWidget::item {
                height: 50px;
            }

            QListWidget::item:selected {
                background-color: #2ABf9E;
            }
        """)

        text_widget.setStyleSheet("""
            QLabel {
                background-color: #FFFFFF;
                border: 2px solid #33373B;
                border-radius: 5px;
                padding: 10px;
                font-size: 18px;
            }
        """)

        button.setStyleSheet("""
            QPushButton {
                background-color: #2ABf9E;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 18px;
            }

            QPushButton:hover {
                background-color: #238e76;
            }
        """)

        content_layout = QVBoxLayout()
        content_layout.addWidget(text_widget)
        content_layout.addWidget(button)
        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(200, 50, 1500, 1000)

        self.central_widget = Widget()
        self.setCentralWidget(self.central_widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
