from corpusreader import CorpusReader
from model import BigramModel

import os.path
import random
import argparse

def generate_sentence(model):
    """
    :param model:
    :return:
    """
    sentence = str()
    new_token = '<s>'
    while new_token is not '</s>':
        successors = model.successors(new_token)
        sorted_successors = successors.sort(key=lambda x: x[1])
        new_token = random.choice(sorted_successors[:10, 0])
        sentence += (new_token + ' ') if new_token != '</s>' else '. '

    sentence[0].upper()
    return sentence


def generate(model, n):
    """
    :param model: Bigram model object
    :param n: any number, amount of sentences generated
    :return: a paragraph of n random sentences as a single (formatted) string.
    """
    paragraph = str()
    for _ in range(n):
        paragraph += generate_sentence(model)
    return paragraph


def main():
    """
    Constructs a bigram model.
    Generates five random sentences.
    Calculates the perplexity of a few test sentences.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, help='path to corpus file', default='.')
    args = parser.parse_args()

    corpus_reader = CorpusReader(args.file)
    model = BigramModel(corpus_reader.sents())

    test_sentences = ['Suggestive, Watson, is it not?',
                     'It is amazing that a family can be torn apart by something as simple as a pack of wild dogs!',
                     'So spoke Sherlock Holmes and turned back to the great scrapbook in which he was arranging and indexing some of his recent material.',
                     'What I like best about my friends is that they are few.',
                     'Friends what is like are they about I best few my that.']

    # maakt 2 keer een paragraaf met 5 zinnen
    for _ in range(2):
        print(generate(model, 5) + '\n')

    # for each sentence in the testsentences print the perplexity
    for sentence in test_sentences:
        print(model.perplexity(test_sentences))


if __name__ == '__main__':
    main()

