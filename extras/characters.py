from dragonfly import Choice


def characters(name: str) -> Choice:
    """
    The character extras.

    @unreleased

    @param name: str - The name of this element.
    """
    return Choice(name, {
        # Phonetic Alphabet
        'alpha': 'a',
        'bravo': 'b',
        'charlie': 'c',
        'delta': 'd',
        'echo': 'e',
        'foxtrot': 'f',
        'golf': 'g',
        'hotel': 'h',
        'india': 'i',
        'juliet': 'j',
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

        # Special Characters
        'tick': '`',
        'tilde': '~',
        'bang': '!',
        'at': '@',
        'hash': '#',
        'dollar': '$',
        'percent': '%',
        'up carrot': '^',
        'amp': '&',
        'star': '*',
        'left print': '(',
        'right print': '(',
        'prints': '(',
        'minus': '-',
        'equals': '=',
        'plus': '+',
        'left bracket': '[',
        'right bracket': ']',
        'brackets': '[',
        'left brace': '{',
        'right brace': '}',
        'braces': '{',
        'backslash': '\\',
        'pipe': '|',
        'semicolon': ';',
        'colon': ':',
        'quote': "'",
        'double quote': '"',
        'comma': ',',
        'dot': '.',
        'left angle': '<',
        'right angle': '>',
        'angles': '<',
        'slash': '/',
        'question': '?',
    })
