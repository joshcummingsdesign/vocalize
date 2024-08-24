from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Key


class Grammar(BaseGrammar):
    """
    Filesystem grammar

    @since 0.1.0
    """

    @property
    def _name(self) -> str:
        return 'filesystem'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_filesystem_rule,
        ]

    def _make_filesystem_rule(self) -> Rule:
        """
        Filesystem rule factory

        @since 0.5.7
        """
        return MappingRule(
            name='scroll_manager_rule',
            mapping={
                'trash': Key('w-backspace'),
                'empty trash': Key('ws-backspace'),
            },
        )
