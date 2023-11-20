from lib.todo_list import TodoList
from lib.todo import Todo

# test 1 empty todo list


#  add two todos to todo list

def test_adds_multiple_incomplete_todo():
    todo_list = TodoList
    todo_1 = Todo('walk the dog')
    todo_2 = Todo('do the laundry')
    todo_3 = Todo('wash the dishes')
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    assert todo_list.incomplete() == [todo_1, todo_2, todo_3]
