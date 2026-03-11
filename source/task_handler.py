from data import json_handler

dict_storage = {}

class TaskHandler:
    def __init__(self):
        self.task = None
        self.id_task = 0

    def add_task(self, task):
        self.task = task

        if not self.task:
            raise Exception('Task não pode ser vazia')

        self.id_task += 1

        if not self.task in dict_storage:
            dict_storage[self.id_task] = {}

        dict_storage[self.id_task]["Task_name"] = self.task
        dict_storage[self.id_task]["Status"] = None

        return f"Task added successfully (ID: {self.id_task})"

    def delete_task(self, code):
        pass

    def update_task(self, task):
        pass

    def list_tasks(self, filtro: str=None):
        if dict_storage:
            ...

        for task in dict_storage.keys():
            print(f"\n{dict_storage[task]}")




