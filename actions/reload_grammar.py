from loader import GrammarLoader


def reload_grammar() -> None:
    """
    Reload all grammar instances

    @since 0.1.0
    """
    loader = GrammarLoader.instance()
    loader.reload()
