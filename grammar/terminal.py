from actions import repeat_key, enter_optional_text
from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Key, Text, Function, IntegerRef, Dictation
from extras import character


class Grammar(BaseGrammar):
    """
    Terminal grammar

    @since 0.1.0
    """

    @property
    def _name(self) -> str:
        return 'terminal'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_terminal_rule,
        ]

    def _make_terminal_rule(self) -> Rule:
        """
        Terminal rule factory

        @since 0.1.0
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
                'term list': Key('t,l,enter'),
                'term attach <char>': Text('ta %(char)s') + Key('enter'),
                'term detach': Key('c-k,d'),
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
                'open it': Text('open .') + Key('enter'),

                # Vim
                'vim [<text>]': Text('vim %(text)s'),
                'vim it': Text('vim .') + Key('enter'),
                'vim [<text>]': Text('vim %(text)s'),
                'vim it': Text('vim .') + Key('enter'),

                # VS Code
                'code it': Text('code .') + Key('enter'),

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
                'git check out [<text>]': Text('gco ') + Function(enter_optional_text),
                'git reset hard [<text>]': Text('git reset --hard origin/%(text)s'),
                'git stash': Text('git stash') + Key('enter'),
                'git drop': Text('git stash drop') + Key('enter'),
                'git apply': Text('git stash apply') + Key('enter'),
                'git stash and drop': Text('git stash && git stash drop') + Key('enter'),
                'git base <text>': Text('git rebase %(text)s'),
                'git force push': Text('gp -f'),
                'git force push origin <text>': Text('gp -u -f origin %(text)s'),

                # Lando
                'lando start': Text('lando start') + Key('enter'),
                'lando stop': Text('lando stop') + Key('enter'),
            },
            extras=[
                IntegerRef('n', 1, 10),
                Dictation('text'),
                character('char'),
            ],
            defaults={
                'n': 1,
                'text': '',
            }
        )
