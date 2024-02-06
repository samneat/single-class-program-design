class TaskManager:
    def __init__(self):
        self._todo_list = []

    def add(self, task):
        self._todo_list.append(task)

    def list_incomplete(self):
        return self._todo_list

    def mark_complete(self, index):
        if index < 0 or index >= len(self._todo_list):
            raise Exception("No such task to complete")
        del self._todo_list[index]