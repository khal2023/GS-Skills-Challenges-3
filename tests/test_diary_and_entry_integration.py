import pytest
from lib.diary import *
from lib.diary_entry import *

# Word blocks
_10_words = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a."    
_50_words = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Pellentesque leo enim, egestas aliquam vehicula rhoncus, tempor vitae justo. Sed 
tincidunt dui commodo, molestie orci sed, ullamcorper eros. Etiam nibh eros, consequat 
sit amet pulvinar non, faucibus non felis. Praesent faucibus a nibh ultricies consectetur. 
Nulla fringilla, elit non accumsan condimentum."""
_100_words = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean efficitur 
iaculis mauris, in suscipit sapien rhoncus nec. Sed sodales elit in lectus 
bibendum, a vestibulum mauris porttitor. Sed malesuada, ex eget elementum 
sollicitudin, erat eros ultricies velit, id varius orci ex a lacus. Vivamus 
a lectus metus. Donec eu commodo velit, non sodales tortor. Vestibulum ante 
ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Mauris 
et nunc pretium libero pharetra ultricies sit amet a felis. Mauris pretium 
ipsum eget mi posuere ultricies. Etiam vel sapien dolor. Integer dapibus mi 
vel erat bibendum consequat. In laoreet est dui."""
_200_words = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. In id arcu odio. Nullam 
consectetur, turpis sed condimentum tempus, ex tellus feugiat felis, vel eleifend ex ex eu ante. 
Curabitur rutrum, neque non sollicitudin elementum, nulla augue scelerisque erat, eget mattis 
magna mi non lectus. Nulla non tortor in velit vulputate porttitor. Nam pellentesque ac odio a 
pretium. Aliquam a odio facilisis, vehicula sapien non, dignissim enim. Nunc tempor imperdiet lacinia. 
Vestibulum vel sem at ex placerat vulputate. Suspendisse iaculis, mi et varius condimentum, leo lorem 
pretium felis, eu tincidunt lectus risus in neque. In turpis tortor, pulvinar vel pellentesque vel, 
molestie a ligula. Donec non ligula vestibulum, hendrerit purus ac, maximus mi. Praesent dictum tellus 
et erat scelerisque  sollicitudin vitae eu diam. Curabitur vulputate arcu et ipsum malesuada, ut ornare 
sem sodales. Fusce eu efficitur lectus. Vestibulum semper cursus turpis, sit amet finibus metus consequat 
rutrum. Etiam volutpat imperdiet velit, eu maximus ante volutpat vitae. Ut vehicula lacus non nulla 
mattis molestie. Aliquam non dictum nulla. Phasellus commodo massa non justo faucibus, vitae malesuada 
felis vestibulum. Mauris rhoncus bibendum semper. Praesent feugiat, nibh sit amet pretium tempor, odio 
magna finibus ex, sit amet aliquam dui mauris in turpis. Nulla blandit."""

# Test diary adds and returns an entry
def test_diary_adds_and_returns():
    diary = Diary()
    entry1 = DiaryEntry("Wednesday", "Today was a great day")
    diary.add(entry1)
    assert diary.all() == [entry1]

# Refuses arguments that aren't diary entries  
def test_only_accepts_diaries():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.add(7)
    assert str(e.value) == "Valid input: DiaryEntry"

# Returns empty list when no entries added
def test_returns_empty_when_nothing_added():
    diary = Diary()
    assert diary.all() == []

# Correctly counts words in all diary entries
def test_count_words_in_all_diaries():
    diary = Diary()
    diary.add(DiaryEntry("Wed", _10_words))
    diary.add(DiaryEntry("Thu", _50_words))
    diary.add(DiaryEntry("Fri", _100_words))
    assert diary.count_words() == 160

# Correctly returs the total reading time of all entries 
def test_total_reading_time():    
    diary = Diary()
    entry1 = DiaryEntry("Wed", _10_words)
    entry2 = DiaryEntry("Thu", _50_words)
    entry3 = DiaryEntry("Fri", _100_words)
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.reading_time(10) == 16

# Reading time refuses non number input
def test_non_int_input():    
    diary = Diary()
    entry1 = DiaryEntry("Wed", _10_words)
    entry2 = DiaryEntry("Thu", _50_words)
    entry3 = DiaryEntry("Fri", _100_words)
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    with pytest.raises(Exception) as error:
        diary.reading_time("Hello")
    assert str(error.value) == "Please enter a number for the words per minute"

# Find the best entry for reading
def test_find_appropriate_reading_chunk():
    diary = Diary()
    entry1 = DiaryEntry("Wed", _10_words)
    entry2 = DiaryEntry("Thu", _50_words)
    entry3 = DiaryEntry("Fri", _100_words)
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.find_best_entry_for_reading_time(45, 2) == entry2

# Returns error when there is no best entry 

# Returns choice of two or more entries to choose from if there are any