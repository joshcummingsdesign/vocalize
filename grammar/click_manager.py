from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Key


class Grammar(BaseGrammar):
    """
    Click manager grammar

    @since 0.5.1
    """

    @property
    def _name(self) -> str:
        return 'click_manager'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_click_manager_rule,
        ]

    def _make_click_manager_rule(self) -> Rule:
        """
        Click manager rule factory

        @since 0.5.1
        """
        return MappingRule(
            name='click_manager_rule',
            mapping={
                'click': Key('cs-space'),
                'mouse': Key('ws-j'),
            },
        )
