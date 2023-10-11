#!/usr/bin/env python3
"""
Transliterate between the latin alphabet and some runic alphabets (futharks)
and the latin alphabet. Currently, the following futharcs are supported:
    - anglo-saxon
    - elder futharc
    - younger futharc
        - long-branch
        - short twig

Sources:
    https://en.wikipedia.org/wiki/Runic_(Unicode_block)
    https://en.wikipedia.org/wiki/Medieval_runes
    https://en.wikipedia.org/wiki/Runes
    https://sv.wikipedia.org/wiki/Runor
"""


midevial = {
    'a': 'ᛆ',
    'b': 'ᛒ',
    'c': 'ᛍ',
    'd': 'ᛑ',
    'Ð': 'ᚧ',
    'e': 'ᛂ',
    'f': 'ᚠ',
    'g': 'ᚵ',
    'h': 'ᚼ',
    'i': 'ᛁ',
    'k': 'ᚴ',
    'l': 'ᛚ',
    'm': 'ᛘ',
    'n': 'ᚿ',
    'o': 'ᚮ',
    'p': 'ᛔ', # (ᛕ)
    'q': 'ᛩ',
    'r': 'ᚱ',
    's': 'ᛋ', # or ᛌ
    't': 'ᛐ',
    'u': 'ᚢ',
    'v': 'ᚡ', # (ᚢ)
    'w': 'ᚥ',
    'x': 'ᛪ',
    'y': 'ᛦ', # (ᚤ ᛨ)
    'z': 'ᛎ',
    'Þ': 'ᚦ',
    'ä': 'ᛅ', # or ᛆ
    'ö': 'ᚯ'
    }

anglo_saxon = {
    'f': 'ᚠ',
    'u': 'ᚢ',
    'y': 'ᚣ', # y or yr?
    'th': 'ᚦ',
    'o': 'ᚩ',
    'a': 'ᚪ',
    'ae': 'ᚫ',
    'r': 'ᚱ',
    'c': 'ᚳ',
    'g': 'ᚷ',
    'w': 'ᚹ',
    'h': 'ᚻ',
    'n': 'ᚾ',
    'i': 'ᛁ',
    'j': 'ᛄ',
    'y': 'ᛇ',
    'p': 'ᛈ',
    'x': 'ᛉ',
    's': 'ᛋ',
    't': 'ᛏ',
    'b': 'ᛒ',
    'e': 'ᛖ',
    'm': 'ᛗ',
    'g': 'ᚹ',
    'l': 'ᛚ',
    'ing': 'ᛝ',
    'd': 'ᛞ',
    'oe': 'ᛟ',
    'ea': 'ᛠ',
    'ia': 'ᛡ',
    'eo': 'ᛢ',
    'k': 'ᛣ',
    'kk': 'ᛤ',
    'st': 'ᛥ'
    }

elder_futhark = { 
    'f': 'ᚠ',
    'u': 'ᚢ',
    't': 'ᚦ',
    'a': 'ᚨ',
    'r': 'ᚱ',
    'k': 'ᚲ',
    'g': 'ᚷ',
    'w': 'ᚹ',
    'h': 'ᚺ',
    'n': 'ᚾ',
    'i': 'ᛁ',
    'j': 'ᛃ',
    'y': 'ᛇ',
    'p': 'ᛈ',
    'z': 'ᛉ',
    's': 'ᛊ',
    't': 'ᛏ',
    'b': 'ᛒ',
    'e': 'ᛖ',
    'm': 'ᛗ',
    'g': 'ᚹ',
    'l': 'ᛚ',
    'y': 'ᛜ',
    'd': 'ᛞ',
    'o': 'ᛟ',
    }

younger_futhark_lb = {
    'f': 'ᚠ',
    'u': 'ᚢ',
    'th': 'ᚦ',
    'o': 'ᚬ',
    'r': 'ᚱ',
    'k': 'ᚴ',
    'h': 'ᚼ',
    'n': 'ᚾ',
    'i': 'ᛁ',
    'a': 'ᛅ',
    's': 'ᛋ',
    't': 'ᛏ',
    'b': 'ᛒ',
    'm': 'ᛘ',
    'l': 'ᛚ',
    'r': 'ᛦ'
    }

younger_futhark_st = {
    'f': 'ᚠ',
    'u': 'ᚢ',
    'th': 'ᚦ',
    'o': 'ᚭ',
    'r': 'ᚱ',
    'k': 'ᚴ',
    'h': 'ᚽ',
    'n': 'ᚾ',
    'i': 'ᛁ',
    'a': 'ᚽ',
    's': 'ᛌ',
    't': 'ᛐ',
    'b': 'ᛓ',
    'm': 'ᛙ',
    'l': 'ᛚ',
    'r': 'ᛧ'
    }


def to_runes(futhark, text):
    text = text.lower()
    for k, v in futhark.items():
        text = text.replace(k, v)
    return text


def to_text(futhark, text):
    text = text.lower()
    for k, v in futhark.items():
        text = text.replace(v, k)
    return text


def main():
    text = input('Enter text: ')
    print('\nText to runes')
    print('-------------')
    print('Elder futhark: ' + to_runes(elder_futhark, text))
    print('Anglo-Saxon:   ' + to_runes(anglo_saxon, text))
    print('Younger futhark long-branch:   ' + to_runes(younger_futhark_lb , text))
    print('Younger futhark short-twig:    ' + to_runes(younger_futhark_st, text))
    print('Midevial:    ' + to_runes(midevial, text))
    print('\nRunes to text')
    print('-------------')
    print('Elder futhark: ' + to_text(elder_futhark, text))
    print('Anglo-Saxon:   ' + to_text(anglo_saxon, text))
    print('Younger futhark long-branch:   ' + to_text(younger_futhark_lb , text))
    print('Younger futhark short-twig:    ' + to_text(younger_futhark_st, text))
    print('Midevial:    ' + to_text(midevial, text))


if __name__ == '__main__':
    main()
