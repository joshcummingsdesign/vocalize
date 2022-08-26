from loader import GrammarLoader


def load_grammar() -> None:
    """
    Load all grammars in the `grammar` directory

    @unreleased
    """
    loader = GrammarLoader.instance()
    loader.load()
