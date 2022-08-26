"""
String helpers

@since 0.1.0
"""


def uc_first(text: str) -> str:
    """
    Make the first letter uppercase

    @since 0.1.0
    """
    return text[:1].upper() + text[1:]


def lc_first(text: str) -> str:
    """
    Make the first letter lowercase

    @since 0.1.0
    """
    return text[:1].lower() + text[1:]


def to_pascal(text: str) -> str:
    """
    Transform text to pascal case

    @since 0.1.0
    """
    return ''.join(x for x in text.title() if not x.isspace())


def to_camel(text: str) -> str:
    """
    Transform text to camel case

    @since 0.1.0
    """
    return lc_first(to_pascal(text))


def to_snake(text: str) -> str:
    """
    Transform text to snake case

    @since 0.1.0
    """
    return text.replace(' ', '_')


def to_kebab(text: str) -> str:
    """
    Transform text to kebab case

    @since 0.1.0
    """
    return text.replace(' ', '-')


def to_dot_case(text: str) -> str:
    """
    Transform text to dot case

    @since 0.1.0
    """
    return text.replace(' ', '.')
