from lib.track import Track


# Given a title, an artist and a search keyword for the full title matches is true


def test_matches_on_full_title():
    track = Track('1989', 'taylor')
    assert track.matches('1989') == True

# Given a title, an artist and a keyword for a martial title matches is True
def test_matches_on_partial_title():
    track = Track('Blank Space', 'Taylor')
    assert track.matches('Blank') == True


#  Given a title, an artist and a keyword for a full artist matches is True

def test_matches_on_full_artist():
    track = Track('1989', 'taylor swift')
    assert track.matches('taylor swift') == True



#  Given a title, an artist and a keyword for a partial artist matches is True
def test_matches_on_partial_artist():
    track = Track('1989', 'taylor swift')
    assert track.matches('taylor') == True


#  Given a title, an artist and a keyword that doesn't match either matches is False
def test_matches_no_match():
    track = Track('1989', 'taylor swift')
    assert track.matches('Red') == False