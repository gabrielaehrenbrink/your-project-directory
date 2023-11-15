from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_add_diary():
    diary = Diary()
    entry = DiaryEntry("Dear diary", "Today was a day of connection and laughter.")
    diary.add(entry)
    title = diary.diary_entry[0].title
    content = diary.diary_entry[0].contents
    result = [title, content]
    assert result == ["Dear diary", "Today was a day of connection and laughter."]

def test_all_diary():
    diary = Diary()
    entry = DiaryEntry("Dear diary", "Today was a day of connection and laughter.")
    entry1 = DiaryEntry("Hello", "As I returned home, I couldn't help but feel grateful for the people who fill my life with joy and warmth.")
    entry2 = DiaryEntry("Dear Jonny", "Today was a good day")
    diary.add(entry)
    diary.add(entry1)
    diary.add(entry2)
    result = diary.all()
    assert result == ["Today was a day of connection and laughter.",
        "As I returned home, I couldn't help but feel grateful for the people who fill my life with joy and warmth.",
        "Today was a good day"
        ]

def test_count_words():
    diary = Diary()
    entry = DiaryEntry("Dear diary", "Today was a day of connection and laughter.")
    entry1 = DiaryEntry("Hello", "As I returned home, I couldn't help but feel grateful for the people who fill my life with joy and warmth.")
    entry2 = DiaryEntry("Dear Jonny", "Today was a good day")
    diary.add(entry)
    diary.add(entry1)
    diary.add(entry2)
    result = diary.count_words()
    assert result == 34

def test_reading_time():
    diary = Diary()
    entry = DiaryEntry("Dear diary", "Today was a day of connection and laughter.")
    entry1 = DiaryEntry("Hello", "As I returned home, I couldn't help but feel grateful for the people who fill my life with joy and warmth.")
    entry2 = DiaryEntry("Dear Jonny", "Today was a good day")
    diary.add(entry)
    diary.add(entry1)
    diary.add(entry2)
    result = diary.reading_time(1)
    assert result == 34

def test_second_chunck():
    entry1 = DiaryEntry("Hello", "As I returned home, I couldn't help but feel grateful for the people who fill my life with joy and warmth.")
    result = entry1.reading_chunk(1, 5)
    result = entry1.reading_chunk(1, 5)
    assert result == "couldn't help but feel grateful"

def test_best_entry():
    diary = Diary()
    entry = DiaryEntry("Dear diary", "Today was a day of connection and laughter.")
    entry1 = DiaryEntry("Hello", "As I returned home, I couldn't help but feel grateful for the people who fill my life with joy and warmth.")
    entry2 = DiaryEntry("Dear Jonny", "Today was a good day")
    diary.add(entry)
    diary.add(entry1)
    diary.add(entry2)
    result = diary.find_best_entry_for_reading_time(1, 7)
    assert result == "Today was a day of connection and laughter."