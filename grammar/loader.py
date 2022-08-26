from actions import load_grammar
from contracts import BaseGrammar
from contracts.rules import Rule, RuleFactory
from dragonfly import MappingRule, Function


class Grammar(BaseGrammar):
    """
    Loader grammar

    @unreleased
    """

    @property
    def _name(self) -> str:
        return 'loader'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_loader_rule,
        ]

    def _foo(self):
        print('goodnight')

    def _make_loader_rule(self) -> Rule:
        """
        Loader rule factory

        @unreleased
        """
        return MappingRule(
            name='loader_rule',
            mapping={
                'load grammar': Function(load_grammar),
                'hello': Function(lambda: self._foo()),
            }
        )
