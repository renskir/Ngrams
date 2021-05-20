import os.path
import nltk
import itertools
"""
CorpusReader opens a .txt file and tokenizes the words in it. Returns a list of words
"""

class CorpusReader:
    """
    Reads the contents of directory files
    """

    def __init__(self, path):
        """
        initialize a CorpusReader object, stores the path to the corpus directory
        """

        self.path = path
        if not os.path.isdir(self.path):                                    #Gives an Error if the path isn't correct
            raise ValueError(path + " isn't a directory, or doesn't exist at all")

    def sents(self):
        """
        Reads the text of the corpus and return it as a list of tokenized words.
        """

        text = str()
        for file in os.listdir(self.path):
            if file.endswith(".txt"):                                       #checks if the given path contains a text file and opens it
                with open(self.path + "/" + file) as connection:
                    text += connection.read()

        sentences_list = nltk.sent_tokenize(text)                           #tokenizes the text to sentences
        word_list = [nltk.word_tokenize(sent) for sent in sentences_list]   #tokenizes the tokenized sentences to words
        return word_list
