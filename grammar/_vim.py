from dragonfly import Grammar, MappingRule, Key, IntegerRef, Function, Text, Dictation, FuncContext
from extras import chars
from typing import Any, Callable


class Vim:
    """
    The Vim grammar class.

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance.

    @unreleased
    """

    def _select(self) -> None:
        """
        The select operator.

        @unreleased
        """
        Key('v').execute()
        print('v')

    def _change(self) -> None:
        """
        The change operator.

        @unreleased
        """
        Key('c').execute()
        print('c')

    def _delete(self) -> None:
        """
        The delete operator.

        @unreleased
        """
        Key('d').execute()
        print('d')

    def _yank(self) -> None:
        """
        The yank operator.

        @unreleased
        """
        Key('y').execute()
        print('y')

    def _in_word(self) -> None:
        """
        The inner word text object.

        @unreleased
        """
        Key('i,w').execute()
        print('iw')

    def _in_big_word(self) -> None:
        """
        The inner Word text object.

        @unreleased
        """
        Key('i,W').execute()
        print('iW')

    def _around_word(self) -> None:
        """
        The around word text object.

        @unreleased
        """
        Key('a,w').execute()
        print('aw')

    def _around_big_word(self) -> None:
        """
        The around Word text object.

        @unreleased
        """
        Key('a,W').execute()
        print('aW')

    def _in_char(self, char: str) -> None:
        """
        The inside [character] text object.

        @unreleased
        """
        Key('i').execute()
        Text(char, True).execute()
        print(f'i{char}')

    def _around_char(self, char: str) -> None:
        """
        The around [character] text object.

        @unreleased
        """
        Key('a').execute()
        Text(char, True).execute()
        print(f'a{char}')

    def _find(self, char: str) -> None:
        """
        The find motion.

        @unreleased
        """
        Key('f').execute()
        Text(char, True).execute()
        print(f'f{char}')

    def _back_find(self, char: str) -> None:
        """
        The Find motion.

        @unreleased
        """
        Key('F').execute()
        Text(char, True).execute()
        print(f'F{char}')

    def _till(self, char: str) -> None:
        """
        The till motion.

        @unreleased
        """
        Key('t').execute()
        Text(char, True).execute()
        print(f't{char}')

    def _back_till(self, char: str) -> None:
        """
        The Till motion.

        @unreleased
        """
        Key('T').execute()
        Text(char, True).execute()
        print(f'T{char}')

    def _up(self, n: int) -> None:
        """
        The up motion.

        @unreleased
        """
        Key(f'k:{n}', True).execute()
        print(f'{n}k')

    def _down(self, n: int) -> None:
        """
        The down motion.

        @unreleased
        """
        Key(f'j:{n}', True).execute()
        print(f'{n}j')

    def _right(self, n: int) -> None:
        """
        The right motion.

        @unreleased
        """
        Key(f'l:{n}', True).execute()
        print(f'{n}l')

    def _left(self, n: int) -> None:
        """
        The left motion.

        @unreleased
        """
        Key(f'h:{n}', True).execute()
        print(f'{n}h')

    def _matching(self) -> None:
        """
        The % motion.

        @unreleased
        """
        Key('%').execute()
        print('%')

    def _search(self, text: str) -> None:
        """
        The search motion.

        @unreleased
        """
        Key('slash').execute()
        Text(text, True).execute()
        Key('enter').execute()
        print(f'/ {text} enter')

    def _back_search(self, text: str) -> None:
        """
        The backwards search motion.

        @unreleased
        """
        Key('?').execute()
        Text(text, True).execute()
        Key('enter').execute()
        print(f'? {text} enter')

    def _make_operator(self, name: str, fn: Callable[..., None]) -> dict[str, Any]:
        """
        Make an operator for text objects with its motions.

        @unreleased

        @param name: str - The operator name.
        @param fn: Callable[..., None] - The operator callback function.
        """
        return {
            f'{name}': Function(fn),
            f'{name} [in] word': Function(fn) + Function(self._in_word),
            f'{name} [in] big word': Function(fn) + Function(self._in_big_word),
            f'{name} out word': Function(fn) + Function(self._around_word),
            f'{name} out big word': Function(fn) + Function(self._around_big_word),
            f'{name} in <char>': Function(fn) + Function(self._in_char),
            f'{name} out <char>': Function(fn) + Function(self._around_char),
            f'{name} find <char>': Function(fn) + Function(self._find),
            f'{name} back find <char>': Function(fn) + Function(self._back_find),
            f'{name} till <char>': Function(fn) + Function(self._till),
            f'{name} back till <char>': Function(fn) + Function(self._back_till),
            f'{name} [<n>] up': Function(fn) + Function(self._up),
            f'{name} [<n>] down': Function(fn) + Function(self._down),
            f'{name} [<n>] right': Function(fn) + Function(self._right),
            f'{name} [<n>] left': Function(fn) + Function(self._left),
            f'{name} matching': Function(fn) + Function(self._matching),
            f'{name} search <text>': Function(fn) + Function(self._search),
            f'{name} back search <text>': Function(fn) + Function(self._back_search),
        }

    def _make_vim_rule(self) -> MappingRule:
        """
        The Vim rule factory.

        @unreleased
        """
        return MappingRule(
            name='vim_rule',
            mapping={
                # Mode
                'insert': Key('i') + Function(lambda: print('i')),
                'select': Function(self._select),
                'block': Key('c-v') + Function(lambda: print('c-v')),

                # Motion
                '[<n>] word': Key('w:%(n)d') + Function(lambda n: print(f'{n}w')),
                '[<n>] big word': Key('W:%(n)d') + Function(lambda n: print(f'{n}W')),
                'find <char>': Function(self._find),
                'back find <char>': Function(self._back_find),
                'till <char>': Function(self._till),
                'back till <char>': Function(self._back_till),
                '[<n>] up': Function(self._up),
                '[<n>] down': Function(self._down),
                '[<n>] right': Function(self._right),
                '[<n>] left': Function(self._left),
                'matching': Function(self._matching),
                'search <text>': Function(self._search),
                'back search <text>': Function(self._back_search),

                # Select
                **self._make_operator('select', self._select),
                'select line': Key('%(n)d,V') + Function(lambda n: print(f'{n}V')),
                'select <n> line': Key('V,j:%(n)d') + Function(lambda n: print(f'V{n}j')),

                # Change
                **self._make_operator('change', self._change),

                # Delete
                **self._make_operator('delete', self._delete),
                'delete [<n>] line': Key('%(n)d,d,d') + Function(lambda n: print(f'{n}dd')),
                'wipe': Key('d, d') + Function(lambda: print('dd')),

                # Yank
                **self._make_operator('yank', self._yank),
                'yank [<n>] line': Key('%(n)d,y,y') + Function(lambda n: print(f'{n}yy')),
                'big yank': Key('Y') + Function(lambda: print('Y')),

                # Surround
                'surround with <char>': Key('S,%(char)s') + Function(lambda char: print(f'S{char}')),
                'surround [in] word <char>': Key('y,s,i,w,%(char)s') + Function(lambda char: print(f'ysiw{char}')),
                'surround [in] big word <char>': Key('y,s,i,W,%(char)s') + Function(lambda char: print(f'ysiW{char}')),
                'surround out word <char>': Key('y,s,a,w,%(char)s') + Function(lambda char: print(f'ysaw{char}')),
                'surround out big word <char>': Key('y,s,a,W,%(char)s') + Function(lambda char: print(f'ysaW{char}')),
                'surround in <object> <char>': Key('y,s,i,%(object)s,%(char)s') + Function(lambda object, char: print(f'ysi{object}{char}')),
                'surround line <char>': Key('y,s,s,%(char)s') + Function(lambda char: print(f'yss{char}')),
                'surround change <object> [to] <char>': Key('c,s,%(object)s,%(char)s') + Function(lambda object, char: print(f'cs{object}{char}')),
                'surround delete <char>': Key('d,s,%(char)s') + Function(lambda char: print(f'ds{char}')),

                # Command
                '[<n>] paste': Key('p:%(n)d') + Function(lambda n: print(f'{n}p')),
                '[<n>] back paste': Key('P:%(n)d') + Function(lambda n: print(f'{n}P')),
                '[<n>] repeat': Key('.:%(n)d') + Function(lambda n: print(f'{n}.')),
                '[<n>] slap': Key('o:%(n)d') + Function(lambda n: print(f'{n}o')),
                '[<n>] bump': Key('O:%(n)d') + Function(lambda n: print(f'{n}O')),
                '[<n>] undo': Key('u:%(n)d') + Function(lambda n: print(f'{n}u')),
                '[<n>] redo': Key('c-r:%(n)d') + Function(lambda n: print(f'{n}c-r')),
                '[<n>] slice': Key('x:%(n)d') + Function(lambda n: print(f'{n}x')),
                '[<n>] next': Key('n:%(n)d') + Function(lambda n: print(f'{n}n')),
                'space': Key('i') + Text(' ') + Key('escape') + Function(lambda: print("i ' ' escape")),
                'app': Key('A') + Function(lambda: print('a')),
                'prep': Key('I') + Function(lambda: print('I')),
                '[<n>] star': Key('*:%(n)s') + Function(lambda n: print(f'{n}*')),
                'see ghee next': Key('c,g,n') + Function(lambda: print('cgn')),
                'fuzzy <text>': Key('c-p') + Text('%(text)s') + Function(lambda text: print(f'c-p {text}')),
                'comment': Key('g,c') + Function(lambda: print('gc')),
                'comment line': Key('g,c,c') + Function(lambda: print('gcc')),
                '[<n>] tab': Key('%(n)d,>') + Function(lambda n: print(f'{n}>')),
                '[<n>] tab left': Key('%(n)d,<') + Function(lambda n: print(f'{n}<')),
                'tab start': Key('colon') + Text('left') + Key('enter') + Function(lambda: print(':left enter')),

                # File
                'save': Key('colon,w,enter') + Function(lambda: print(':w enter')),
                'quit': Key('colon,q,enter') + Function(lambda: print(':q enter')),
                'buff': Key('space,b,p') + Function(lambda: print('space,b,p')),
                'next buff': Key('space,b,n') + Function(lambda: print('space,b,n')),

                # Navigation
                'top': Key('g,g') + Function(lambda: print('gg')),
                'bottom': Key('G') + Function(lambda: print('G')),
                'zed zed': Key('z,z') + Function(lambda: print('zz')),
                'zed top': Key('z,t') + Function(lambda: print('zt')),
                'zed bottom': Key('z,b') + Function(lambda: print('zb')),
                '[<n>] pup': Key('c-u:%(n)d') + Function(lambda n: print(f'{n}c-u')),
                '[<n>] pea down': Key('c-d:%(n)d') + Function(lambda n: print(f'{n}c-d')),
                'line <n>': Key('colon') + Text('%(n)d') + Key('enter') + Function(lambda n: print(f':{n} enter')),
                'start': Key('0') + Function(lambda: print('0')),
                'end': Key('$') + Function(lambda: print('$')),
                'run in': Key('c-i') + Function(lambda: print('c-i')),
                'run out': Key('c-o') + Function(lambda: print('c-o')),
            },
            extras=[
                IntegerRef('n', 1, 1000),
                Dictation('text'),
                chars('object'),
                chars('char'),
            ],
            defaults={
                'n': 1,
            }
        )

    def load(self) -> None:
        """
        Load the grammar.

        @unreleased
        """
        self._grammar = Grammar('vim')
        self._grammar.add_rule(self._make_vim_rule())
        self._grammar.load()


vim = Vim()
vim.load()
