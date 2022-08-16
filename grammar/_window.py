from dragonfly import Grammar, MappingRule, Key, Function, Dictation, Text, IntegerRef


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
                'new tab': Key('w-t') + Function(lambda: print('w-t')),
                'reopen': Key('ws-t') + Function(lambda: print('ws-t')),
                '[<n>] swap': Key('win:down,tab:%(n)d,win:up') + Function(lambda n: print(f'{n}w-tab')),
                '[<n>] switch': Key('w-`:%(n)d') + Function(lambda n: print(f'{n}w-`')),
                'spotlight [<text>]': Key('c-space') + Text('%(text)s') + Function(lambda text: print(f'spotlight {text}')),
                'kill': Key('w-q') + Function(lambda: print('w-q')),
                'vault': Key('wa-backslash') + Function(lambda: print('wa-\\')),
                'term': Key('w-space') + Function(lambda: print('w-space')),
                'close window': Key('w-w') + Function(lambda: print('w-w')),
                'new window': Key('w-n') + Function(lambda: print('w-n')),
                'new big window': Key('ws-n') + Function(lambda: print('ws-n')),
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
        self._grammar = Grammar('window')
        self._grammar.add_rule(self._make_window_rule())
        self._grammar.load()


window = Window()
window.load()
