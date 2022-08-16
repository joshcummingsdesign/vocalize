from dragonfly import Grammar, MappingRule, Key, Function


class Window:
    """
    The window grammar class.

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance.

    @unreleased
    """

    def _make_window_rule(self) -> MappingRule:
        """
        Window rule factory.

        @unreleased
        """
        return MappingRule(
            name='window_rule',
            mapping={
                'reopen': Key('ws-t') + Function(lambda: print('ws-t')),
            },
        )

    def load(self) -> None:
        """
        Load the grammar.

        @unreleased
        """
        self._grammar = Grammar('window')
        self._grammar.add_rule(self._make_window_rule())
        self._grammar.load()


window = Window()
window.load()
