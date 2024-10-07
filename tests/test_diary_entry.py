import pytest
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


# Adds title and contents
def test_add_entry():
    entry = DiaryEntry("Wednesday", "Today was a great day")
    assert entry.title == "Wednesday"
    assert entry.contents == "Today was a great day"

# Refuses non-string input
def test_refuses_nonstring_input():
    with pytest.raises(Exception) as error:
        entry = DiaryEntry("Tuesday", 7)
    assert str(error.value) == "DiaryEntry only accepts text as input"

# Caluclates the number of words in contents correctly
def test_counts_10_words():
    entry = DiaryEntry("Monday", _10_words)
    assert entry.count_words() == 10
    entry = DiaryEntry("Tuesday", _50_words)
    assert entry.count_words() == 50
    entry = DiaryEntry("Wednesday", _100_words)
    assert entry.count_words() == 100

    # entry1 = DiaryEntry("Wed", _10_words)
    # entry1.reading_time(10)
    # entry2 = DiaryEntry("Thu", _50_words)
    # entry2.reading_time(10)
    # entry3 = DiaryEntry("Fri", _100_words)
    # entry3.reading_time(10)