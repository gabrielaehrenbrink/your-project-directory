from lib.music_tracker import MusicTracker

def test_one_song_added():
    song_tracker = MusicTracker()
    song_tracker.add_songs('Red')
    result = song_tracker.songs_heard()
    assert result == ['Red']
    # tests if one song was added to tracker

def test_multiple_songs_added():
    # tests if multiple songs were added to tracker
    song_tracker = MusicTracker()
    song_tracker.add_songs('Red')
    song_tracker.add_songs('Out of the woods')
    song_tracker.add_songs('Is it over now')
    result = song_tracker.songs_heard()
    assert result == ['Red', 'Out of the woods', 'Is it over now']

def repeated_songs_added():
    # returns message of song already in tracker + tracker of songs
    song_tracker = MusicTracker('Red')
    song_tracker = MusicTracker('Red')
    song_tracker = MusicTracker('Is it over now')
    repeated_message = 'Song is already in tracker'
    assert song_tracker == 'Red, Is it over now' + repeated_message