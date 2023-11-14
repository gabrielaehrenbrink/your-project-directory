# Create a function that allows me to add tasks to todo list if a text includes the string #TODO.
def check_to_do(string):
    todo = '#TODO'
    todo_list = ''
    if todo in string:
        todo_list = string.replace("#TODO", "").strip()
        todo_list = ', '.join(item.strip() for item in todo_list.split(','))
        return f'Your todo list is: {todo_list}'

    else:
        return "You have done all your tasks, now chill!"


 
    # checks if string has TODO in the list
    # if string has TODO add task to todo_list
    # return todo_list
    # if no tasks return string that has "you have done all your tasks, now chill"

   