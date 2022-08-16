from dragonfly import Grammar, MappingRule, Key, Function


class Keyboard:
    _grammar_name = 'keyboard'
    _grammar = None

    def _make_keyboard_rule(self):
        return MappingRule(
            name='keyboard_rule',
            mapping={
                'go': Key('enter') + Function(lambda: print('enter')),
                'del': Key('backspace') + Function(lambda: print('backspace')),
                'zap': Key('w-backspace') + Function(lambda: print('w-backspace')),
                'out': Key('escape') + Function(lambda: print('escape')),
            },
        )

    def load(self):
        self._grammar = Grammar(self._grammar_name)
        self._grammar.add_rule(self._make_keyboard_rule())
        self._grammar.load()


keyboard = Keyboard()
keyboard.load()
