import os.path
import nltk
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
        # Raises an Error if the path doesn't exist
        if not os.path.isdir(self.path):
            raise ValueError(path + " isn't a directory, or doesn't exist at all")

    def sents(self):
        """
        Reads the text of the corpus and return it as a list of tokenized words.
        """

        text = str()
        for file in os.listdir(self.path):
            # checks if the given path contains a text file and opens it
            if file.endswith(".txt"):
                with open(self.path + "/" + file) as connection:
                    text += connection.read()

        # tokenizes the text to sentences and tokenizes the tokenized sentences to words
        sentences_list = nltk.sent_tokenize(text)
        word_list = [nltk.word_tokenize(sent) for sent in sentences_list]

        return word_list
