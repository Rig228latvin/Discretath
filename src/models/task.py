from typing import List


class Task:
    def __init__(self, name: str, code: str, parameters: list[int]):
        self.code = code
        self.name = name
        self.parameters = parameters

    def execute(self):
        exec(self.code)


tasks: List[Task] = [
    Task("Title 1", "#include <gayporn>", []),
    Task("Title 2", "#include <gayporn>", [])
]
