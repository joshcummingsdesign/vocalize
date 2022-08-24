from actions import load_grammar
from dragonfly import Grammar, MappingRule, Function


class GrammarLoader:
    """
    The grammar loader grammar class

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance

    @unreleased
    """

    def _make_grammar_loader_rule(self) -> MappingRule:
        """
        Grammar loader rule factory

        @unreleased
        """
        return MappingRule(
            name='grammar_loader_rule',
            mapping={
                'load grammar': Function(load_grammar),
            }
        )

    def load(self) -> None:
        """
        Load the grammar

        @unreleased
        """
        self._grammar = Grammar('grammar_loader')
        self._grammar.add_rule(self._make_grammar_loader_rule())
        self._grammar.load()


grammar_loader = GrammarLoader()
grammar_loader.load()
