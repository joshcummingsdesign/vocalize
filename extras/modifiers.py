from dragonfly import Choice


def modifiers(name: str) -> Choice:
    """
    The modifier key extras

    @since 0.1.0

    @param name: str - The name of this element
    """
    return Choice(name, {
        'up': 'up',
        'down': 'down',
        'left': 'left',
        'right': 'right',
    })
