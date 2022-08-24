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
                'term <n>': Key('c-k,%(n)d'),
                'term hide': Key('w-space/20:2'),
                'term new': Key('c-k,c'),
                'term name <text>': Key('c-k,r') + Text('%(text)s') + Key('enter'),
                'term switch <n>': Key('c-k,%(n)d'),
                'term split': Key('c-k,v'),
                '[<n>] term win left': Function(lambda n: repeat_key(n, 'c-k,h')),
                '[<n>] term win right': Function(lambda n: repeat_key(n, 'c-k,l')),
                'term win even': Key('c-k,enter'),
                'exit': Key('c-d'),
                'abort': Key('c-c'),

                # Navigation
                'see dee [<text>]': Text('cd %(text)s'),
                '[<n>] see dee back': Text('cd ') + Function(lambda n: repeat_key(n, '.,.,slash')) + Key('enter'),
                'list': Key('l,enter'),
                'cat [<text>]': Text('cat %(text)s'),
                'yup': Key('c-r'),
                'clear': Key('c-l'),
                'free': Key('c-k,escape'),

                # Vim
                'vim [<text>]': Text('vim %(text)s'),
                'vim it': Text('vim .') + Key('enter'),
                'vim [<text>]': Text('vim %(text)s'),
                'vim it': Text('vim .') + Key('enter'),

                # VS Code
                'code it': Text('code .'),

                # PHPStorm
                'storm it': Text('phpstorm .'),

                # Git
                'git add all': Text('gaa') + Key('enter'),
                'git commit': Text('gca') + Key('enter'),
                'git push': Text('gp') + Key('enter'),
                'git pull': Text('gl') + Key('enter'),
                'git status': Text('gst') + Key('enter'),
                'git diff [<text>]': Text('git diff %(text)s') + Key('enter'),
                'git new branch': Text('gco -b '),
                'git branch': Text('gb') + Key('enter'),
                'git branch delete': Text('gb --delete '),
                'git tag': Text('git tag -a '),
                'git message': Text(" -m ''") + Key('left'),
                'git push tags': Text('gp --tags') + Key('enter'),
                'git tag delete': Text('git tag --delete '),
                'git tag delete origin': Text('git push origin :'),
                'git merge <text>': Text('git merge %(text)s'),
                'git fetch all': Text('gfa') + Key('enter'),
                'git push origin': Text('gp -u origin '),
                'git check out [<text>]': Text('gco %(text)s'),
                'git reset hard [<text>]': Text('git reset --hard origin/%(text)s'),
                'git stash': Text('git stash') + Key('enter'),
                'git drop': Text('git stash drop') + Key('enter'),
                'git apply': Text('git stash apply') + Key('enter'),
                'git stash and drop': Text('git stash && git stash drop') + Key('enter'),
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
