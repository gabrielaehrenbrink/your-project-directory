class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.read_so_far = 0
        
        # Parameters:
        #   title: string
        #   contents: string
    def format(self):
        return f"{self.title}: {self.contents}"
    #     # Returns:
    #     #   A formatted diary entry, for example:
    #     #   "My Title: These are the contents"
        

    def count_words(self):
    #     # Returns:
    #     #   int: the number of words in the diary entry
        return len(self.contents.split()) + len(self.title.split())

    def reading_time(self, wpm):
        self.wpm = wpm
        num_words = len(self.contents.split())
        return f'You will take {int(num_words/self.wpm)} minutes to read the content'
    #     # Parameters:
    #     #   wpm: an integer representing the number of words the user can read 
    #     #        per minute
    #     # Returns:
    #     #   int: an estimate of the reading time in minutes for the contents at
    #     #        the given wpm.
        

    def reading_chunk(self, wpm, minutes):
        words_user_read = wpm * minutes
        words = self.contents.split()
        start_chunck = self.read_so_far
        end_chunck = self.read_so_far + words_user_read
        chunk_words = words[start_chunck:end_chunck]
        self.read_so_far = end_chunck
        return " ".join(chunk_words)
    #     # Parameters
    #     #   wpm: an integer representing the number of words the user can read
    #     #        per minute
    #     #   minutes: an integer representing the number of minutes the user has
    #     #            to read
    #     # Returns:
    #     #   string: a chunk of the contents that the user could read in the
    #     #           given number of minutes
    #     #
    #     # If called again, `reading_chunk` should return the next chunk,
    #     # skipping what has already been read, until the contents is fully read.
    #     # The next call after that should restart from the beginning.
        
