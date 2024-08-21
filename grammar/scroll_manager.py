from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Function

from actions import scroll_on_hum


class Grammar(BaseGrammar):
    """
    Scroll manager grammar

    @since 0.5.1
    """

    @property
    def _name(self) -> str:
        return 'scroll_manager'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_scroll_manager_rule,
        ]

    def _make_scroll_manager_rule(self) -> Rule:
        """
        Scroll manager rule factory

        @since 0.5.1
        """
        return MappingRule(
            name='scroll_manager_rule',
            mapping={
                'enable (scrolling | scroll)': Function(lambda: scroll_on_hum.start()),
                'disable (scrolling | scroll)': Function(lambda: scroll_on_hum.stop()),
            },
        )
