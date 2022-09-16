from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Key


class Grammar(BaseGrammar):
    """
    IDE grammar

    @since 0.1.0
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

        @since 0.1.0
        """
        return MappingRule(
            name='ide_rule',
            mapping={
                'find in': Key('w-f'),
                'find all': Key('ws-f'),
                'reveal': Key('wa-f11'),
                'git changes': Key('ws-g'),
                'new file': Key('c-n'),
                'factor': Key('c-t'),
            }
        )
