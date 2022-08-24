from contracts import Grammar
from contracts.rules import Rule, RuleFactoryList
from dragonfly import MappingRule, Key, IntegerRef


class Clipboard(Grammar):
    """
    Clipboard grammar

    @unreleased
    """

    @property
    def _name(self) -> str:
        return 'clipboard'

    @property
    def _rules(self) -> RuleFactoryList:
        return [
            self._make_clipboard_rule,
        ]

    def _make_clipboard_rule(self) -> Rule:
        """
        Clipboard rule factory

        @unreleased
        """
        return MappingRule(
            name='clipboard_rule',
            mapping={
                'clip': Key('ws-space'),
                'clip <i>': Key('w-%(i)d'),
            },
            extras=[
                IntegerRef('i', 0, 9),
            ]
        )


clipboard = Clipboard()
clipboard.load()


def unload() -> None:
    clipboard.unload()
