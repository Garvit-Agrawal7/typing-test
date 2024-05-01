from gui import App
from word_list import WordList

# Getting the random word list
words = WordList()
list_of_words = words.getting_words(sample_size=30)

# Creating the UI
app = App(word_list=list_of_words)
