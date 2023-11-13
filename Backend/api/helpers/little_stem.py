# -*- coding: utf-8 -*-

def bengali_stem_er(word):
    # Define a list of suffixes to remove
    suffixes = ["ের", "ে"]

    # Iterate through the suffixes and remove them if they exist at the end of the word
    for suffix in suffixes:
        if word.endswith(suffix):
            word = word[:-len(suffix)]
            break

    return word

def bengali_stem_ta(word):
    # Define a list of suffixes to remove

    suffixes = ["টি", "টা", "টার", "টির"]

    # Iterate through the suffixes and remove them if they exist at the end of the word
    for suffix in suffixes:
        if word.endswith(suffix) :
            word = word[:-len(suffix)]
            break

    return word

def bengali_stem_ra(word):
    # Define a list of suffixes to remove

    suffixes = ["র"]

    # Iterate through the suffixes and remove them if they exist at the end of the word
    for suffix in suffixes:
        if word.endswith(suffix) and word!="কার" and word!="স্কুটার":
            word = word[:-len(suffix)]
            break

    return word