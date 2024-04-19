from typing import List


class Task:
    def __init__(self, name: str, code: str, parameters: list[int]):
        self.code = code
        self.name = name

    def execute_with_parameters(self, parameters: List[int]) -> str:
        result = "Результат выполнения задачи"
        return result


tasks: List[Task] = [
    Task("Задача 1", "#include <iostream>", []),
    Task("Задача 2", "#include <123>", []),
    Task("Задача 3", "#include <324>", []),
    Task("Задача 4", "#include <532>", []),
    Task("Задача 5", "#include <iream>", []),
    Task("Задача 6", "#include <754>", []),
    Task("Задача 7", "#include <6546>", []),
    Task("Задача 8", "#include <65г2>", []),
    Task("Задача 9", "#include <iream>", []),
    Task("Задача 10", "#include <754>", []),
    Task("Задача 11", "#include <6546>", []),
    Task("Задача 12", "#include <65г2>", [])
]
