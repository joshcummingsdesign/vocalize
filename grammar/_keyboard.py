from dragonfly import Grammar, MappingRule, Key, Function, IntegerRef


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
                '[<n>] whack': Key('backspace:%(n)d') + Function(lambda n: print(f'{n} backspace')),
                'scratch': Key('w-backspace') + Function(lambda: print('w-backspace')),
                'out': Key('escape') + Function(lambda: print('escape')),
            },
            extras=[
                IntegerRef('n', 1, 1000),
            ],
            defaults={
                'n': 1,
            }
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
