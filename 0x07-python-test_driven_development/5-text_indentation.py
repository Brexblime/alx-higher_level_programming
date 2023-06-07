#!/usr/bin/python3
"""
defines a text identation.
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for c in [".", "?", ":"]:
        text = text.replace(c, c + "\n\n")

    lines = [line.strip() for line in text.split("\n")]
    print("\n".join(lines))
