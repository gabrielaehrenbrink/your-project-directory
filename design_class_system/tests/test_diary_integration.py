from lib.contacts import Contacts
from lib.diary_entry import DiaryEntry
from lib.diary import Diary
from lib.todo import TodoList


#  Test single entry is being added
def test_single_entry_added():
    diary = Diary()
    entry = DiaryEntry("Today was a day of connection and laughter.")
    diary.add(entry)
    content = diary.diary_entry[0].contents
    result = [content]
    assert result == ["Today was a day of connection and laughter."]




# read all entries
def test_read_all_entries():
    diary = Diary()
    entry = DiaryEntry("Today was a day of connection and laughter.")
    entry2 = DiaryEntry("Last night was very fun.")
    diary.add(entry)
    diary.add(entry2)
    content = diary.read_all_entries()
    result = [content]
    assert result == [["Today was a day of connection and laughter.", "Last night was very fun."]]



# chose diary entry that is closest to reading time available based on wpm give and minutes available
def test_closest_reading_time():
    diary = Diary()
    entry = DiaryEntry("Today was a day of connection and laughter.")
    entry1 = DiaryEntry("Last night was very fun.")
    entry2 = DiaryEntry("Today was a good day, I studied, went to the gym, cooked a nice lunch to have at home, went out to the pub and blablabla")
    diary.add(entry)
    diary.add(entry1)
    diary.add(entry2)
    result = diary.read_time(1, 7)
    assert result == "Today was a day of connection and laughter."



# check todo list is added to diary

def test_todo_list_in_diary():
    diary = Diary()
    entry = DiaryEntry("Today was a day of connection and laughter.")
    todo = TodoList("walk the dog")
    diary.add(entry)
    diary.add_todo_list(todo)
    assert 'You have a todo item in your Diary'


def test_multiple_todo_list_in_diary():
    diary = Diary()
    entry = DiaryEntry("Today was a day of connection and laughter.")
    todo = TodoList("walk the dog")
    todo1 = TodoList("walk the cat")
    diary.add(entry)
    diary.add_todo_list(todo)
    diary.add_todo_list(todo1)
    assert 'You have a todo item in your Diary'

# call todo list and show just the todo tasks
def test_todo_task():
    diary = Diary()
    entry = DiaryEntry("Today was a day of connection and laughter.")
    todo = TodoList("walk the dog")
    diary.add(entry)
    diary.add_todo_list(todo)
    diary.my_task(todo)
    assert [todo]


# see if contacts are being added to each diary entry and then return the contact + diary entry

def test_see_contacts():
    diary = Diary()
    entry = DiaryEntry("Today was a day of connection and laughter")
    contact = {'Mike': '070737'}
    result = diary.add_contacts(entry, contact)
    assert result == 'Today was a day of connection and laughter with Mike, 070737'


# call contact name and return phone number
def test_get_number():
    diary = Diary()
    entry = DiaryEntry("Today was a day of connection and laughter")
    contact = {'Mike': '070737'}
    diary.add_contacts(entry, contact)
    result = diary.get_number('Mike')
    expected_result = '070737'
    assert result == expected_result

def test_get_number_no_number():
    diary = Diary()
    entry = DiaryEntry("Today was a day of connection and laughter")
    contact = {'Mike': '070737'}
    diary.add_contacts(entry, contact)
    result = diary.get_number('Gab')
    expected_result = "Contact Gab not in contacts"
    assert result == expected_result

def test_multiple_contacts():
    diary = Diary()
    entry = DiaryEntry("Today was a day of connection and laughter")
    entry2 = DiaryEntry("Today was a very sad day")
    contact = {'Mike': '070737'}
    contact2 = {'Gab': '35567'}
    diary.add_contacts(entry, contact)
    diary.add_contacts(entry2, contact2)
    result = diary.read_all_entries()
    expected_result = ['Today was a day of connection and laughter with Mike, 070737',
                       'Today was a very sad day with Gab, 35567']

    assert result == expected_result

