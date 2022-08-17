from dragonfly import Grammar, Text, IntegerRef, Function
from extras import characters
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

    def _repeatable_text(self, n: int, text: str) -> None:
        word = ''.join(text * n)
        Text(word, True).execute()

    def _make_insert_mode_rule(self) -> SeriesMappingRule:
        """
        The insert mode rule factory

        @unreleased
        """
        return SeriesMappingRule(
            name='insert_mode_rule',
            mapping={
                '[<n>] <char>': Function(lambda n, char: self._repeatable_text(n, char)),
            },
            extras=[
                IntegerRef('n', 1, 100),
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
