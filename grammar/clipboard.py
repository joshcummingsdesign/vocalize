from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Key, IntegerRef


class Grammar(BaseGrammar):
    """
    Clipboard grammar

    @since 0.1.0
    """

    @property
    def _name(self) -> str:
        return 'clipboard'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_clipboard_rule,
        ]

    def _make_clipboard_rule(self) -> Rule:
        """
        Clipboard rule factory

        @since 0.1.0
        """
        return MappingRule(
            name='clipboard_rule',
            mapping={
                'clip': Key('c-space'),
                'clip <i>': Key('w-%(i)d'),
            },
            extras=[
                IntegerRef('i', 0, 9),
            ]
        )
