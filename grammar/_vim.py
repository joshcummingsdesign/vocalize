from dragonfly import Grammar, MappingRule, Key, IntegerRef, Function


class Vim:
    _grammar_name = 'vim'
    _grammar = None

    def _make_vim_rule(self):
        return MappingRule(
            name='vim_rule',
            mapping={
                'in': Key('i') + Function(lambda: print('i')),
                'out': Key('escape') + Function(lambda: print('escape')),
                '[<n>] slap': Key('%(n)d,o') + Function(lambda n: print(f'{n}o'), extra={'n'}),
                '[<n>] bump': Key('%(n)d,O') + Function(lambda n: print(f'{n}O'), extra={'n'}),
                'wipe': Key('d, d') + Function(lambda: print('dd')),
                'save': Key('colon, w, enter') + Function(lambda: print(':w enter')),
                'quit': Key('colon, q, enter') + Function(lambda: print(':q enter')),
                'undo': Key('u') + Function(lambda: print('u')),
                'redo': Key('c-r') + Function(lambda: print('c-r')),
            },
            extras=[
                IntegerRef("n", 1, 1000),
            ],
            defaults={
                "n": 1,
            }
        )

    def load(self):
        self._grammar = Grammar(self._grammar_name)
        self._grammar.add_rule(self._make_vim_rule())
        self._grammar.load()


vim = Vim()
vim.load()
