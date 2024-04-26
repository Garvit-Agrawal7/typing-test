import random


class WordList:
    def __init__(self):
        self.word = []

    def getting_words(self, sample_size):
        """Returns the list of words randomly chosen from a sample size."""
        with open('5000-words.txt', 'r') as f:
            content = f.readlines()
            for word in content:
                self.word.append(word.strip())
            f.close()
        random_list = random.sample(self.word, sample_size)
        return random_list
