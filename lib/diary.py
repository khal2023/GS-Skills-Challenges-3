from lib.diary_entry import *

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        if isinstance(entry, DiaryEntry):
            self.entries.append(entry)
        else:
            raise Exception("Valid input: DiaryEntry")

    def all(self):
        return self.entries

    def count_words(self):
        return sum(entry.count_words() for entry in self.entries)

    def reading_time(self, wpm):
        if type(wpm) == int:
            return round((self.count_words() / wpm), 1)
        else:
            raise Exception("Please enter a number for the words per minute")

    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        best_entries = {entry: entry.count_words() for entry in self.entries if entry.count_words() <= words_user_can_read}
        return max(best_entries, key=best_entries.get)

        
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
    