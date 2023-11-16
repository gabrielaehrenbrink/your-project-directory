class TodoList:
    def __init__(self):
        self._todo = []


    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self._todo.append(todo)
        
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_todos = [todo for todo in self._todo if not todo.complete]
        return incomplete_todos

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_todos = []
        for todo in self._todo:
            if todo.complete:
                complete_todos.append(todo)

        return complete_todos

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self._todo:
            todo.complete = True   

