
from lib.music_library import MusicLibrary
from lib.track import Track


# When I add multiple, they are reflected in the tracks list

def test_adds_and_lists_multiple_tracks():
    library = MusicLibrary()
    track_1 = Track("Title 1", "Artist 1")
    track_2 = Track("Title 2", "Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]


#  When I add multiple tracks and I search for one track I get the track back

def test_search_for_track_by_full_title():
    library = MusicLibrary()
    track_1 = Track("Title 1", "Artist 1")
    track_2 = Track("Title 2", "Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.search('Title 1') == [track_1]