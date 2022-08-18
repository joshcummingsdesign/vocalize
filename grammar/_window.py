from dragonfly import Grammar, MappingRule, Key, Dictation, Text, IntegerRef


class Window:
    """
    The window grammar class

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance

    @unreleased
    """

    def _make_window_rule(self) -> MappingRule:
        """
        Window rule factory

        @unreleased
        """
        return MappingRule(
            name='window_rule',
            mapping={
                'kill': Key('w-q'),
                'close window': Key('w-w'),
                'new window': Key('w-n'),
                'new big window': Key('ws-n'),
                'new tab': Key('w-t'),
                'reopen': Key('ws-t'),
                'hide': Key('w-h'),
                'spotlight [<text>]': Key('c-space') + Text('%(text)s'),
                '[<n>] swap': Key('win:down,tab:%(n)d,win:up'),
                '[<n>] switch': Key('w-`:%(n)d'),
            },
            extras=[
                IntegerRef('n', 1, 10),
                Dictation('text'),
            ],
            defaults={
                'n': 1,
                'text': '',
            }
        )

    def load(self) -> None:
        """
        Load the grammar

        @unreleased
        """
        self._grammar = Grammar('window')
        self._grammar.add_rule(self._make_window_rule())
        self._grammar.load()


window = Window()
window.load()
