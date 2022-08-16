from dragonfly import Grammar, MappingRule, Key, Function, Dictation, Text, IntegerRef
from extras import characters
from actions import repeatable


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
                'tile main': Key('as-enter') + Function(lambda: print('as-enter')),
                '[<n>] tile up': Key('as-k/20:%(n)d') + Function(lambda n: print(f'{n}as-k')),
                '[<n>] tile down': Key('as-j/20:%(n)d') + Function(lambda n: print(f'{n}as-j')),
                '[<n>] tile left': Key('as-h/20:%(n)d') + Function(lambda n: print(f'{n}as-h')),
                '[<n>] tile right': Key('as-l/20:%(n)d') + Function(lambda n: print(f'{n}as-l')),
                'tile hop': Key('cas-h') + Function(lambda: print('cas-h')),
                'tile swap': Key('cas-l') + Function(lambda: print('cas-l')),
                'tile flip': Key('cas-k') + Function(lambda: print('cas-k')),
                'tile flop': Key('cas-j') + Function(lambda: print('cas-j')),
                'see dee': Key('c,d,space') + Function(lambda: print('cd space')),
                'see dee back': Key('c,d,space,dot,dot,enter') + Function(lambda: print('cd ..')),
                'list': Key('l,enter') + Function(lambda: print('l enter')),
                'vim it': Key('v,i,m,space,dot,enter') + Function(lambda: print('vim . enter')),
                'vim': Key('v,i,m,space') + Function(lambda: print('vim space')),
            },
            extras=[
                IntegerRef('n', 1, 10),
                Dictation('text'),
                characters('char'),
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
