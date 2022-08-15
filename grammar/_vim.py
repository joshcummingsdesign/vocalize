from dragonfly import Grammar, MappingRule, Key, IntegerRef, Function, Text, Dictation
from helpers.string import filter_char


class Vim:
    _grammar_name = 'vim'
    _grammar = None

    def _make_vim_rule(self):
        return MappingRule(
            name='vim_rule',
            mapping={
                # Modes
                'insert': Key('i') + Function(lambda: print('i')),
                'out': Key('escape') + Function(lambda: print('escape')),
                'select': Key('v') + Function(lambda: print('v')),

                # Files
                'save': Key('colon, w, enter') + Function(lambda: print(':w enter')),
                'quit': Key('colon, q, enter') + Function(lambda: print(':q enter')),
                'buff': Key('space,b,p') + Function(lambda: print('space,b,p')),
                'next buff': Key('space,b,n') + Function(lambda: print('space,b,n')),
                'reopen': Key('ws-t') + Function(lambda: print('ws-t')),

                # Search
                'search <text>': Key('slash') + Text('%(text)s') + Key('enter') + Function(lambda text: print(f'/ {text} enter')),
                'next': Key('n') + Function(lambda: print('n')),

                # Navigation
                'top': Key('g,g') + Function(lambda: print('gg')),
                'bottom': Key('G') + Function(lambda: print('G')),
                'zed zed': Key('z,z') + Function(lambda: print('zz')),
                'zed top': Key('z,t') + Function(lambda: print('zt')),
                'zed bottom': Key('z,b') + Function(lambda: print('zb')),
                '[<n>] up': Key('k:%(n)d') + Function(lambda n: print(f'{n}k')),
                '[<n>] down': Key('j:%(n)d') + Function(lambda n: print(f'{n}j')),
                '[<n>] pup': Key('c-u:%(n)d') + Function(lambda n: print(f'{n}c-u')),
                '[<n>] pea down': Key('c-d:%(n)d') + Function(lambda n: print(f'{n}c-d')),
                '[<n>] left': Key('h:%(n)d') + Function(lambda n: print(f'{n}h')),
                '[<n>] right': Key('l:%(n)d') + Function(lambda n: print(f'{n}l')),
                'line <n>': Key('colon') + Text('%(n)d') + Key('enter') + Function(lambda n: print(f':{n} enter')),
                'start': Key('0') + Function(lambda: print('0')),
                'end': Key('$') + Function(lambda: print('$')),
                'till <char>': Key('t') + Text('%(char)s') + Function(lambda char: print(f't {char}')),
                'find <char>': Key('f') + Text('%(char)s') + Function(lambda char: print(f'f {char}')),
                'run in': Key('c-i') + Function(lambda: print('c-i')),
                'run out': Key('c-o') + Function(lambda: print('c-o')),

                # Editing
                '[<n>] slap': Key('o:%(n)d') + Function(lambda n: print(f'{n}o')),
                '[<n>] bump': Key('O:%(n)d') + Function(lambda n: print(f'{n}O')),
                'wipe': Key('d, d') + Function(lambda: print('dd')),
                '[<n>] undo': Key('u:%(n)d') + Function(lambda n: print(f'{n}u')),
                '[<n>] redo': Key('c-r:%(n)d') + Function(lambda n: print(f'{n}c-r')),
                'yank': Key('y') + Function(lambda: print('y')),
                'yank line': Key('y,y') + Function(lambda: print('yy')),
                '[<n>] paste': Key('p:%(n)d') + Function(lambda n: print(f'{n}p')),
                'back paste': Key('P') + Function(lambda: print('P')),
                '[<n>] zap': Key('x:%(n)d') + Function(lambda n: print(f'{n}x')),
                'delete': Key('d') + Function(lambda: print('d')),
                'delete inner word': Key('d,i,w') + Function(lambda: print('diw')),
                'select inner word': Key('v,i,w') + Function(lambda: print('viw')),
                'select line': Key('V') + Function(lambda: print('V')),
                'change': Key('c') + Function(lambda: print('c')),
                'space': Key('i') + Text(' ') + Key('escape') + Function(lambda: print("i ' ' escape")),
                '[<n>] repeat': Key('.:%(n)d') + Function(lambda n: print(f'{n}.')),
                'append': Key('A') + Function(lambda: print('a')),
                'prep': Key('I') + Function(lambda: print('I')),
            },
            extras=[
                IntegerRef('n', 1, 1000),
                Dictation('text'),
                Dictation('char').apply(filter_char),
            ],
            defaults={
                'n': 1,
            }
        )

    def load(self):
        self._grammar = Grammar(self._grammar_name)
        self._grammar.add_rule(self._make_vim_rule())
        self._grammar.load()


vim = Vim()
vim.load()
