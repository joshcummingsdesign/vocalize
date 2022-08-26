from loader import GrammarLoader


def reload_grammar() -> None:
    """
    Reload all grammars in the `grammar` directory

    @unreleased
    """
    loader = GrammarLoader.instance()
    loader.reload()
