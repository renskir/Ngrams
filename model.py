class BigramModel:
    def __init__(self):
        pass

    def p_raw(self, w, w_n):
        """
        :param w:
        :param w_n:
        :return: P_r(w_n | w) , the raw (unsmoothed) probability of
        seeing token w_n if we have just seen token w.
        """

    def p_smooth(self, w, w_n):
        """
        :param w:
        :param w_n:
        :return: P(w_n | w) , the Laplace-smoothed probability of
        seeing token w_n if we have just seen token w.
        """

    def successors(self, w):
        """
        :param w:
        :return:    a list of pairs (w_i, c_i) , where w_i is a token that
        might follow w , and c_i is its raw (unsmoothed) bigram
        probability, P_r(w_i | w) . Tokens with zero probability need
        not be included in the result.
        """

    def perplexity(self, sent):
        """
        :param sent:
        :return:
        Given a sentence in the form of a list of tokens, clean it up the same way the training input was
        cleaned up (remove punctuation-only tokens, change to lowercase,
        surround with <s> and </s> ), and return its perplexity
        using the Laplace-smoothed probability model. If any
        unknown words are seen, return 0.
        """