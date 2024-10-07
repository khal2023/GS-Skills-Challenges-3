class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        if type(title) == str and type(contents) == str:
            self.title = title
            self.contents = contents
        else:
            raise Exception("DiaryEntry only accepts text as input")

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return (self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        words = self.contents.split()
        words_to_read = minutes * wpm
        chunk_end_index = self.chunk_start_index + words_to_read
        words_read = " ".join(words[self.chunk_start_index:chunk_end_index])

        if chunk_end_index >= len(words):
            self.chunk_start_index = 0
        else:
            self.chunk_start_index = chunk_end_index
            
        return words_read