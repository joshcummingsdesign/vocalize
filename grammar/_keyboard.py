from dragonfly import Grammar, MappingRule, Key, Function, IntegerRef, Text, Dictation
from extras import modifiers
from rules import SeriesMappingRule


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
                'type in <text>': Text('%(text)s') + Function(lambda text: print(text)),
                '[<n>] press <mod>': Key('%(mod)s:%(n)d') + Function(lambda n, mod: print(f'{n}{mod}')),
                'highlight': Key('w-a') + Function(lambda: print('w-a')),
            },
            extras=[
                IntegerRef('n', 1, 1000),
                Dictation('text'),
                modifiers('mod'),
            ],
            defaults={
                'n': 1,
            }
        )

    def _make_series_keyboard_rule(self) -> SeriesMappingRule:
        """
        Series keyboard rule factory.

        @unreleased
        """
        return SeriesMappingRule(
            name='series_keyboard_rule',
            mapping={
                'alpha': Key('a') + Function(lambda: print('a')),
                'bravo': Key('b') + Function(lambda: print('b')),
                'charlie': Key('c') + Function(lambda: print('c')),
                'delta': Key('d') + Function(lambda: print('d')),
                'echo': Key('e') + Function(lambda: print('e')),
                'foxtrot': Key('f') + Function(lambda: print('f')),
                'golf': Key('g') + Function(lambda: print('g')),
                'hotel': Key('h') + Function(lambda: print('h')),
                'india': Key('i') + Function(lambda: print('i')),
                'juliet': Key('j') + Function(lambda: print('j')),
                'kilo': Key('k') + Function(lambda: print('k')),
                'lima': Key('l') + Function(lambda: print('l')),
                'mike': Key('m') + Function(lambda: print('m')),
                'november': Key('n') + Function(lambda: print('n')),
                'oscar': Key('o') + Function(lambda: print('o')),
                'papa': Key('p') + Function(lambda: print('p')),
                'quebec': Key('q') + Function(lambda: print('q')),
                'romeo': Key('r') + Function(lambda: print('r')),
                'sierra': Key('s') + Function(lambda: print('s')),
                'tango': Key('t') + Function(lambda: print('t')),
                'uniform': Key('u') + Function(lambda: print('u')),
                'victor': Key('v') + Function(lambda: print('v')),
                'whiskey': Key('w') + Function(lambda: print('w')),
                'x ray': Key('x') + Function(lambda: print('x')),
                'yankee': Key('y') + Function(lambda: print('y')),
                'zulu': Key('z') + Function(lambda: print('z')),
            }
        )

    def load(self) -> None:
        """
        Load the grammar.

        @unreleased
        """
        self._grammar = Grammar('keyboard')
        self._grammar.add_rule(self._make_keyboard_rule())
        self._grammar.add_rule(self._make_series_keyboard_rule())
        self._grammar.load()


keyboard = Keyboard()
keyboard.load()
