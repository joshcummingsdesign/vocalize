from actions import repeatable_text
from dragonfly import Grammar, Text, Key, IntegerRef, Function, Dictation
from extras import characters
from helpers.string import to_snake, to_camel, to_pascal, to_kebab, to_dot_case, uc_first
from rules import SeriesMappingRule


class InsertMode:
    """
    The InsertMode grammar class

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance

    @unreleased
    """

    def _make_insert_mode_rule(self) -> SeriesMappingRule:
        """
        The insert mode rule factory

        @unreleased
        """
        return SeriesMappingRule(
            name='insert_mode_rule',
            mapping={
                # Modifiers
                'out': Key('escape'),
                '[<n>] slap': Key('enter:%(n)d'),
                '[<n>] tab': Key('tab:%(n)d'),

                # Editing
                '[<n>] del': Key('backspace:%(n)d'),
                '[<n>] slice': Key('right:%(n)d,backspace:%(n)d'),

                # Special Characters
                '[<n>] <char>': Function(lambda n, char: repeatable_text(n, char)),
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
                'dot word <text>': Function(lambda text: Text(to_dot_case(text), True).execute()),
                'upper <text>': Function(lambda text: Text(to_snake(text).upper(), True).execute()),
                'sentence <text>': Function(lambda text: Text(uc_first(text), True).execute()),
                'title <text>': Function(lambda text: Text(text.title(), True).execute()),
            },
            extras=[
                IntegerRef('n', 1, 100),
                Dictation('text'),
                characters('char'),
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
        self._grammar = Grammar('insert_mode')
        self._grammar.add_rule(self._make_insert_mode_rule())
        self._grammar.load()


insertMode = InsertMode()
insertMode.load()
