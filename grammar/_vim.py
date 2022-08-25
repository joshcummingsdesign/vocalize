from actions import enter_optional_text
from contracts import Grammar
from contracts.rules import Rule, RuleFactory
from dragonfly import MappingRule, Key, IntegerRef, ShortIntegerRef, Text, Function, Dictation
from extras import character
from rules import SeriesMappingRule


class Vim(Grammar):
    """
    Vim grammar

    @unreleased
    """

    @property
    def _name(self) -> str:
        return 'vim'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_vim_series_rule,
            self._make_vim_rule,
        ]

    def _make_vim_series_rule(self) -> Rule:
        """
        Vim series rule factory

        @unreleased
        """
        return SeriesMappingRule(
            name='vim_series_rule',
            mapping={
                # Operators
                'select': Key('escape,v'),
                'change': Key('c'),
                'delete': Key('d'),
                'yank': Key('y'),

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
                'head': Key('g,g'),
                'foot': Key('G'),
                'snap': Text('^'),
                'start': Key('0'),
                'end': Key('$'),
                'match': Key('percent'),

                # Text Objects
                'inner': Key('i'),
                'around': Key('a'),
                'word': Key('w'),
                'big word': Key('W'),
                'back': Key('b'),
                'big back': Key('B'),
                'paragraph': Key('p'),

                # Editing
                'select [<n>] (line | lines)': Key('escape,V') + Function(lambda n: Text(f'{n - 1}j', True).execute() if n > 1 else False),
                'wipe': Key('escape,d,d'),
                'delete [<n>] (line | lines)': Function(lambda n: Text(f'{n}dd', True).execute()),
                'yank [<n>] (line | lines)': Function(lambda n: Text(f'{n}yy', True).execute()),
                '[<n>] paste': Key('p:%(n)d'),
                '[<n>] back paste': Key('P:%(n)d'),
                '[<n>] pete': Key('.:%(n)d'),
                '[<n>] (scratch | undo)': Key('escape') + Function(lambda n: Text(f'{n}u', True).execute()),
                '[<n>] redo': Key('escape') + Function(lambda n: Text(f'{n}', True).execute()) + Key('c-r'),
                '[<n>] slice': Function(lambda n: Text(f'{n}x', True).execute()),
                '[<n>] splice': Function(lambda n: Text(f'{n}X', True).execute()),
                '[<n>] bump': Function(lambda n: Text(f'{n}o', True).execute()),
                '[<n>] nudge': Function(lambda n: Text(f'{n}O', True).execute()),
                '[<n>] sit': Function(lambda n: Text(f'{n}*', True).execute()),

                # Navigation
                'line <line>': Key('escape') + Text(':%(line)d') + Key('enter'),
                '[<n>] next': Function(lambda n: Text(f'{n}n', True).execute()),
                '[<n>] previous': Function(lambda n: Text(f'{n}N', True).execute()),

                # File
                'buff': Key('escape,space,b,p'),
                'next buff': Key('escape,space,b,n'),
                '[<n>] choose': Key('c-j:%(n)d'),
                '[<n>] back choose': Key('c-k:%(n)d'),
            },
            extras=[
                IntegerRef('n', 1, 1000),
                ShortIntegerRef('line', 1, 10000),
                character('char'),
            ],
            defaults={
                'n': 1,
            }
        )

    def _make_vim_rule(self) -> Rule:
        """
        Vim rule factory

        @unreleased
        """
        return MappingRule(
            name='vim_rule',
            mapping={
                # Modes
                'insert': Key('escape,l,i'),
                'blip': Key('escape,i'),
                'block': Key('escape,c-v'),

                # Editing
                'big change': Key('C'),
                'delete line <line>': Function(lambda line: Text(f':{line}d', True).execute()) + Key('enter'),
                'delete line <line> from <l>': Function(lambda line, l: Text(f':{l},{line}d', True).execute()) + Key('enter,c-o'),
                'move line <line> from <l>': Function(lambda line, l: Text(f':{l},{line}m.', True).execute()) + Key('enter'),
                'yank line <line>': Function(lambda line: Text(f':{line}y', True).execute()) + Key('enter'),
                'yank line <line> from <l>': Function(lambda line, l: Text(f':{l},{line}y', True).execute()) + Key('enter'),
                'change line': Key('escape,c,c'),
                'clip yank': Key('",*,y'),
                'clip paste': Key('",*,p'),
                'after': Key('escape,A'),
                'before': Key('escape,I'),
                'spock': Key('i,space,escape'),
                '[<n>] lent': Function(lambda n: Text(f'{n}<', True).execute()),
                '[<n>] rent': Function(lambda n: Text(f'{n}<', True).execute()),
                'sent': Text(':left') + Key('enter'),
                'replace <char>': Key('r,%(char)s'),
                'go upper': Key('g,U'),
                'go lower': Key('g,u'),
                'wrap': Key('g,q'),
                'define': Key('g,d'),
                'change go next': Key('c,g,n'),

                # File
                'save': Key('escape,colon,w,enter'),
                'quit': Key('escape,colon,q,enter'),
                'write out': Key('escape,colon,w,q,enter'),
                'bail': Key('escape,colon,q,!,enter'),
                'close buff': Key('escape,colon,b,d,enter'),
                'kill buff': Key('escape,colon,b,w,enter'),
                'fuzzy [<text>]': Key('c-p') + Text('%(text)s'),
                'tree': Key('c-backslash'),

                # Navigation
                'search [<text>]': Key('slash/20') + Function(enter_optional_text),
                'back search [<text>]': Key('?') + Function(enter_optional_text),
                'zed zed': Key('escape,z,z'),
                'zed top': Key('escape,z,t'),
                'zed bottom': Key('escape,z,b'),
                'run in': Key('escape,c-i'),
                'run out': Key('escape,c-o'),
                'win right': Key('escape,space,w,l'),
                'win left': Key('escape,space,w,h'),

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
                ShortIntegerRef('l', 1, 10000),
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


vim = Vim()
vim.load()


def unload() -> None:
    vim.unload()
