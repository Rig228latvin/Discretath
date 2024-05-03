from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, \
    QLineEdit
from src.models.task import tasks
from src.styles.textWidget import textWidgetStyles, menuWidgetStyles, buttonStyles


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.variable_inputs = {}
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

        self.solved_tasks_widget = QListWidget()

        menu_widget.setStyleSheet(menuWidgetStyles)
        self.text_widget.setStyleSheet(textWidgetStyles)
        self.button.setStyleSheet(buttonStyles)

        main_layout = QHBoxLayout()

        menu_layout = QVBoxLayout()
        menu_layout.addWidget(menu_widget)
        main_layout.addLayout(menu_layout)

        content_layout = QVBoxLayout()
        content_layout.addWidget(self.text_widget)

        for task in tasks:
            variable_label = QLabel(f"Переменные для {task.name}:")
            variable_input = QLineEdit()
            self.variable_inputs[task] = variable_input
            content_layout.addWidget(variable_label)
            content_layout.addWidget(variable_input)

        content_layout.addWidget(self.button)
        content_layout.addWidget(self.solved_tasks_widget)

        main_widget = QWidget()
        main_widget.setLayout(content_layout)
        main_layout.addWidget(main_widget)

        self.setLayout(main_layout)

    def on_task_selected(self, item):
        task_name = item.text()
        for t in tasks:
            if t.name == task_name:
                self.current_task = t
                self.text_widget.setText(t.condition)
                break

    def execute_task(self):
        if self.current_task:
            parameters = [input_widget.text() for input_widget in self.variable_inputs.values()]
            result = self.current_task.execute_with_parameters(parameters)
            self.solved_tasks_widget.addItem(result)


