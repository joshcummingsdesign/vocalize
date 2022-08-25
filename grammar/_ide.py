from contracts import Grammar
from contracts.rules import Rule, RuleFactory
from dragonfly import MappingRule, Key


class Ide(Grammar):
    """
    IDE grammar

    @unreleased
    """

    @property
    def _name(self) -> str:
        return 'ide'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_ide_rule,
        ]

    def _make_ide_rule(self) -> Rule:
        """
        IDE rule factory

        @unreleased
        """
        return MappingRule(
            name='ide_rule',
            mapping={
                'find all': Key('ws-f'),
                'reveal': Key('wa-f11'),
                'git changes': Key('ws-g'),
                'new file': Key('c-n'),
            }
        )


ide = Ide()
ide.load()


def unload() -> None:
    ide.unload()
