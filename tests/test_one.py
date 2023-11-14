# '''
# Step 1:
#     calculate an estimate of reading time for someone who reads at 200 words per min
# '''
from lib.one import *

# '''
# Given a string of 50 words
# Return string saying will take 15 secs
# '''
def test_one_50():
    book = "In the quiet embrace of dusk, shadows dance with fading sunlight, painting the sky in hues of lavender and gold. Nature's symphony whispers through rustling leaves, serenading the day's end. A tranquil moment unfolds, weaving a tapestry of fleeting beauty that blankets the world in the gentle embrace of evening."
    time = one(book)
    assert time == 'You will take 15 seconds to read the book'

# '''
# Given an empty string
# Return string saying will take 0 secs
# '''
def test_one_0():
    book = ""
    time = one(book)
    assert time == 'You will take 0 seconds to read the book'