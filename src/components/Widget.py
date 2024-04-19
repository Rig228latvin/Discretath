from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from src.models.task import tasks
from src.styles.textWidget import textWidgetStyles, menuWidgetStyles, buttonStyles


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.current_task = None

        menu_widget = QListWidget()
        menu_widget.itemClicked.connect(self.on_task_selected)

        for t in tasks:
            task = QListWidgetItem(t.name)
            task.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            menu_widget.addItem(task)

        self.text_widget = QLabel("Выберите задачу")
        self.button = QPushButton("Дать решение")
        self.button.clicked.connect(self.execute_task)

        menu_widget.setStyleSheet(menuWidgetStyles)
        self.text_widget.setStyleSheet(textWidgetStyles)
        self.button.setStyleSheet(buttonStyles)

        content_layout = QVBoxLayout()
        content_layout.addWidget(self.text_widget)
        content_layout.addWidget(self.button)

        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)

    def on_task_selected(self, item):
        task_name = item.text()
        for t in tasks:
            if t.name == task_name:
                self.current_task = t
                self.text_widget.setText(t.code)
                break

    def execute_task(self):
        if self.current_task:
            parameters = [1, 2, 3]
            result = self.current_task.execute_with_parameters(parameters)
            print(result)
