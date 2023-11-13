# -*- coding: utf-8 -*-

def bengali_stem(word):
    # Define a list of suffixes to remove
    suffixes = ["ের", "ে"]

    # Iterate through the suffixes and remove them if they exist at the end of the word
    for suffix in suffixes:
        if word.endswith(suffix):
            word = word[:-len(suffix)]
            break

    return word
