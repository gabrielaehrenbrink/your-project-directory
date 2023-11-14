from lib.string_builder import StringBuilder

# Test empty string
def test_empty_string_builder():
    string = StringBuilder()
    assert string.output() == ""

# Test single string
def test_single_string_builder():
    string = StringBuilder()
    string.add("hello")
    assert string.output() == "hello"

# Test add string and string size

def test_single_string_size_builder():
    string = StringBuilder()
    string.add("hello")
    assert string.size() == 5


# Add multiple strings

def test_multiple_string_builder():
    string = StringBuilder()
    string.add("hello")
    string.add(" ")
    string.add("gabriela")
    assert string.output() == "hello gabriela"

# multiple strings size
def test_multiple_string_size_builder():
    string = StringBuilder()
    string.add("hello")
    string.add(" ")
    string.add("gabriela")
    assert string.size() == 14