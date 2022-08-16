from dragonfly import Grammar, MappingRule, Key, IntegerRef, Function, Text, Dictation
from extras.special_chars import special_chars


class Vim:
    _grammar_name = 'vim'
    _grammar = None

    def _select(self):
        Key('v').execute()
        print('v')

    def _in_word(self):
        Key('i,w').execute()
        print('iw')

    def _in_big_word(self):
        Key('i,W').execute()
        print('iW')

    def _around_word(self):
        Key('a,w').execute()
        print('aw')

    def _around_big_word(self):
        Key('a,W').execute()
        print('aW')

    def _in_char(self, char):
        Key('i').execute()
        Text(char, True).execute()
        print(f'i{char}')

    def _around_char(self, char):
        Key('a').execute()
        Text(char, True).execute()
        print(f'a{char}')

    def _find(self, char):
        Key('f').execute()
        Text(char, True).execute()
        print(f'f{char}')

    def _back_find(self, char):
        Key('F').execute()
        Text(char, True).execute()
        print(f'F{char}')

    def _till(self, char):
        Key('t').execute()
        Text(char, True).execute()
        print(f't{char}')

    def _back_till(self, char):
        Key('T').execute()
        Text(char, True).execute()
        print(f'T{char}')

    def _make_vim_rule(self):
        return MappingRule(
            name='vim_rule',
            mapping={
                # Modes
                'insert': Key('i') + Function(lambda: print('i')),
                'select': Function(self._select),
                'block': Key('c-v') + Function(lambda: print('c-v')),

                # Navigation
                'find <char>': Function(self._find),
                'back find <char>': Function(self._back_find),
                'till <char>': Function(self._till),
                'back till <char>': Function(self._back_till),

                # Select
                'select [in] word': Function(self._select) + Function(self._in_word),
                'select [in] big word': Function(self._select) + Function(self._in_big_word),
                'select out word': Function(self._select) + Function(self._around_word),
                'select out big word': Function(self._select) + Function(self._around_big_word),
                'select in <char>': Function(self._select) + Function(self._in_char),
                'select out <char>': Function(self._select) + Function(self._around_char),
                'select find <char>': Function(self._select) + Function(self._find),
                'select back find <char>': Function(self._select) + Function(self._back_find),
                'select till <char>': Function(self._select) + Function(self._till),
                'select back till <char>': Function(self._select) + Function(self._back_till),

                # # Files
                # 'save': Key('colon, w, enter') + Function(lambda: print(':w enter')),
                # 'quit': Key('colon, q, enter') + Function(lambda: print(':q enter')),
                # 'buff': Key('space,b,p') + Function(lambda: print('space,b,p')),
                # 'next buff': Key('space,b,n') + Function(lambda: print('space,b,n')),
                # 'reopen': Key('ws-t') + Function(lambda: print('ws-t')),

                # # Search
                # 'search <char>': Key('slash') + Text('%(char)s') + Key('enter') + Function(lambda char: print(f'/ {char} enter')),
                # 'back search <char>': Key('?') + Text('%(char)s') + Key('enter') + Function(lambda char: print(f'? {char} enter')),
                # '[<n>] next': Key('n:%(n)d') + Function(lambda n: print(f'{n}n')),
                # 'star': Key('*') + Function(lambda: print('*')),
                # 'fuzzy <text>': Key('c-p') + Text('%(text)s') + Function(lambda text: print(f'c-p {text}')),

                # # Navigation
                # 'top': Key('g,g') + Function(lambda: print('gg')),
                # 'bottom': Key('G') + Function(lambda: print('G')),
                # 'zed zed': Key('z,z') + Function(lambda: print('zz')),
                # 'zed top': Key('z,t') + Function(lambda: print('zt')),
                # 'zed bottom': Key('z,b') + Function(lambda: print('zb')),
                # '[<n>] up': Key('k:%(n)d') + Function(lambda n: print(f'{n}k')),
                # '[<n>] down': Key('j:%(n)d') + Function(lambda n: print(f'{n}j')),
                # '[<n>] pup': Key('c-u:%(n)d') + Function(lambda n: print(f'{n}c-u')),
                # '[<n>] pea down': Key('c-d:%(n)d') + Function(lambda n: print(f'{n}c-d')),
                # '[<n>] left': Key('h:%(n)d') + Function(lambda n: print(f'{n}h')),
                # '[<n>] right': Key('l:%(n)d') + Function(lambda n: print(f'{n}l')),
                # 'line <n>': Key('colon') + Text('%(n)d') + Key('enter') + Function(lambda n: print(f':{n} enter')),
                # 'start': Key('0') + Function(lambda: print('0')),
                # 'end': Key('$') + Function(lambda: print('$')),
                # 'till <char>': Key('t') + Text('%(char)s') + Function(lambda char: print(f'f {char}')),
                # 'find <char>': Key('f') + Text('%(char)s') + Function(lambda char: print(f'f {char}')),
                # 'run in': Key('c-i') + Function(lambda: print('c-i')),
                # 'run out': Key('c-o') + Function(lambda: print('c-o')),
                # 'word': Key('w') + Function(lambda: print('w')),

                # # Editing
                # '[<n>] slap': Key('o:%(n)d') + Function(lambda n: print(f'{n}o')),
                # '[<n>] bump': Key('O:%(n)d') + Function(lambda n: print(f'{n}O')),
                # '[<n>] undo': Key('u:%(n)d') + Function(lambda n: print(f'{n}u')),
                # '[<n>] redo': Key('c-r:%(n)d') + Function(lambda n: print(f'{n}c-r')),
                # 'wipe': Key('d, d') + Function(lambda: print('dd')),
                # 'yank': Key('y') + Function(lambda: print('y')),
                # 'yank line': Key('y,y') + Function(lambda: print('yy')),
                # '[<n>] paste': Key('p:%(n)d') + Function(lambda n: print(f'{n}p')),
                # 'back paste': Key('P') + Function(lambda: print('P')),
                # '[<n>] zip': Key('x:%(n)d') + Function(lambda n: print(f'{n}x')),
                # 'delete': Key('d') + Function(lambda: print('d')),
                # 'delete inner word': Key('d,i,w') + Function(lambda: print('diw')),
                # 'space': Key('i') + Text(' ') + Key('escape') + Function(lambda: print("i ' ' escape")),
                # '[<n>] repeat': Key('.:%(n)d') + Function(lambda n: print(f'{n}.')),
                # 'append': Key('A') + Function(lambda: print('a')),
                # 'prep': Key('I') + Function(lambda: print('I')),
                # 'change': Key('c') + Function(lambda: print('c')),
                # 'change inner word': Key('c,i,w') + Function(lambda: print('ciw')),
                # 'select inner word': Key('v,i,w') + Function(lambda: print('viw')),
                # 'change in quotes': Key('v,i,w') + Function(lambda: print('viw')),
                # 'select line': Key('V') + Function(lambda: print('V')),
                # 'select in quotes': Key("v,i,'") + Function(lambda: print("vi'")),
                # 'select around quotes': Key("v,a,'") + Function(lambda: print("va'")),
            },
            extras=[
                IntegerRef('n', 1, 1000),
                Dictation('text'),
                special_chars(),
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
