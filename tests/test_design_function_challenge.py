from lib.design_function_challenge import check_to_do

# test if adding single task to todo list
def test_new_task():
    todo_list = check_to_do('wash the dishes #TODO')
    assert todo_list == "Your todo list is: wash the dishes"


# test if adding multiple tasks to todo list
def test_multiple_tasks():
    todo_list = check_to_do('wash the dishes #TODO, do the laundry #TODO')
    assert todo_list == "Your todo list is: wash the dishes, do the laundry"


# test if there are no todo tasks
def test_no_task():
    todo_list = check_to_do('')
    assert todo_list == "You have done all your tasks, now chill!"