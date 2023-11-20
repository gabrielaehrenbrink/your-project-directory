#  When I add multiple tracks and I search keyword, I get tracks that match that keyword
from dbm.ndbm import library
from unittest.mock import Mock
from lib.music_library import MusicLibrary

def test_searcher_by_keyword():
    library = MusicLibrary()
    fake_matching = Mock()
    fake_matching.matches.return_value = True
    # fake_matching = FakeMatchingTrack()
    library.add(fake_matching)
    fake_not_matching = Mock()
    fake_not_matching.matches.return_value = False
    library.add(fake_not_matching)
    assert library.search('hello') == [fake_matching]


# Initially tracks is empty

def test_tracks_empty_initially():
    library = MusicLibrary()
    assert library.tracks == []


# When add tracks they show in tracks list
# 

def test_tracks_get_added_and_list_out():
    library = MusicLibrary()
    track1 = Mock()
    track2 = Mock()
    track3 = Mock()
    library.add(track1)
    library.add(track2)
    library.add(track3)
    assert library.tracks == [track1, track2, track3] 
