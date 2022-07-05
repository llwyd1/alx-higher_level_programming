#!/usr/bin/python3

def multiple_returns(sentence):
    str_len = len(sentence)
    _tuple = ()

    if str_len == 0:
        _tuple = 0, None
    else:
        _tuple = str_len, sentence[0]
    return _tuple
