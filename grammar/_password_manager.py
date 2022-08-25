from contracts import Grammar
from contracts.rules import Rule, RuleFactory
from dragonfly import MappingRule, Key


class PasswordManager(Grammar):
    """
    Password manager grammar

    @unreleased
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

        @unreleased
        """
        return MappingRule(
            name='password_manager_rule',
            mapping={
                'vault': Key('wa-backslash'),
                'login': Key('down/20,enter'),
                'password': Key('right,up:5,down:2,enter'),
            }
        )


password_manager = PasswordManager()
password_manager.load()


def unload() -> None:
    password_manager.unload()
