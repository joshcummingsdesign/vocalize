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

    def _optional_repeat(self, command: str, n: Optional[int] = None) -> None:
        """
        Optionally repeat a command n times

        @since 0.4.0
        """
        if n > 1:
            command = f'{n}{command}'

        Text(command, True).execute()

    def _optional_key_repeat(self, key: str, n: Optional[int] = None) -> None:
        """
        Optionally repeat a key n times

        @since 0.4.0
        """
        if n > 1:
            Text(f'{n}').execute()

        Key(key, True).execute()

    def _play_macro(self, n: Optional[int] = None, char: Optional[str] = None) -> None:
        """
        Play a macro with optional repeat and register

        @since 0.4.0
        """
        if n > 1:
            Text(f'{n}', True).execute()

        Text(f'@{char}', True).execute() if char else Text('@q').execute()

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
                '[<n>] zip': Function(lambda n: self._optional_repeat('a', n)),
                '[<n>] blip': Function(lambda n: self._optional_repeat('i', n)),
                'block': Key('c-v'),

                # Operators
                'select': Text('v'),
                'change': Text('c'),
                'del': Text('d'),
                'yank': Text('y'),
                'format': Text('='),

                # Motions
                '[<n>] left': Function(lambda n: self._optional_repeat('h', n)),
                '[<n>] right': Function(lambda n: self._optional_repeat('l', n)),
                '[<n>] up': Function(lambda n: self._optional_repeat('k', n)),
                '[<n>] down': Function(lambda n: self._optional_repeat('j', n)),
                '[<n>] ascend': Function(lambda n: self._optional_repeat('-', n)),
                '[<n>] descend': Function(lambda n: self._optional_repeat('+', n)),
                '[<n>] find <char>': Function(lambda n: self._optional_repeat('f', n)) + Text('%(char)s'),
                '[<n>] bind <char>': Function(lambda n: self._optional_repeat('F', n)) + Text('%(char)s'),
                '[<n>] till <char>': Function(lambda n: self._optional_repeat('t', n)) + Text('%(char)s'),
                '[<n>] bill <char>': Function(lambda n: self._optional_repeat('T', n)) + Text('%(char)s'),
                '[<n>] biff': Function(lambda n: self._optional_repeat(',', n)),
                '[<n>] rift': Function(lambda n: self._optional_repeat(';', n)),
                '[<n>] cent': Function(lambda n: self._optional_repeat(')', n)),
                '[<n>] bent': Function(lambda n: self._optional_repeat('(', n)),
                '[<n>] raft': Function(lambda n: self._optional_repeat('}', n)),
                '[<n>] laugh': Function(lambda n: self._optional_repeat('{', n)),
                'head': Text('gg'),
                'foot': Text('G'),
                'snap': Text('^'),
                'first': Text('0'),
                'last': Text('$'),
                'match': Key('percent'),
                'high': Text('H'),
                'middle': Text('M'),
                'low': Text('L'),

                # Text Objects
                'inner': Text('i'),
                'around': Text('a'),
                'paragraph': Text('p'),
                '[<n>] word': Function(lambda n: self._optional_repeat('w', n)),
                '[<n>] big word': Function(lambda n: self._optional_repeat('W', n)),
                '[<n>] bird': Function(lambda n: self._optional_repeat('b', n)),
                '[<n>] big bird': Function(lambda n: self._optional_repeat('B', n)),
                '[<n>] end': Function(lambda n: self._optional_repeat('e', n)),
                '[<n>] big end': Function(lambda n: self._optional_repeat('E', n)),

                # Registers
                'register [<char>]': Function(lambda char: Text(f'"{char}' if char else '"*', True).execute()),

                # Editing
                'select [<n>] (line | lines)': Key('V') + Function(lambda n: Text(f'{n - 1}j', True).execute() if n > 1 else False),
                'wipe': Text('dd'),
                'whip': Text('^C'),
                'dart': Key('c-d'),
                'del [<n>] (line | lines)': Function(lambda n: self._optional_repeat('dd', n)),
                'yank [<n>] (line | lines)': Function(lambda n: self._optional_repeat('Y', n)),
                'change line': Text('cc'),
                'dupe': Text('Yp'),
                'cheap': Text('C'),
                'sweep': Text('D'),
                '[<n>] after': Function(lambda n: self._optional_repeat('A', n)),
                '[<n>] little after': Function(lambda n: self._optional_repeat('a', n)),
                '[<n>] before': Function(lambda n: self._optional_repeat('I', n)),
                'sneak': Key('c-o'),
                'recall': Key('c-r'),
                'again': Key('c-a'),
                'recall it': Key('c-r') + Text('"'),
                'raw': Key('c-v'),
                'where': Key('c-w'),
                '[<n>] paste': Function(lambda n: self._optional_repeat('p', n)),
                '[<n>] baste': Function(lambda n: self._optional_repeat('P', n)),
                '[<n>] pete': Function(lambda n: self._optional_repeat('.', n)),
                '[<n>] undo': Function(lambda n: self._optional_repeat('u', n)),
                'scratch': Key('escape') + Text('u'),
                '[<n>] redo': Function(lambda n: self._optional_key_repeat('c-r', n)),
                '[<n>] slice': Function(lambda n: self._optional_repeat('x', n)),
                '[<n>] splice': Function(lambda n: self._optional_repeat('X', n)),
                '[<n>] bump': Function(lambda n: self._optional_repeat('o', n)),
                'bit': Key('o/2,i'),
                '[<n>] nudge': Function(lambda n: self._optional_repeat('O', n)),
                'nit': Key('O/2,i'),
                '[<n>] sit': Function(lambda n: self._optional_repeat('*', n)),
                '[<n>] bit': Function(lambda n: self._optional_repeat('#', n)),
                '[<n>] sub': Function(lambda n: self._optional_repeat('s', n)),
                'sort': Text(':sort') + Key('enter'),
                'sort numeric': Text(':sort n') + Key('enter'),
                'resort': Text(':sort!') + Key('enter'),
                'go increment': Key('g,c-a'),
                'go decrement': Key('g,c-x'),
                '[<n>] increment': Function(lambda n: self._optional_key_repeat('c-a', n)),
                '[<n>] decrement': Function(lambda n: self._optional_key_repeat('c-x', n)),
                '[<n>] join': Function(lambda n: self._optional_repeat('J', n)),
                '[<n>] go join': Function(lambda n: self._optional_repeat('gJ', n)),
                '[<n>] lent': Function(lambda n: self._optional_repeat('<', n)),
                '[<n>] rent': Function(lambda n: self._optional_repeat('>', n)),
                'big lent': Text(':left') + Key('enter'),
                '[<n>] replace [<char>]': Function(lambda n: self._optional_repeat('r', n)) + Text('%(char)s'),
                'go upper': Text('gU'),
                'go lower': Text('gu'),
                'wrap': Text('gq'),
                'define': Text('gd'),
                'tip': Text('gh'),
                'record [<char>]': Function(lambda char: Text(f'q{char}' if char else 'qq', True).execute()),
                'mac': Text('q'),
                '[<n>] play [<char>]': Function(self._play_macro),
                '[<n>] replay': Function(lambda n: self._optional_repeat('@@', n)),

                # Navigation
                'line <line>': Text('%(line)dG'),
                'column <line>': Text('%(line)d|'),
                '[<n>] next': Function(lambda n: self._optional_repeat('n', n)),
                '[<n>] previous': Function(lambda n: self._optional_repeat('N', n)),
                'jump word': Key('escape,space,j,w'),
                'jump line': Key('escape,space,j,l'),

                # File
                'save': Key('escape/20,colon,w,enter'),
                'quit': Key('escape,colon,q,enter'),
                'puff': Key('escape,space,b,p'),
                'buff': Key('escape,space,b,n'),
                '[<n>] choose': Key('c-j:%(n)d'),
                '[<n>] booze': Key('c-k:%(n)d'),

                # Modifiers
                '[<n>] stop': Key('win:up,escape:%(n)d'),
                '[<n>] enter': Key('win:up,enter:%(n)d'),
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
                'light <n> right': Key('shift:down,right:%(n)d,shift:up'),
                'light <n> left': Key('shift:down,left:%(n)d,shift:up'),
                'light left': Key('ws-left'),
                'light right': Key('ws-right'),
                'big up': Key('w-up'),
                'big down': Key('w-down'),
                'big left': Key('w-left'),
                'big right': Key('w-right'),
                'copy': Key('w-c'),
                'big copy': Key('ws-c'),
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
                'twig': Key('{,percent'),
                'spread': Text('...'),
                'damp': Text(' && '),
                'soar': Text(' || '),
                'arrow': Text('->'),
                'lambda': Text(' => '),
                'single equals': Text(' = '),
                'double equals': Text(' == '),
                'triple equals': Text(' === '),
                'loose not equals': Text(' != '),
                'not equals': Text(' !== '),
                'greater equals': Text(' >= '),
                'less equals': Text(' <= '),
                'bullet': Text('- '),
                'num list <n>': Text('%(n)d. '),
                'check': Text('✓'),
                'commercial': Text('.com'),

                # Commentary
                'comment': Text('gc'),
                'comment [<n>] (line | lines)': Function(lambda n: self._optional_repeat('gcc', n)),
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
                'select all': Text('ggVG'),
                'select <line>': Text('%(line)dGV'),
                'select <line> from <l>': Text('%(l)dGV%(line)dG'),
                'del all': Text('ggdG'),
                'change all': Text('ggcG'),
                'del <line>': Function(lambda line: Text(f':{line}d', True).execute()) + Key('enter'),
                'del <line> from <l> [in] [<char>]': Function(lambda line, l, char: self._line_in_register('d', line, l, char)),
                'move <line>': Function(lambda line: Text(f':{line}m.', True).execute()) + Key('enter'),
                'move <line> from <l>': Function(lambda line, l: self._line_in_register('m.', line, l)),
                'yank all': Text('ggVGy'),
                'yank <line>': Function(lambda line: Text(f':{line}y', True).execute()) + Key('enter'),
                'yank <line> from <l> [in] [<char>]': Function(lambda line, l, char: self._line_in_register('y', line, l, char)),
                'change go next': Text('cgn'),
                'said': Key('colon') + Text('s/'),
                'said all': Key('colon,percent') + Text('s/'),
                'said block': Key('colon,s,slash,backslash,percent,V'),
                'said pete': Text('g&'),
                'complete': Key('c-n'),
                'go block': Text('gv'),
                'norm': Key('colon') + Text('norm '),
                'norm all': Key('colon,percent') + Text('norm '),
                'successive': Text('Q'),
                'global': Key('colon') + Text('g/'),
                'show column': Key('g,c-g'),

                # File
                'leave': Key('Z,Z'),
                'bail': Key('escape,colon,q,!,enter'),
                'close buff': Key('escape,colon,b,d,enter'),
                'kill buff': Key('escape,colon,b,w,enter'),
                'fuzz [<text>]': Key('c-p') + Text('%(text)s'),
                'tree': Key('c-backslash'),
                'double tree': Key('c-backslash:2'),

                # Navigation
                'search [<text>]': Key('slash/20') + Function(enter_optional_text),
                'birch [<text>]': Key('?') + Function(enter_optional_text),
                'zed zed': Text('zz'),
                'zed top': Text('zt'),
                'zed bottom': Text('zb'),
                'run in': Key('c-i'),
                'run out': Key('c-o'),
                'win right': Key('escape,space,w,l'),
                'win left': Key('escape,space,w,h'),
                'mark [<char>]': Function(lambda char: Text(f'm{char}' if char else 'mm', True).execute()),
                'bark [<char>]': Function(lambda char: Text(f'`{char}' if char else '`m', True).execute()),

                # Surround
                'select inner <char>': Text('vi%(char)s'),
                'select around <char>': Text('va%(char)s'),
                'change inner <char>': Text('ci%(char)s'),
                'change inner tag': Text('cit'),
                'change around <char>': Text('ca%(char)s'),
                'del inner <char>': Text('di%(char)s'),
                'del inner tag': Text('dit'),
                'del around <char>': Text('da%(char)s'),
                'yank inner <char>': Text('yi%(char)s'),
                'yank around <char>': Text('ya%(char)s'),
                'surround [with] <char>': Text('S%(char)s'),
                'surround inner <object> [with] <char>': Text('ysi%(object)s%(char)s'),
                'surround around <object> [with] <char>': Text('ysa%(object)s%(char)s'),
                'surround [inner] [word] [with] <char>': Text('ysiw%(char)s'),
                'surround [inner] big word [with] <char>': Text('ysiW%(char)s'),
                'surround line [with] <char>': Text('yss%(char)s'),
                'change surrounding <object> [to] <char>': Text('cs%(object)s%(char)s'),
                'del surrounding <char>': Text('ds%(char)s'),

                # Abolish
                'go snake': Key('c,r,s'),
                'go camel': Key('c,r,c'),
                'go pascal': Key('c,r,m'),
                'go kebab': Key('c,r,minus'),
                'go dot case': Key('c,r,.'),
                'go upper snake': Key('c,r,u'),
                'go space case': Key('c,r,space'),
                'go title': Key('c,r,t'),

                # Typing
                'slap <text>': Text('%(text)s'),
                'smack <text>': Text('%(text)s '),
                'tag <text>': Text('<') + Function(lambda text: Text(to_kebab(text), True).execute()) + Key('>'),
                'tag pascal <text>': Text('<') + Function(lambda text: Text(to_pascal(text), True).execute()) + Key('>'),
                'tag dev': Text('<div>'),
                'num <n>': Text('%(n)s'),
                'no space <text>': Function(lambda text: Text(text.replace(' ', ''), True).execute()),
                'quote no space <text>': Function(lambda text: Text("'" + text.replace(' ', '') + "'", True).execute()),
                'bunny no space <text>': Function(lambda text: Text('"' + text.replace(' ', '') + '"', True).execute()),
                'snake <text>': Function(lambda text: Text(to_snake(text), True).execute()),
                'quote snake <text>': Function(lambda text: Text("'" + to_snake(text) + "'", True).execute()),
                'bunny snake <text>': Function(lambda text: Text('"' + to_snake(text) + '"', True).execute()),
                'camel <text>': Function(lambda text: Text(to_camel(text), True).execute()),
                'quote camel <text>': Function(lambda text: Text("'" + to_camel(text) + "'", True).execute()),
                'bunny camel <text>': Function(lambda text: Text('"' + to_camel(text) + '"', True).execute()),
                'pascal <text>': Function(lambda text: Text(to_pascal(text), True).execute()),
                'quote pascal <text>': Function(lambda text: Text("'" + to_pascal(text) + "'", True).execute()),
                'bunny pascal <text>': Function(lambda text: Text('"' + to_pascal(text) + '"', True).execute()),
                'kebab <text>': Function(lambda text: Text(to_kebab(text), True).execute()),
                'quote kebab <text>': Function(lambda text: Text("'" + to_kebab(text) + "'", True).execute()),
                'bunny kebab <text>': Function(lambda text: Text('"' + to_kebab(text) + '"', True).execute()),
                'dot case <text>': Function(lambda text: Text(to_dot_case(text), True).execute()),
                'quote dot case <text>': Function(lambda text: Text("'" + to_dot_case(text) + "'", True).execute()),
                'bunny dot case <text>': Function(lambda text: Text('"' + to_dot_case(text) + '"', True).execute()),
                'constant <text>': Function(lambda text: Text(to_snake(text).upper(), True).execute()),
                'quote constant <text>': Function(lambda text: Text("'" + to_snake(text).upper() + "'", True).execute()),
                'bunny constant <text>': Function(lambda text: Text('"' + to_snake(text).upper() + '"', True).execute()),
                'yell <text>': Function(lambda text: Text(text.upper(), True).execute()),
                'quote yell <text>': Function(lambda text: Text("'" + text.upper() + "'", True).execute()),
                'bunny yell <text>': Function(lambda text: Text('"' + text.upper() + '"', True).execute()),
                'sentence <text>': Function(lambda text: Text(uc_first(text), True).execute()),
                'quote sentence <text>': Function(lambda text: Text("'" + uc_first(text) + "'", True).execute()),
                'bunny sentence <text>': Function(lambda text: Text('"' + uc_first(text) + '"', True).execute()),
                'title <text>': Function(lambda text: Text(text.title(), True).execute()),
                'quote title <text>': Function(lambda text: Text("'" + text.title() + "'", True).execute()),
                'bunny title <text>': Function(lambda text: Text('"' + text.title() + '"', True).execute()),

                # File Extensions
                'dot js': Text('.js'),
                'dot ts': Text('.ts'),
                'dot ts ex': Text('.tsx'),
                'dot pie': Text('.py'),
                'dot html': Text('.html'),
                'dot see ss': Text('.css'),
                'dot es see ss': Text('.scss'),

                # Words
                'jason': Text('json'),
                'environment': Text('env'),
                'con fig': Text('config'),

                # JavaScript
                'kuhn': Text('const '),
                'let': Text('let '),
                'prop <text>': Function(lambda text: Text(to_camel(text) + '={', True).execute()),
                'arrow funk <text>': Function(lambda text: Text('const ' + to_camel(text) + ' = () => ', True).execute()),
                'arrow funk pascal <text>': Function(lambda text: Text('const ' + to_pascal(text) + ' = () => ', True).execute()),

                # Scss
                'sass <text>': Function(lambda text: Text(to_kebab(text), True).execute()) + Key('colon,space,semicolon,left'),
                '<line> pixels': Text('%(line)dpx'),

                # Python
                'stir': Text('str'),
                'dictionary': Text('dict'),
                'def <text>': Function(lambda text: Text('def ' + to_snake(text) + '(', True).execute()),

                # Code
                'key <text>': Function(lambda text: Text(to_kebab(text) + ': ', True).execute()),
                'ski <text>': Function(lambda text: Text("'" + to_kebab(text) + "': ", True).execute()),
                'far <text>': Function(lambda text: Text(to_snake(text) + ' = ', True).execute()),
                'funk <text>': Function(lambda text: Text(to_snake(text) + '(', True).execute()),
                'funk camel <text>': Function(lambda text: Text(to_camel(text) + '(', True).execute()),
                'e num': Text('enum'),

                # Quick Typing
                'hips': Text('https://'),
                'null': Text('null'),
                'read me': Text('README.md'),
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
