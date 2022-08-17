from dragonfly import Text


def repeatable_text(n: int, text: str) -> None:
    """
    Repeat text n times

    @unreleased
    """
    word = ''.join(text * n)
    Text(word, True).execute()
