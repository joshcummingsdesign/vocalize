from dragonfly import Grammar, MappingRule, Key, Function, IntegerRef, AppContext, Dictation, Text


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
                'book [<text>]': Key('b') + Text('%(text)s') + Function(lambda text: print(f'b {text}')),
                'book new [<text>]': Key('B') + Text('%(text)s') + Function(lambda text: print(f'B {text}')),
                'open [<text>]': Key('o') + Text('%(text)s') + Function(lambda text: print(f'o {text}')),
                'open new [<text>]': Key('O') + Text('%(text)s') + Function(lambda text: print(f'O {text}')),
                '[<n>] you': Key('u:%(n)d') + Function(lambda n: print(f'{n}u')),
                '[<n>] dee': Key('d:%(n)d') + Function(lambda n: print(f'{n}d')),
                'jump': Key('f') + Function(lambda: print('f')),
                'close window': Key('x') + Function(lambda: print('x')),
                'switch user': Key('ws-m') + Function(lambda: print('ws-m')),
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
        Load the grammar.

        @unreleased
        """
        context = AppContext(executable='Google Chrome')
        self._grammar = Grammar('vimium', context=context)
        self._grammar.add_rule(self._make_vimium_rule())
        self._grammar.load()


vimium = Vimium()
vimium.load()
