from corpusreader import CorpusReader
from model import BigramModel
import nltk

import os.path
import random
import argparse
"""
Constructs a bigram model.
Generates two paragraphs of five random sentences.
Calculates the perplexity of a few test sentences.
"""


def generate_sentence(model):
    """
    :param model: a bigram model
    :return: a random sentence generated by the bigram model
    """
    # initialises an empty sentence
    sentence = str()
    new_token = '<s>'
    end_token = '</s>'
    # generates new words until the end token is reached
    while new_token != end_token:
        # returns successors and sorts them
        successors = model.successors(new_token)
        successors.sort(key=lambda x: x[1], reverse=True)

        # takes the first few successors with the highest probability and chooses one at random
        successors = [successor[0] for successor in successors[:10]]
        new_token = random.choice(successors)

        # if the sentence is too short, another token will be chosen
        while new_token == end_token and len(sentence.split(' ')) < 5:
            new_token = random.choice(successors)

        sentence += (new_token + ' ') if new_token != end_token else ''

    # capitalizes first word and adds a period at the end of the sentence
    sentence = sentence.capitalize()
    sentence = sentence[:-1] + '. '

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
    Generates two paragraphs of five random sentences.
    Calculates the perplexity of a few test sentences.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, help='path to corpus file', default='./train')
    args = parser.parse_args()

    corpus_reader = CorpusReader(args.file)
    model = BigramModel(corpus_reader.sents())

    test_sentences = ['Suggestive, Watson, is it not?',
                     'It is amazing that a family can be torn apart by something as simple as a pack of wild dogs!',
                     'So spoke Sherlock Holmes and turned back to the great scrapbook in which he was arranging and indexing some of his recent material.',
                     'What I like best about my friends is that they are few.',
                     'Friends what is like are they about I best few my that.']

    # prints two paragraphs with each five sentences
    for _ in range(2):
        print(generate(model, 5) + '\n')

    # for each sentence in the test_sentences print the perplexity
    for sentence in test_sentences:
        print(model.perplexity(nltk.word_tokenize(sentence)))


if __name__ == '__main__':
    main()

