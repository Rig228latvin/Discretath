from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from src.models.task import tasks
from src.styles.textWidget import textWidgetStyles, menuWidgetStyles, buttonStyles


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        menu_widget = QListWidget()

        for t in tasks:
            task = QListWidgetItem(t.name)
            task.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            menu_widget.addItem(task)

        text_widget = QLabel("Кал залупа пизда")
        button = QPushButton("Дать решение")

        menu_widget.setStyleSheet(menuWidgetStyles)
        text_widget.setStyleSheet(textWidgetStyles)
        button.setStyleSheet(buttonStyles)

        content_layout = QVBoxLayout()
        content_layout.addWidget(text_widget)
        content_layout.addWidget(button)

        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)
