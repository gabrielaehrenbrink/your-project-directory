from lib.test_drive_class import DiaryEntry

# given a title and content, format return a formatted entry "My Title: These are the contents"

def test_formats_with_title_contents():
    diary_entry = DiaryEntry("My title", "the content")
    result = diary_entry.format()
    assert result == "My title: the content"


def test_count_word_title_content():
    diary_entry = DiaryEntry("My title", "the content")
    result = diary_entry.count_words()
    assert result == 4

def test_reading_time():
    diary_entry = DiaryEntry("My title", "the content has to be a bit longer so blablabla")
    result = diary_entry.reading_time(2)
    assert result == f'You will take 5 minutes to read the content'

def test_reading_chunk():
    diary_entry = DiaryEntry("My title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == 'one two three four'

def test_reading_with_called_twice():
    diary_entry = DiaryEntry("My title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == 'three four'