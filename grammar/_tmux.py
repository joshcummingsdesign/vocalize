from dragonfly import Grammar, MappingRule, Key, Function, Text, Dictation, IntegerRef

from actions import repeatable


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

    def _term_win_left(self) -> None:
        """
        Change terminal window left.

        @unreleased
        """
        Key('c-k,h').execute()
        print(f'c-k h')

    def _term_win_right(self) -> None:
        """
        Change terminal window right.

        @unreleased
        """
        Key('c-k,l').execute()
        print(f'c-k l')

    def _make_tmux_rule(self) -> MappingRule:
        """
        Tmux rule factory.

        @unreleased
        """
        return MappingRule(
            name='tmux_rule',
            mapping={
                'yup': Key('c-r') + Function(lambda: print('c-r')),
                'clear': Key('c-l') + Function(lambda: print('c-l')),
                'new term': Key('c-k,c') + Function(lambda: print('c-k c')),
                'exit': Key('c-d') + Function(lambda: print('c-d')),
                'abort': Key('c-c') + Function(lambda: print('c-c')),
                'split': Key('c-k,v') + Function(lambda: print('c-k v')),
                'rename term [<text>]': Key('c-k,r') + Text('%(text)s') + Key('enter') + Function(lambda text: print(f'c-k r {text} enter')),
                'switch term <n>': Key('c-k,%(n)d') + Function(lambda n: print(f'c-k{n}')),
                '[<n>] term win left': Function(lambda n: repeatable(n, self._term_win_left)),
                '[<n>] term win right': Function(lambda n: repeatable(n, self._term_win_right)),
                'term win even': Key('c-k,enter') + Function(lambda: print('c-k enter')),
                'git add all': Text('gaa') + Key('enter') + Function(lambda: print('gaa enter')),
                'git commit': Text('gca') + Key('enter') + Function(lambda: print('gca enter')),
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
        self._grammar = Grammar('tmux')
        self._grammar.add_rule(self._make_tmux_rule())
        self._grammar.load()


tmux = Tmux()
tmux.load()
