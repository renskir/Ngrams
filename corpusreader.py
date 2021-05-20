import os.path
import nltk

class CorpusReader:
    """Read the contents of a directory of files, and return the results as
    either a list of lines or a list of words.

    The pathname of the directory to read should be passed when
    creating the class:

    >>> reader = CorpusReader(r"path/to/dir")
    """

    def __init__(self, path):
        """
        Initialize a CorpusReader object. This function stores the path to
        the corpus directory.
        """
        self.path = path
        if os.path.isdir(self.path) != True:
            raise ValueError(path + "doe snot exist or is not a directory")

    def sents(self):
        """"
        return the text of the corpus as a list of tokenized sentences
        --> Corpus becomes a list of tokens
        """
        for
    def lines(self):
        """Read all text in the corpus and return it as a list of lines"""
        # Your code here

corpus = CorpusReader("path/to/corpus/directory")
sentences = corpus.sents()  # a list of lists of tokens
#dit is een comment