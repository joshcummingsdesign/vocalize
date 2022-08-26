from loader import GrammarLoader


def load_grammar() -> None:
    """
    Load all grammar instances

    @since 0.1.0
    """
    loader = GrammarLoader.instance()
    loader.load()
