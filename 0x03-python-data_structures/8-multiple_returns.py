#!/usr/bin/python3
def multiple_returns(sentence):
    first = list(sentence)
    if sentence == ' ':
        first[0] = None
    return(len(sentence), ''.join(first[:1]))
