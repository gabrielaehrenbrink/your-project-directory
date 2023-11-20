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
        if self.complete == False:
            return self._todo

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass

