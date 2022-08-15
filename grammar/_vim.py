from dragonfly import Grammar, MappingRule, Key, IntegerRef, Function, Text, Dictation


class Vim:
    _grammar_name = 'vim'
    _grammar = None

    def _make_vim_rule(self):
        return MappingRule(
            name='vim_rule',
            mapping={
                'in': Key('i') + Function(lambda: print('i')),
                'out': Key('escape') + Function(lambda: print('escape')),
                '[<n>] slap': Key('o:%(n)d') + Function(lambda n: print(f'{n}o'), extra={'n'}),
                '[<n>] bump': Key('O:%(n)d') + Function(lambda n: print(f'{n}O'), extra={'n'}),
                'wipe': Key('d, d') + Function(lambda: print('dd')),
                'save': Key('colon, w, enter') + Function(lambda: print(':w enter')),
                'quit': Key('colon, q, enter') + Function(lambda: print(':q enter')),
                'undo': Key('u') + Function(lambda: print('u')),
                'redo': Key('c-r') + Function(lambda: print('c-r')),
                'top': Key('g,g') + Function(lambda: print('gg')),
                'bottom': Key('G') + Function(lambda: print('G')),
                'zed zed': Key('z,z') + Function(lambda: print('zz')),
                'zed top': Key('z,t') + Function(lambda: print('zt')),
                'zed bottom': Key('z,b') + Function(lambda: print('zb')),
                '[<n>] up': Key('k:%(n)d') + Function(lambda n: print(f'{n}k'), extra={'n'}),
                '[<n>] down': Key('j:%(n)d') + Function(lambda n: print(f'{n}j'), extra={'n'}),
                'line <n>': Key('colon') + Text('%(n)d') + Key('enter') + Function(lambda n: print(f':{n} enter'), extra={'n'}),
                'search <text>': Key('slash') + Text('%(text)s') + Key('enter') + Function(lambda text: print(f'/ {text} enter')),
            },
            extras=[
                IntegerRef('n', 1, 1000),
                Dictation('text'),
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
