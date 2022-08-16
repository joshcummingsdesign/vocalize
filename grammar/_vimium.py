from dragonfly import Grammar, MappingRule, Key, Function, IntegerRef, AppContext


class Vimium:
    """
    The Vimium grammar class.

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance.

    @unreleased
    """

    def _make_vimium_rule(self) -> MappingRule:
        """
        Vimium rule factory.

        @unreleased
        """
        return MappingRule(
            name='vimium_rule',
            mapping={
                'book': Key('b') + Function(lambda: print('b')),
                'new book': Key('B') + Function(lambda: print('B')),
                'open': Key('o') + Function(lambda: print('o')),
                'open new': Key('O') + Function(lambda: print('O')),
                '[<n>] choose': Key('c-j:%(n)d') + Function(lambda n: print(f'{n}c-j')),
                '[<n>] back choose': Key('c-k:%(n)d') + Function(lambda n: print(f'{n}c-k')),
                'jump': Key('f') + Function(lambda: print('f')),
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
        Load the grammar.

        @unreleased
        """
        context = AppContext(executable='Google Chrome')
        self._grammar = Grammar('vimium', context=context)
        self._grammar.add_rule(self._make_vimium_rule())
        self._grammar.load()


vimium = Vimium()
vimium.load()
