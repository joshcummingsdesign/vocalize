from dragonfly import Grammar, MappingRule, Key, Function


class Keyboard:
    """
    The keyboard grammar class.

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance.

    @unreleased
    """

    def _make_keyboard_rule(self) -> MappingRule:
        """
        Keyboard rule factory.

        @unreleased
        """
        return MappingRule(
            name='keyboard_rule',
            mapping={
                'go': Key('enter') + Function(lambda: print('enter')),
                'whack': Key('backspace') + Function(lambda: print('backspace')),
                'scratch': Key('w-backspace') + Function(lambda: print('w-backspace')),
                'out': Key('escape') + Function(lambda: print('escape')),
            },
        )

    def load(self) -> None:
        """
        Load the grammar.

        @unreleased
        """
        self._grammar = Grammar('keyboard')
        self._grammar.add_rule(self._make_keyboard_rule())
        self._grammar.load()


keyboard = Keyboard()
keyboard.load()
