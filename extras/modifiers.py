from dragonfly import Choice


def modifiers(name: str) -> Choice:
    """
    The modifier extras.

    @unreleased

    @param name: str - The name of this element.
    """
    return Choice(name, {
        'tab': 'tab',
    })
