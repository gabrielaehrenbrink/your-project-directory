def one(book):
#     '''
#     Count number of words in book and return reading time for 200 words per min
    
#     Parameters:
#         Book: a string containing words (a long one!)
# ​
#     Returns:
#         A time in seconds embedded in a string
    
#     Side effects:
#         N/A
#     '''
    string_list = [word for word in book.split(' ') if word != '']
    time = (len(string_list) / 200) * 60
    return f'You will take {int(time)} seconds to read the book'