import re
import nltk
import itertools
"""
Defines the class BigramModel
"""


class BigramModel:
    """
    constructs bigrams from a given corpus,
    computes P_r(w_n | w) and smoothed P_r(w_n | w),
    returns possible next tokens, given a particular token
    and calculates perplexity of a given sentence
    """
    def __init__(self, sents):
        """
        :param sents: a list of a lists of tokens
        """
        # process sentences
        self.sentences = [self._process(sentence) for sentence in sents]

        # construct vocabulary
        self.vocabulary = list(set(itertools.chain(*self.sentences)))

        # construct bigrams
        bigrams = list(itertools.chain(*[nltk.bigrams(sentence) for sentence in self.sentences]))
        self.frequency_table = nltk.FreqDist(bigrams)

    @staticmethod
    def _process(sentence):
        """
        :param sentence: a sentence in the form of a list of tokens
        :return: processed sentence, meaning changed to lowercase,
        removed punctuation, and added start and end tokens
        """
        # remove punctuation
        # to lower case
        sentence = [token.lower() for token in sentence if re.search(r'[a-z]', token)]

        # add start and end tokens
        sentence.insert(0, '<s>')
        sentence.append('</s>')

        return sentence

    def p_raw(self, w, w_n):
        """
        :param w: any token in the vocabulary
        :param w_n: any token in the vocabulary
        :return: P_r(w_n | w) , the raw (unsmoothed) probability of
        seeing token w_n if we have just seen token w.
        """
        return self.frequency_table[(w, w_n)] / sum(self.frequency_table.values())

    def p_smooth(self, w, w_n):
        """
        :param w: any token in the vocabulary
        :param w_n: any token in the vocabulary
        :return: P(w_n | w) , the Laplace-smoothed probability of
        seeing token w_n if we have just seen token w.
        """
        return (self.frequency_table[(w, w_n)] + 1) / (sum(self.frequency_table.values()) + len(self.vocabulary))

    def successors(self, w):
        """
        :param w: any word
        :return: a list of pairs (w_i, c_i) , where w_i is a token that
        might follow w , and c_i is its raw (unsmoothed) bigram
        probability, P_r(w_i | w). Tokens with zero probability are
        not be included in the result.
        """
        successors = [(w_i, self.frequency_table[(w, w_i)] / sum(self.frequency_table.values()))
                      for w_i in self.vocabulary
                      if self.frequency_table[(w, w_i)] != 0]
        return successors

    def perplexity(self, sent):
        """
        :param sent: a sentence in the form of a list of tokens
        :return: perplexity
        using the Laplace-smoothed probability model. If any
        unknown words are seen, returns 0.
        """
        # processing the sentences
        sent = self._process(sent)
        print(sent)

        # construct onegrams in order to calculate p(w1)
        onegrams = nltk.ngrams(list(itertools.chain(*self.sentences)), 1)
        token_frequencies = nltk.FreqDist(onegrams)

        # calculating p(sent)
        p = token_frequencies[(sent[0], )] / sum(token_frequencies.values())
        print(p)
        for token1, token2 in zip(sent[:-1], sent[1:]):
            p *= self.p_smooth(token1, token2)

        # return perplexity, if any unknown words are seen, return 0
        return (1 / p)**(1/len(sent)) if p != 0 else 0
