from dragonfly import Grammar, MappingRule, Key, IntegerRef


class WindowManager:
    """
    The window manager grammar class

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance

    @unreleased
    """

    def _make_window_manager_rule(self) -> MappingRule:
        """
        Window manager rule factory

        @unreleased
        """
        return MappingRule(
            name='window_manager_rule',
            mapping={
                'tile main': Key('as-enter'),
                '[<n>] tile up': Key('as-k/20:%(n)d'),
                '[<n>] tile down': Key('as-j/20:%(n)d'),
                '[<n>] tile left': Key('as-h/20:%(n)d'),
                '[<n>] tile right': Key('as-l/20:%(n)d'),
                'tile hop': Key('cas-h'),
                'tile swap': Key('cas-l'),
                'tile flip': Key('cas-k'),
                'tile flop': Key('cas-j'),
            },
            extras=[
                IntegerRef('n', 1, 10),
            ],
            defaults={
                'n': 1,
            }
        )

    def load(self) -> None:
        """
        Load the grammar

        @unreleased
        """
        self._grammar = Grammar('window_manager')
        self._grammar.add_rule(self._make_window_manager_rule())
        self._grammar.load()


window_manager = WindowManager()
window_manager.load()
