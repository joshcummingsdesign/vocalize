from dragonfly import Grammar, MappingRule, Key, Function


class Tmux:
    """
    The Tmux grammar class.

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance.

    @unreleased
    """

    def _make_tmux_rule(self) -> MappingRule:
        """
        Tmux rule factory.

        @unreleased
        """
        return MappingRule(
            name='tmux_rule',
            mapping={
                'yup': Key('c-r') + Function(lambda: print('c-r')),
            }
        )

    def load(self) -> None:
        """
        Load the grammar.

        @unreleased
        """
        self._grammar = Grammar('tmux')
        self._grammar.add_rule(self._make_tmux_rule())
        self._grammar.load()


tmux = Tmux()
tmux.load()
