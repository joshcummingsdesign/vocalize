from actions import reload_grammar
from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Function


class Grammar(BaseGrammar):
    """
    Loader grammar

    @since 0.1.0
    """

    @property
    def _name(self) -> str:
        return 'loader'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_loader_rule,
        ]

    def _make_loader_rule(self) -> Rule:
        """
        Loader rule factory

        @since 0.1.0
        """
        return MappingRule(
            name='loader_rule',
            mapping={
                'reload grammar': Function(reload_grammar),
            }
        )
