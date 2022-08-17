from dragonfly import Grammar, Key, IntegerRef, Text, Dictation
from rules import SeriesMappingRule


class Vim:
    """
    The Vim grammar class

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance

    @unreleased
    """

    def _make_vim_rule(self) -> SeriesMappingRule:
        """
        The keyboard rule factory

        @unreleased
        """
        return SeriesMappingRule(
            name='keyboard',
            mapping={
                # Modes
                'insert': Key('i'),

                # Editing
                '[<n>] undo': Key('escape,u:%(n)d'),
                '[<n>] redo': Key('escape,c-r:%(n)d'),

                # Navigation
                'search <text>': Key('escape') + Text('/%(text)s') + Key('enter'),
                'back search <text>': Key('escape') + Text('?%(text)s') + Key('enter'),
                'next': Key('n'),
            },
            extras=[
                IntegerRef('n', 1, 1000),
                Dictation('text'),
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
        self._grammar = Grammar('vim')
        self._grammar.add_rule(self._make_vim_rule())
        self._grammar.load()


vim = Vim()
vim.load()
