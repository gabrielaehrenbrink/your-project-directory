class Diary:
    def __init__(self):
        self.diary_entry = []
        
    def add(self, entry):
        # title, contents = entry
        # entry = DiaryEntry(title, contents)
        # self.entry = entry 
        self.diary_entry.append(entry)
    
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        
    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        contents_list = []
        for diary_entry_item in self.diary_entry:
            contents_list.append(diary_entry_item.contents)
        return contents_list

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        count = 0 
        for word in self.diary_entry:
            count += word.count_words()
        return count
            
    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        count = 0 
        for word in self.diary_entry:
            count += word.reading_time(wpm)
        return count

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   but not over, the length that the user could read in the minutes
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   they have available given their reading speed.
        time_diff_list = []
        contents_list = self.all()
        for diary_entry in contents_list:
            exert_reading_time = len(diary_entry.split(' ')) / wpm
            time_diff = abs(exert_reading_time - minutes)
            time_diff_list.append(time_diff)
        min_value = min(time_diff_list)
        min_index = time_diff_list.index(min_value)
        correct_exert = contents_list[min_index]
        return correct_exert