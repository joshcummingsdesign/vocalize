from actions import load_grammar
from contracts import Grammar
from contracts.rules import Rule, RuleFactoryList
from dragonfly import MappingRule, Function


class Loader(Grammar):
    """
    Loader grammar

    @unreleased
    """

    @property
    def _name(self) -> str:
        return 'loader'

    @property
    def _rules(self) -> RuleFactoryList:
        return [
            self._make_loader_rule,
        ]

    def _make_loader_rule(self) -> Rule:
        """
        Loader rule factory

        @unreleased
        """
        return MappingRule(
            name='loader_rule',
            mapping={
                'load grammar': Function(load_grammar),
            }
        )


loader = Loader()
loader.load()


def unload() -> None:
    loader.unload()
