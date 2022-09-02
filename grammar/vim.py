from actions import enter_optional_text
from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Key, IntegerRef, ShortIntegerRef, Text, Function, Dictation
from extras import character, modifiers
from helpers.string import to_snake, to_camel, to_pascal, to_kebab, to_dot_case, uc_first
from rules import SeriesMappingRule
from typing import Optional


class Grammar(BaseGrammar):
    """
    Vim grammar

    @since 0.1.0
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

    def _register(self, char: Optional[str] = None) -> None:
        """
        Set the Vim register

        @since 0.1.0
        """
        Key('"', True).execute()
        if char:
            Text(char, True).execute()
        else:
            Text('*', True).execute()

    def _line_in_register(self, command: str, line: int, l: int, char: Optional[str] = None) -> None:
        """
        Perform a command on a line with optional register

        @since 0.1.0
        """
        Text(f':{l},{line}{command}', True).execute()

        if char:
            Text(f' {char}', True).execute()

        Key('enter').execute()

    def _make_vim_series_rule(self) -> Rule:
        """
        Vim series rule factory

        @since 0.1.0
        """
        return SeriesMappingRule(
            name='vim_series_rule',
            mapping={
                # Modes
                '(zip | insert)': Key('escape,l,i'),
                'blip': Key('escape,i'),
                'block': Key('escape,c-v'),

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

                # Registers
                'register [<char>]': Function(self._register),

                # Editing
                'select [<n>] (line | lines)': Key('escape,V') + Function(lambda n: Text(f'{n - 1}j', True).execute() if n > 1 else False),
                'wipe': Key('escape,d,d'),
                'whip': Key('escape,^,C'),
                'delete [<n>] (line | lines)': Function(lambda n: Text(f'{n}dd', True).execute()),
                'yank [<n>] (line | lines)': Function(lambda n: Text(f'{n}yy', True).execute()),
                'dupe': Text('yyp'),
                'cheap': Key('C'),
                'sweep': Key('D'),
                'after': Key('escape,A'),
                'before': Key('escape,I'),
                'spock': Key('i,space,escape'),
                '[<n>] paste': Key('p:%(n)d'),
                'clip yank': Text('"*y'),
                '[<n>] clip paste': Text('"*') + Key('p:%(n)d'),
                '[<n>] clip back paste': Text('"*') + Key('P:%(n)d'),
                '[<n>] back paste': Key('P:%(n)d'),
                '[<n>] pete': Key('.:%(n)d'),
                '[<n>] (scratch | undo)': Key('escape') + Function(lambda n: Text(f'{n}u', True).execute()),
                '[<n>] redo': Key('escape') + Function(lambda n: Text(f'{n}', True).execute()) + Key('c-r'),
                '[<n>] slice': Function(lambda n: Text(f'{n}x', True).execute()),
                '[<n>] splice': Function(lambda n: Text(f'{n}X', True).execute()),
                '[<n>] bump': Function(lambda n: Text(f'{n}o', True).execute()),
                '[<n>] nudge': Function(lambda n: Text(f'{n}O', True).execute()),
                '[<n>] sit': Function(lambda n: Text(f'{n}*', True).execute()),
                'sort': Text(':sort') + Key('enter'),

                # Navigation
                'line <line>': Key('escape') + Text(':%(line)d') + Key('enter'),
                '[<n>] next': Function(lambda n: Text(f'{n}n', True).execute()),
                '[<n>] previous': Function(lambda n: Text(f'{n}N', True).execute()),

                # File
                'buff': Key('escape,space,b,p'),
                'next buff': Key('escape,space,b,n'),
                '[<n>] choose': Key('c-j:%(n)d'),
                '[<n>] back choose': Key('c-k:%(n)d'),

                # Modifiers
                '[<n>] (zap | axe)': Key('win:up,escape:%(n)d'),
                '[<n>] (enter | slap)': Key('win:up,enter:%(n)d'),
                '[<n>] clap': Key('enter:%(n)d,tab'),
                '[<n>] tab': Key('tab:%(n)d'),
                '[<n>] bat': Key('s-tab:%(n)d'),
                '[<n>] press <mod>': Key('%(mod)s:%(n)d'),

                # Keyboard
                '[<n>] snip': Key('backspace:%(n)d'),
                '[<n>] strike': Key('w-backspace:%(n)d'),
                'strike all': Key('w-up,w-left,ws-down,backspace'),
                'light all': Key('w-a'),
                'light up': Key('ws-up'),
                'light down': Key('ws-down'),
                'light <n> down': Key('shift:down,down:%(n)d,shift:up'),
                'light <n> up': Key('shift:down,up:%(n)d,shift:up'),
                'light left': Key('ws-left'),
                'light right': Key('ws-right'),
                'big up': Key('w-up'),
                'big down': Key('w-down'),
                'big left': Key('w-left'),
                'big right': Key('w-right'),
                'copy': Key('w-c'),
                'pasta': Key('w-v'),
                'big pasta': Key('ws-v'),
                'begin': Key('w-left'),
                '[<n>] oops': Key('w-z:%(n)d'),
                '[<n>] never mind': Key('ws-z:%(n)d'),
                'duplicate': Key('w-d'),
                'bold': Key('w-b'),

                # Special Characters
                'pad <char>': Text(' %(char)s '),
                'tags': Key('<,>,left'),
                'spread': Text('...'),
                'arrow': Text('->'),
                'lambda': Text('=>'),
                'double equals': Text(' == '),
                'triple equals': Text(' === '),
                'loose not equals': Text(' != '),
                'not equals': Text(' !== '),
                'greater equals': Text(' >= '),
                'less equals': Text(' <= '),
                'bullet': Text('- '),
                'check': Text('✓'),

                # Typing
                'type <text>': Text('%(text)s'),
                'sass <text>': Function(lambda text: Text(to_kebab(text), True).execute()) + Key('colon,space,semicolon,left'),
                'prop <text>': Text('%(text)s: '),
                'php echo': Key('<,?,=,space,?,>,left,left,left,space'),
                'tag <text>': Text('<') + Function(lambda text: Text(to_kebab(text), True).execute()) + Key('>'),
                'tag dev': Text('<div>'),
                'num <n>': Text('%(n)s'),
                'key <text>': Text('%(text)s '),
                'snake <text>': Function(lambda text: Text(to_snake(text), True).execute()),
                'camel <text>': Function(lambda text: Text(to_camel(text), True).execute()),
                'pascal <text>': Function(lambda text: Text(to_pascal(text), True).execute()),
                'kebab <text>': Function(lambda text: Text(to_kebab(text), True).execute()),
                'dot case <text>': Function(lambda text: Text(to_dot_case(text), True).execute()),
                'upper snake <text>': Function(lambda text: Text(to_snake(text).upper(), True).execute()),
                'upper <text>': Function(lambda text: Text(text.upper(), True).execute()),
                'sentence <text>': Function(lambda text: Text(uc_first(text), True).execute()),
                'title <text>': Function(lambda text: Text(text.title(), True).execute()),
            },
            extras=[
                IntegerRef('n', 1, 1000),
                ShortIntegerRef('line', 1, 10000),
                Dictation('text'),
                character('char'),
                modifiers('mod'),
            ],
            defaults={
                'n': 1,
                'char': '',
            }
        )

    def _make_vim_rule(self) -> Rule:
        """
        Vim rule factory

        @since 0.1.0
        """
        return MappingRule(
            name='vim_rule',
            mapping={
                # Editing
                'select all': Key('g,g,V,G'),
                'select <line>': Text('%(line)dGV'),
                'select <line> from <l>': Text('%(l)dGV%(line)dG'),
                'delete all': Key('g,g,V,G,d'),
                'delete <line>': Function(lambda line: Text(f':{line}d', True).execute()) + Key('enter'),
                'delete <line> from <l> [in] [<char>]': Function(lambda line, l, char: self._line_in_register('d', line, l, char)) + Key('c-o'),
                'move <line>': Function(lambda line: Text(f':{line}m.', True).execute()) + Key('enter'),
                'move <line> from <l>': Function(lambda line, l: self._line_in_register('m.', line, l)),
                'yank all': Key('g,g,V,G,y'),
                'yank <line>': Function(lambda line: Text(f':{line}y', True).execute()) + Key('enter'),
                'yank <line> from <l> [in] [<char>]': Function(lambda line, l, char: self._line_in_register('y', line, l, char)),
                'change line': Key('escape,c,c'),
                '[<n>] lent': Function(lambda n: Text(f'{n}<', True).execute()),
                '[<n>] rent': Function(lambda n: Text(f'{n}>', True).execute()),
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
                'fuzz [<text>]': Key('c-p') + Text('%(text)s'),
                'tree': Key('c-backslash'),

                # Navigation
                'search [<text>]': Key('slash/20') + Function(enter_optional_text),
                'back search [<text>]': Key('?') + Function(enter_optional_text),
                'said': Key('colon,percent') + Text('s///g') + Key('left:3'),
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
