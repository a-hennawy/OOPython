import random


class WordFinder:
    """WordFinder: finds random words from a dictionary.
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        word_file = open(path)
        self.words = self.read(word_file)
        print(f"{len(self.words)} words read")

    def __repr__(self):
        return f"<WordFinder read {self.read()} words>"

    def read(self, word_file):
        return [word.strip() for word in word_file]

    def random(self):
        return random.choice(self.words)
