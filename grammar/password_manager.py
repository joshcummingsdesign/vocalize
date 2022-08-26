from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Key


class Grammar(BaseGrammar):
    """
    Password manager grammar

    @since 0.1.0
    """

    @property
    def _name(self) -> str:
        return 'password_manager'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_password_manager_rule,
        ]

    def _make_password_manager_rule(self) -> Rule:
        """
        Password manager rule factory

        @since 0.1.0
        """
        return MappingRule(
            name='password_manager_rule',
            mapping={
                'vault': Key('wa-backslash'),
                'login': Key('down/20,enter'),
                'password': Key('right,up:5,down:2,enter'),
            }
        )
