from dragonfly import Grammar, MappingRule, Key, Text, Function, IntegerRef, Dictation
from actions import repeat_key


class Terminal:
    """
    The terminal grammar class

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance

    @unreleased
    """

    def _make_terminal_rule(self) -> MappingRule:
        """
        Terminal rule factory

        @unreleased
        """
        return MappingRule(
            name='terminal_rule',
            mapping={
                # Window
                'term': Key('w-space'),
                'new term': Key('c-k,c'),
                'term name <text>': Key('c-k,r') + Text('%(text)s') + Key('enter'),
                'switch term <n>': Key('c-k,%(n)d'),
                'split': Key('c-k,v'),
                '[<n>] term win left': Function(lambda n: repeat_key(n, 'c-k,h')),
                '[<n>] term win right': Function(lambda n: repeat_key(n, 'c-k,l')),
                'term win even': Key('c-k,enter'),
                'exit': Key('c-d'),
                'abort': Key('c-c'),

                # Navigation
                'see dee [<text>]': Text('cd %(text)s'),
                'see dee back': Text('cd ..') + Key('enter'),
                'list': Key('l,enter'),
                'guess': Key('tab'),
                'yup': Key('c-r'),
                'clear': Key('c-l'),
                'free': Key('c-k,escape'),

                # Vim
                'vim [<text>]': Text('vim %(text)s'),
                'vim it': Text('vim .') + Key('enter'),

                # Git
                'git add all': Text('gaa') + Key('enter'),
                'git commit': Text('gca') + Key('enter'),
                'git push': Text('gp') + Key('enter'),
                'git status': Text('gst') + Key('enter'),
                'git diff': Text('git diff') + Key('enter'),
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
        Load the grammar

        @unreleased
        """
        self._grammar = Grammar('terminal')
        self._grammar.add_rule(self._make_terminal_rule())
        self._grammar.load()


terminal = Terminal()
terminal.load()