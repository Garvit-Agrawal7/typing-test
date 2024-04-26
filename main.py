from word_list import WordList
from gui import App

# Getting the random word list
words = WordList()
list_of_words = words.getting_words(sample_size=20)

print(list_of_words)
list_of_words = list_of_words.replace(" ", ".")

# Creating the UI
app = App(word_list=list_of_words)
