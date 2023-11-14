# To improve writting skills, create a function that starts with a capital letter and ends with a pontuation mark.
# punctuation mark = Full stop or question mark

def writting_skills(string):
    question_words = ["what", "who", "where", "why", "how"]
    if string.isupper():
        new_string = string.lower()
        return new_string.capitalize() + "!"
    elif any(word in string.lower() for word in question_words):
        return string.capitalize() + "?"
    else:
        return string.capitalize() + "."
    # takes first letter of string and sets it to uppercase
    # if sentence starts with question word add ? to the end, it not add .
    # if sentence all uppercase, only leave first letter upper case and add ! to the endtouc