#!/usr/bin/python3
# returns the first character and length of a string.

def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
