#!/usr/bin/python3
""" Module for line indentation """


def text_indentation(text):
    """ function to print that prints a text after '.:?
    characters are encountered"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    spaces = False
    new_text = text.replace(". ", ".").replace("? ", "?").replace(": ", ":")
    new_text = text.replace(" .", ".").replace(" ?", "?").replace(" :", ":")
    for ch in new_text:
        ch.strip()
        if ch in [".", "?", ":"]:
            print(ch)
            print()
            spaces = True
        else:
            if spaces is False:
                print(ch, end='')
            else:
                if ch != " ":
                    print(ch.strip(), end='')
                    spaces = False
