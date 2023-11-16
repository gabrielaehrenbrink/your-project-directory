class TodoList():
    def __init__(self, todo_item):
        self._todo = [todo_item]

    def entry_todo(self, todo):
        self._todo.append(todo)