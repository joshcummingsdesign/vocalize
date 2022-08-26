from dragonfly import Key


def repeat_key(n: int, spec: str, static: bool = False) -> None:
    """
    Repeat a keypress n times

    @since 0.1.0
    """
    key = Key(spec, static) * n
    key.execute()
