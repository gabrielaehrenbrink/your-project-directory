from lib.todo import TodoList
from lib.contacts import Contacts
from lib.diary_entry import DiaryEntry

class Diary():

    def __init__(self):
        self.diary_entry = []
        self.todo_list = TodoList('')
        self._contacts = Contacts()

    def add(self, entry):
        # add diary entry
        self.diary_entry.append(entry)

    def read_all_entries(self):
        contents_list = []
        for diary_entry_item in self.diary_entry:
            contents_list.append(diary_entry_item.contents)
        return contents_list
    
    # select diary entry to read based on reading time (minutes) and reading speed (wpm)
    def read_time(self, wpm, minutes):
        self.wpm = wpm
        self.minutes = minutes
        time_diff_list = []
        contents_list = self.read_all_entries()
        for diary_entry in contents_list:
            exert_reading_time = len(diary_entry.split(' ')) / wpm
            time_diff = abs(exert_reading_time - minutes)
            time_diff_list.append(time_diff)
        min_value = min(time_diff_list)
        min_index = time_diff_list.index(min_value)
        correct_exert = contents_list[min_index]
        return correct_exert
    
     # keep a todo list along with my diary
    def add_todo_list(self, todo):
        self.todo_list.entry_todo(todo)
        if todo in self.diary_entry:
            return "You have a todo item in your Diary"
    
    def my_task(self, todo):
        self.todo_list.entry_todo(todo)
        if todo in self.diary_entry:
            return todo
      
        
    def add_contacts(self, entry, contact):
        self._contacts.add_contact(contact)
        contact_info = f"{entry.contents} with {', '.join([f'{k}, {v}' for k, v in contact.items()])}"
        self.add(DiaryEntry(contact_info))
        return contact_info
    
    def get_number(self, name):
        if name in self._contacts._contacts:
            return self._contacts._contacts[name]
        else:
            return f"Contact {name} not in contacts"

      
    
