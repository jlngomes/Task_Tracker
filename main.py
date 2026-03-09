from data import json_handler
from source import task_handler

if __name__ == '__main__':
    obj = task_handler.TaskHandler()

    print(obj.add_task("teste_2"))
    print(obj.add_task("teste_1"))
