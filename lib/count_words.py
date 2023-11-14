def count_words(string):
    string_list = [word for word in string.split(' ') if word != '']
    return f'This string has {len(string_list)} words'