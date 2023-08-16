#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_num = {
            'I': 1, 'V': 5, 'X': 1, 'L': 50, 'C': 100, 'D': 500, 'M': 100
            }
    prev = 0
    res = 0
    for ch in reversed(roman_string):
        value = roman_num[ch]
        if value >= prev:
            res += value
        else:
            res -= value
        prev = value
    return res
