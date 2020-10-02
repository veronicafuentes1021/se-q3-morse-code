#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Veronica Fuentes'

from morse_dict import MORSE_2_ASCII as morse_dict
import re


def decode_bits(bits):
    find_spaces = ''
    find_dashes = ''
    find_gaps = ''
    find_zeros = ''
    find_ones = ''
    morse_efied = ''

    strip_zeros = bits.strip('0')
    zeros_ones = re.split('(0+)', strip_zeros)
    pattern = len(min(zeros_ones, key=len))
    for part in range(pattern):
        find_spaces += '0000000+'
        find_dashes += '111'
        find_gaps += '000'
        find_zeros += '0'
        find_ones += '1'
    spaces = re.sub(find_spaces, 'b   b', strip_zeros)
    dashes = re.sub(find_dashes, 'b-b', spaces)
    gaps = re.sub(find_gaps, 'b b', dashes)
    zeros = re.sub(find_zeros, 'bb', gaps)
    dots = re.sub(find_ones, 'b.b', zeros)
    ready = re.split('b', dots)
    morse_efied += ''.join(ready)
    return morse_efied
    # print(spaces)


def decode_morse(morse):
    holder = []
    stripped = morse.strip()
    morsed = re.split(r'(\s+)', stripped)
    for char in morsed:
        if char == '   ':
            holder.append(' ')
        elif char == ' ':
            pass
        else:
            holder.append(morse_dict[char])
    translated = ''.join(holder)
    return translated


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa
    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
