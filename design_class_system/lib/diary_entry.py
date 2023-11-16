class DiaryEntry:
    
    def __init__(self, contents): 
        self.contents = contents
        self.head = 0

    def count_words(self):
        words = self.contents.split(" ")
        return len(words)

    def reading_time(self, wpm):
        words = self.contents.split(' ')
        return len(words) / wpm
    

        
    