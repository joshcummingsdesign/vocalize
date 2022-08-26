from loader import GrammarLoader


def load_grammar() -> None:
    """
    Load all grammar instances

    @unreleased
    """
    loader = GrammarLoader.instance()
    loader.load()
