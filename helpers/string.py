def filter_char(char):
    """
    Filter special characters
    """
    match char:
        case 'bang':
            return '!'
        case 'com':
            return ','
        case _:
            return char
