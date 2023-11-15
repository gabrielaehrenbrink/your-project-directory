# 1. Describe the Problem
# Create a class to keep track of music listening, add tracks that have been listened and return a list of those tracks

# 2. Design the Class Interface
# The interface of a class includes:

# The name of the class.
# The design of its initializer, the parameters it takes, and their data types
# The design of any properties the user will need to read or write, and their data types
# The design of its public methods, including:
# Their names and purposes
# What parameters they take and the data types
# What they return and that data type
# Any other side effects they might have

class MusicTracker():
    def __init__(self):
        self.tracker = []
    def add_songs(self, song):
        if song not in self.tracker:
            self.tracker.append(song)
    def songs_heard(self):
        return self.tracker
        # adds songs listened to list (tracker)
        # returns tracker
        # if song already in tracker return already heard song message + list of songs
       

