from dragonfly import Text


def repeat_text(n: int, text: str) -> None:
    """
    Repeat text n times

    @since 0.1.0
    """
    word = ''.join(text * n)
    Text(word, True).execute()
