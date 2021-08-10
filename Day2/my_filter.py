#!/usr/bin/env python3
"""
Author : t21 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""
import operator
from functools import reduce
from pprint import pp


def count_words(doc):
    normalize_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalize_doc.split():
        frequencies[word] = frequencies.get(word, 0)+1
    return frequencies

def combine_counts(d1,d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d
# --------------------------------------------------
def main():
    """Make your noise here"""
    negatives = []
    positives = []
    numbers = [-7, 2, 5, 8, -1, 90, -2, -33, 0, 12]
    accumulator = operator.add(numbers[0], numbers[1])
    for item in numbers[2:]:
        accumulator = operator.add(accumulator, item)
    #print(accumulator)

    document = ['It was the best of times, it was the worst of times',
               'I went to the woods becasue I wished to love deliberatly, to front on the essentials',
               'Friedns, Romans, countrymen, lend me your ears; I come to bury Ceaser, not to praise him',]
    counts = map(count_words, document)
    total_counts = reduce(combine_counts, counts)
    pp(total_counts)

# --------------------------------------------------
if __name__ == '__main__':
    main()
