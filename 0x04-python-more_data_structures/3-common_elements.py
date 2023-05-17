#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_char = set(set_1) & set(set_2)
    if len(common_char) > 0:
        return(common_char)
