Diary plan README

``` python 

# Test diary adds and returns an entry
def test_diary_adds_and_returns():
    diary = Diary()
    entry1 = DiaryEntry("title", "Contents")
    diary.add(entry1)
    assert diary.all() == [entry1]    

```