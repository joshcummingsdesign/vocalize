from dragonfly import Grammar, MappingRule, Key, IntegerRef, ShortIntegerRef, Text, Function, Dictation
from extras import character
from rules import SeriesMappingRule


class Vim:
    """
    The Vim grammar class

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance

    @unreleased
    """

    def _make_vim_series_rule(self) -> SeriesMappingRule:
        """
        The Vim series rule factory

        @unreleased
        """
        return SeriesMappingRule(
            name='vim_series_rule',
            mapping={
                # Operators
                'select': Key('escape,v'),
                'select [<n>] (line | lines)': Key('escape') + Function(lambda n: Text(f'V,{n - 1}j', True).execute()),
                'change': Key('c'),
                'big change': Key('C'),
                'delete': Key('d'),
                'delete [<n>] (line | lines)': Function(lambda n: Text(f'{n}dd', True).execute()),
                'yank': Key('y'),
                'yank [<n>] (line | lines)': Function(lambda n: Text(f'{n}yy', True).execute()),
                '[<n>] paste': Key('p:%(n)d'),
                '[<n>] back paste': Key('P:%(n)d'),
                '[<n>] repeat': Key('.:%(n)d'),

                # Motions
                '[<n>] left': Function(lambda n: Text(f'{n}h', True).execute()),
                '[<n>] right': Function(lambda n: Text(f'{n}l', True).execute()),
                '[<n>] up': Function(lambda n: Text(f'{n}k', True).execute()),
                '[<n>] down': Function(lambda n: Text(f'{n}j', True).execute()),
                '[<n>] ascend': Function(lambda n: Text(f'{n}-', True).execute()),
                '[<n>] descend': Function(lambda n: Text(f'{n}+', True).execute()),
                '[<n>] find <char>': Function(lambda n, char: Text(f'{n}f{char}', True).execute()),
                '[<n>] back find <char>': Function(lambda n, char: Text(f'{n}F{char}', True).execute()),
                '[<n>] till <char>': Function(lambda n, char: Text(f'{n}t{char}', True).execute()),
                '[<n>] back till <char>': Function(lambda n, char: Text(f'{n}T{char}', True).execute()),
                'top': Key('g,g'),
                'bottom': Key('G'),
                'snap': Text('^'),
                'start': Key('0'),
                'end': Key('$'),
                'matching': Key('percent'),

                # Text Objects
                'inner': Key('i'),
                'around': Key('a'),
                'word': Key('w'),
                'big word': Key('W'),
                'back': Key('b'),
                'big back': Key('B'),
            },
            extras=[
                IntegerRef('n', 1, 1000),
                character('char'),
            ],
            defaults={
                'n': 1,
            }
        )

    def _make_vim_rule(self) -> MappingRule:
        """
        The Vim rule factory

        @unreleased
        """
        return MappingRule(
            name='vim_rule',
            mapping={
                # Modes
                'insert': Key('escape,i'),
                'block': Key('escape,c-v'),

                # Editing
                '[<n>] undo': Key('escape') + Function(lambda n: Text(f'{n}u', True).execute()),
                '[<n>] redo': Key('escape') + Function(lambda n: Text(n, True).execute()) + Key('c-r'),
                'wipe': Key('escape,d,d'),
                '[<n>] slice': Function(lambda n: Text(f'{n}x', True).execute()),
                '[<n>] splice': Function(lambda n: Text(f'{n}X', True).execute()),
                '[<n>] bump': Function(lambda n: Text(f'{n}o', True).execute()),
                '[<n>] nudge': Function(lambda n: Text(f'{n}O', True).execute()),
                'clip yank': Key('",*,y'),
                'clip paste': Key('",*,p'),
                'after': Key('escape,A'),
                'before': Key('escape,I'),
                '[<n>] sit': Function(lambda n: Text(f'{n}*', True).execute()),
                'spock': Key('i,space,escape'),
                '[<n>] lent': Function(lambda n: Text(f'{n}<', True).execute()),
                '[<n>] rent': Function(lambda n: Text(f'{n}<', True).execute()),
                'sent': Text(':left') + Key('enter'),
                'replace <char>': Key('r,%(char)s'),
                'go upper': Key('g,U'),
                'go lower': Key('g,u'),
                'wrap': Key('g,q'),
                'define': Key('g,d'),

                # File
                'save': Key('colon,w,enter'),
                'quit': Key('colon,q,enter'),
                'write out': Key('colon,w,q,enter'),
                'bail': Key('colon,q,!,enter'),
                'buff': Key('space,b,p'),
                'next buff': Key('space,b,n'),
                'fuzzy [<text>]': Key('c-p') + Text('%(text)s'),
                'tree': Key('c-backslash'),
                '[<n>] choose': Key('c-j:%(n)d'),
                '[<n>] back choose': Key('c-k:%(n)d'),

                # Navigation
                'line <line>': Key('escape') + Text(':%(line)d') + Key('enter'),
                '[<n>] search [<object>] [<text>] [<char>]': Text('%(n)d/%(object)s%(text)s%(char)s') + Key('enter'),
                '[<n>] back search [<object>] [<text>] [<char>]': Text('%(n)d?%(object)s%(text)s%(char)s') + Key('enter'),
                '[<n>] next': Function(lambda n: Text(f'{n}n', True).execute()),
                '[<n>] previous': Function(lambda n: Text(f'{n}N', True).execute()),
                '[<n>] pup': Function(lambda n: Text(f'{n}', True).execute()) + Key('c-u'),
                '[<n>] page': Function(lambda n: Text(f'{n}', True).execute()) + Key('c-d'),
                'zed zed': Key('escape,z,z'),
                'zed top': Key('escape,z,t'),
                'zed bottom': Key('escape,z,b'),
                'run in': Key('escape,c-i'),
                'run out': Key('escape,c-o'),

                # Surround
                'select inner <char>': Key('escape,v,i,%(char)s'),
                'select around <char>': Key('escape,v,a,%(char)s'),
                'change inner <char>': Key('escape,c,i,%(char)s'),
                'change around <char>': Key('escape,c,a,%(char)s'),
                'delete inner <char>': Key('escape,d,i,%(char)s'),
                'delete around <char>': Key('escape,d,a,%(char)s'),
                'yank inner <char>': Key('escape,y,i,%(char)s'),
                'yank around <char>': Key('escape,y,a,%(char)s'),
                'surround [with] <char>': Key('S,%(char)s'),
                'surround inner <object> [with] <char>': Key('escape,y,s,i,%(object)s,%(char)s'),
                'surround around <object> [with] <char>': Key('escape,y,s,a,%(object)s,%(char)s'),
                'surround [inner] [word] [with] <char>': Key('escape,y,s,i,w,%(char)s'),
                'surround [inner] big word [with] <char>': Key('escape,y,s,i,W,%(char)s'),
                'surround line [with] <char>': Key('escape,y,s,s,%(char)s'),
                'change surrounding <object> [to] <char>': Key('escape,c,s,%(object)s,%(char)s'),
                'delete surrounding <char>': Key('escape,d,s,%(char)s'),

                # Abolish
                'go snake': Key('escape,c,r,s'),
                'go camel': Key('escape,c,r,c'),
                'go pascal': Key('escape,c,r,m'),
                'go kebab': Key('escape,c,r,minus'),
                'go dot case': Key('escape,c,r,.'),
                'go upper snake': Key('escape,c,r,u'),
                'go space case': Key('escape,c,r,space'),
                'go title': Key('escape,c,r,t'),

                # Commentary
                'comment': Key('escape,g,c'),
                'comment [<n>] (line | lines)': Key('escape') + Function(lambda n: Text(f'{n}gcc', True).execute()),
            },
            extras=[
                IntegerRef('n', 1, 1000),
                ShortIntegerRef('line', 1, 10000),
                Dictation('text'),
                character('char'),
                character('object'),
            ],
            defaults={
                'n': 1,
                'text': '',
                'char': '',
                'object': '',
            }
        )

    def load(self) -> None:
        """
        Load the grammar

        @unreleased
        """
        self._grammar = Grammar('vim')
        self._grammar.add_rule(self._make_vim_series_rule())
        self._grammar.add_rule(self._make_vim_rule())
        self._grammar.load()


vim = Vim()
vim.load()
