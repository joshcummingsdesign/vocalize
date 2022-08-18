from dragonfly import Grammar, MappingRule, Key


class Ide:
    """
    The IDE grammar class

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance

    @unreleased
    """

    def _make_ide_rule(self) -> MappingRule:
        """
        IDE rule factory

        @unreleased
        """
        return MappingRule(
            name='ide_rule',
            mapping={
                'find all': Key('ws-f'),
                'reveal': Key('wa-f11'),
            }
        )

    def load(self) -> None:
        """
        Load the grammar

        @unreleased
        """
        self._grammar = Grammar('ide')
        self._grammar.add_rule(self._make_ide_rule())
        self._grammar.load()


ide = Ide()
ide.load()
