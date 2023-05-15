#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == ' ':
        sentence = [None] + sentence[1:]
    return len(sentence), sentence[:1]
