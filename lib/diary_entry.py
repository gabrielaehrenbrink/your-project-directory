class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string
    
    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.head = 0
    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        words = self.contents.split(" ")
        return len(words)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        words = self.contents.split(' ')
        return len(words) / wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        num_of_words = wpm * minutes
        words_list = self.contents.split(' ')
        chunk_list = words_list[self.head : self.head + num_of_words]
        self.head += num_of_words
        return ' '.join(chunk_list)