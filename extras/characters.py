from dragonfly import Choice


def characters(name: str) -> Choice:
    """
    The character extras.

    @unreleased

    @param name: str - The name of this element.
    """
    return Choice(name, {
        # Numbers
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',

        # Alphabet
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
        'x ray': 'x',
        'yankee': 'y',
        'zulu': 'z',

        # Special Characters
        'tick': '`',
        'tilde': '~',
        'bang': '!',
        'at': '@',
        'hash': '#',
        'dollar': '$',
        'mod': '%',
        'hat': '^',
        'amp': '&',
        'star': '*',
        'pars': '(',
        'left par': '(',
        'par': ')',
        'minus': '-',
        'score': '_',
        'equals': '=',
        'plus': '+',
        'brackets': '[',
        'left bracket': '[',
        'bracket': ']',
        'braces': '{',
        'left brace': '{',
        'brace': '}',
        'whack': '\\',
        'pipe': '|',
        'semi': ';',
        'cole': ':',
        'quote': "'",
        'double quote': '"',
        'com': ',',
        'dot': '.',
        'tags': '<',
        'left tag': '<',
        'tag': '>',
        'slash': '/',
        'quest': '?',
    })
