from dragonfly import Choice


def special_chars():
    return Choice('char', {
        'alpha': 'a',
        'bravo': 'b',
        'charlie': 'c',
        'delta': 'd',
        'echo': 'e',
        'foxtrot': 'f',
        'golf': 'g',
        'hotel': 'h',
        'india': 'i',
        'jay': 'j',
        'kilo': 'k',
        'lima': 'l',
        'mike': 'm',
        'november': 'n',
        'oscar': 'o',
        'papa': 'p',
        'quebec': 'q',
        'romeo': 'r',
        'sierra': 's',
        'tango': 't',
        'uniform': 'u',
        'victor': 'v',
        'whiskey': 'w',
        'xray': 'x',
        'yankee': 'y',
        'zulu': 'z',
        'comma': ',',
        'colon': ':',
        'quotes': "'",
        'double quotes': '"',
        'bang': '!',
        'at': '@',
        'hash': '#',
        'dollar': '$',
        'percent': '%',
        'up carrot': '^',
        'carrot up': '^',
        'ampersand': '&',
        'star': '*',
        'left pea': '(',
        'right pea': '(',
        'peas': '(',
        'left bracket': '[',
        'right bracket': ']',
        'brackets': '[',
        'left brace': '{',
        'right brace': '}',
        'braces': '{',
        'minus': '-',
        'plus': '+',
        'equals': '=',
        'left angle': '<',
        'right angle': '>',
        'angles': '<',
    })
