def make_snippet(string):
    string_list = string.split(" ")
    if len(string_list) > 5:
        new_string =  " ".join(string_list[0:5])
        new_string = new_string + '...'
        return new_string
    else:
        return string