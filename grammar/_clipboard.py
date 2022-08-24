from dragonfly import Grammar, MappingRule, Key, IntegerRef


class Clipboard:
    """
    The clipboard grammar class

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance

    @unreleased
    """

    def _make_clipboard_rule(self) -> MappingRule:
        """
        Clipboard rule factory

        @unreleased
        """
        return MappingRule(
            name='clipboard_rule',
            mapping={
                'clip': Key('ws-space'),
                'clip <i>': Key('w-%(i)d'),
            },
            extras=[
                IntegerRef('i', 0, 9),
            ]
        )

    def load(self) -> None:
        """
        Load the grammar

        @unreleased
        """
        self._grammar = Grammar('clipboard')
        self._grammar.add_rule(self._make_clipboard_rule())
        self._grammar.load()


clipboard = Clipboard()
clipboard.load()
