from actions import repeat_key, enter_optional_text
from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Key, Text, Function, IntegerRef, Dictation
from extras import character
from rules import SeriesMappingRule


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
            self._make_terminal_series_rule,
            self._make_terminal_rule,
        ]

    def _make_terminal_series_rule(self) -> Rule:
        """
        Terminal series rule factory

        @since 0.2.0
        """
        return SeriesMappingRule(
            name='terminal_series_rule',
            mapping={
                # Navigation
                'cd desktop': Text('cd ~/Desktop') + Key('enter'),
                'cd downloads': Text('cd ~/Downloads') + Key('enter'),
                'cd projects': Text('cd ~/Projects/'),
                'cd contribute': Text('cd ~/Contrib/'),
                'cd [<text>]': Text('cd %(text)s'),
                '[<n>] der back': Text('cd ') + Function(lambda n: repeat_key(n, '.,.,slash')) + Key('enter'),
                'home': Text('~/'),
                'list': Text('ls -lah') + Key('enter'),
                'yup': Key('c-r'),
                'clear': Key('c-l'),
                'free': Key('c-k,escape'),

                # Editing
                'remove [<text>]': Text('rm -rf %(text)s'),
                'cp [<text>]': Text('cp -R %(text)s'),
                'make der [<text>]': Text('mkdir ') + Function(enter_optional_text),
                'into it': Text('$_'),
                'try again': Key('escape,k'),

                # SSH
                'swish': Text('ssh '),
                'sync': Text('rsync -aziP '),

                # Notes
                'notes': Text('vim ~/Documents/scratch.md') + Key('enter'),

                # Node
                'node run [<text>]': Text('npm run %(text)s'),
                'node install': Text('npm install') + Key('enter'),
                'node version': Text('node --version') + Key('enter'),

                # Python
                'python version': Text('python --version') + Key('enter'),
                'python virtual': Text('python -m venv venv'),
                'activate': Text('source venv/bin/activate') + Key('enter'),
                'deactivate': Text('deactivate') + Key('enter'),

                # File extensions
                'dot js': Text('.js'),
                'dot pie': Text('.py'),
                'dot html': Text('.html'),

                # Ruby
                'ruby version': Text('ruby --version') + Key('enter'),

                # Miniconda
                'con list': Text('conda env list') + Key('enter'),
                'con activate [<text>]': Text('conda activate %(text)s'),
                'con deactivate': Text('conda deactivate') + Key('enter'),

                # Vim
                'vim [<text>]': Text('vim %(text)s'),
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

    def _make_terminal_rule(self) -> Rule:
        """
        Terminal rule factory

        @since 0.1.0
        """
        return MappingRule(
            name='terminal_rule',
            mapping={
                # Window
                'term': Key('ws-space'),
                'term <n>': Key('c-k,%(n)d'),
                'term new': Key('c-k,c'),
                'term name <text>': Key('c-k,r') + Text('%(text)s') + Key('enter'),
                'term split': Key('c-k,v'),
                'term list': Key('t,l,enter'),
                'term attach <char>': Text('ta %(char)s') + Key('enter'),
                'term detach': Key('c-k,d'),
                '[<n>] term left': Function(lambda n: repeat_key(n, 'c-k,h')),
                '[<n>] term right': Function(lambda n: repeat_key(n, 'c-k,l')),
                'term even': Key('c-k,enter'),
                'exit': Key('c-d'),
                'abort': Key('c-c'),

                # Navigation
                'print [<text>]': Text('cat %(text)s'),
                'open it': Text('open .') + Key('enter'),

                # Vim
                'vim it': Text('vim .') + Key('enter'),

                # VS Code
                'code it': Text('code .') + Key('enter'),

                # Git
                'git add all': Text('gaa') + Key('enter'),
                'git commit': Text('gca') + Key('enter'),
                'git commit message': Text("gcam ''") + Key('left'),
                'git push': Text('gp') + Key('enter'),
                'git pull': Text('gl') + Key('enter'),
                'git status': Text('gst') + Key('enter'),
                'git log': Text('glg') + Key('enter'),
                'git diff [<text>]': Text('git diff %(text)s') + Key('enter'),
                'git check out branch': Text('gco -b '),
                'git branch': Text('gb') + Key('enter'),
                'git branch delete': Text('gb --delete '),
                'git tag': Text('git tag -a '),
                'git message': Text(" -m ''") + Key('left'),
                'git push tags': Text('gp --tags') + Key('enter'),
                'git tag delete': Text('git tag --delete '),
                'git tag delete origin': Text('git push origin :'),
                'git merge <text>': Text('git merge %(text)s'),
                'git fetch all': Text('gfa') + Key('enter'),
                'git push upstream': Text('gp -u origin '),
                'git check out [<text>]': Text('gco ') + Function(enter_optional_text),
                'git reset [<text>]': Text('git reset --hard origin/%(text)s'),
                'git stash': Text('git stash') + Key('enter'),
                'git stash drop': Text('git stash drop') + Key('enter'),
                'git stash apply': Text('git stash apply') + Key('enter'),
                'git base [<text>]': Text('git rebase %(text)s'),
                'git base continue': Text('git rebase --continue'),
                'git eye base': Text('git rebase -i '),
                'git force push': Text('gp -f'),
                'git force push origin <text>': Text('gp -u -f origin %(text)s'),
                'git abort merge': Text('git merge --abort') + Key('enter'),
                'git add origin': Text('git remote add origin '),
                'git clone': Text('git clone '),

                # Lando
                'lando start': Text('lando start') + Key('enter'),
                'lando stop': Text('lando stop') + Key('enter'),
                'lando [<text>]': Text('lando %(text)s'),

                # Docker
                'dock running': Text('docker ps') + Key('enter'),
                'dock volume list': Text('docker volume ls') + Key('enter'),
                'dock network list': Text('docker network ls') + Key('enter'),
                'dock kill': Text('docker stop $(docker ps -a)') + Key('enter'),

                # asdf
                'machine list all': Text('asdf list') + Key('enter'),
                'machine list node': Text('asdf list nodejs') + Key('enter'),
                'machine list [<text>]': Text('asdf list ') + Function(enter_optional_text),
                'machine install [<text>]': Text('asdf install %(text)s '),
                'machine uninstall node': Text('asdf uninstall nodejs '),
                'machine uninstall [<text>]': Text('asdf uninstall %(text)s '),
                'machine global [<text>]': Text('asdf global %(text)s '),
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
