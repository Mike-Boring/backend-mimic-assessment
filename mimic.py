#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Mike Boring"

import random
import sys
import json


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """

    with open(filename) as f:
        result = {'': 'I'}
        i = 1
        split_file = f.read().split()
        list_length = len(split_file)
        while i <= list_length:
            for word in split_file:
                if i == list_length:
                    if word not in result:
                        result[word] = ['']
                        i += 1
                    else:
                        result[word].append('')
                        i += 1
                else:
                    if word not in result:
                        result[word] = [split_file[i]]
                        i += 1
                    else:
                        result[word].append(split_file[i])
                        i += 1
        for k, v in sorted(result.items()):
            print(k, ':', v)
        return result
        #print(json.dumps(result, indent=0))


def print_mimic(mimic_dict, start_word):
    """Given a previously created mimic_dict and start_word,
    prints 200 random words from mimic_dict as follows:
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    # +++your code here+++
    pass


# Provided main(), calls mimic_dict() and print_mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
