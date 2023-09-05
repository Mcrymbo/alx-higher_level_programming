#!/usr/bin/python3


def text_indentation(text):
   """ function to print that prints a text after '.:?
    characters are encountered """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    st = text[:]
    for delim in ".?:":
        line = st.split(delim)
        st = ""
        for i in line:
            i = i.strip()
            st = i + delim if st is "" else st + '\n\n' + i + delim
    print(st[:-3], end='')
