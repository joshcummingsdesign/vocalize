from actions import repeat_text
from dragonfly import Grammar, Text, Key, IntegerRef, Function, Dictation
from extras import character, modifiers
from helpers.string import to_snake, to_camel, to_pascal, to_kebab, to_dot_case, uc_first
from rules import SeriesMappingRule


class Keyboard:
    """
    The Keyboard grammar class

    Represents keyboard actions that can be performed anywhere

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance

    @unreleased
    """

    def _make_keyboard_rule(self) -> SeriesMappingRule:
        """
        The keyboard rule factory

        @unreleased
        """
        return SeriesMappingRule(
            name='keyboard',
            mapping={
                # Modifiers
                '[<n>] out': Key('escape:%(n)d'),
                '[<n>] slap': Key('enter:%(n)d'),
                '[<n>] clap': Key('enter:%(n)d,tab'),
                '[<n>] tab': Key('tab:%(n)d'),
                '[<n>] press <mod>': Key('%(mod)s:%(n)d'),

                # Editing
                '[<n>] snip': Key('backspace:%(n)d'),
                'strike': Key('w-backspace'),
                'highlight': Key('w-a'),
                'copy': Key('w-c'),
                'pasta': Key('w-v'),

                # Special Characters
                '[<n>] <char>': Function(lambda n, char: repeat_text(n, char)),
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

                # Typing
                'type <text>': Text('%(text)s'),
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
                IntegerRef('n', 1, 100),
                Dictation('text'),
                character('char'),
                modifiers('mod'),
            ],
            defaults={
                'n': 1,
            }
        )

    def load(self) -> None:
        """
        Load the grammar

        @unreleased
        """
        self._grammar = Grammar('keyboard')
        self._grammar.add_rule(self._make_keyboard_rule())
        self._grammar.load()


keyboard = Keyboard()
keyboard.load()
