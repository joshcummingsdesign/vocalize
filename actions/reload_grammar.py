from loader import GrammarLoader


def reload_grammar() -> None:
    """
    Reload all grammar instances

    @unreleased
    """
    loader = GrammarLoader.instance()
    loader.reload()
