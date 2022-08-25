from actions import start_state, stop_state
from contracts import Grammar
from contracts.rules import Rule, RuleFactory
from dragonfly import MappingRule, Dictation, FuncContext, Function, Key


class MacDictation(Grammar):
    """
    Mac dictation grammar

    @unreleased
    """

    @property
    def _name(self) -> str:
        return 'mac_dictation'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_mac_dictation_rule,
            self._make_mac_dictation_listening_rule,
        ]

    _enabled: bool = False
    """
    Whether mac dictation is enabled

    @unreleased
    """

    def _enable(self) -> None:
        """
        Disable mac dictation

        @unreleased
        """
        if not self._enabled:
            self._enabled = True
            self._grammar.set_exclusiveness(True)
        print('Mac dictation enabled...')

    def _disable(self) -> None:
        """
        Enable mac dictation

        @unreleased
        """
        if self._enabled:
            self._enabled = False
            self._grammar.set_exclusiveness(False)
        print('Mac dictation disabled...')

    def _make_mac_dictation_rule(self) -> Rule:
        """
        Mac dictation rule factory

        @unreleased
        """
        return MappingRule(
            name='mac_dictation_rule',
            mapping={
                'siri': Key('cs-d') + Function(stop_state) + Function(self._enable),
            }
        )

    def _make_mac_dictation_listening_rule(self) -> Rule:
        """
        Mac dictation listening rule factory

        @unreleased
        """
        return MappingRule(
            name='mac_dictation_listening_rule',
            mapping={
                '<text>': Function(lambda: False),
                'hush': Key('escape') + Function(self._disable) + Function(start_state),
                'crush': Key('escape') + Function(self._disable) + Function(start_state) + Key('enter'),
                'flush': Key('escape') + Function(self._disable) + Function(start_state) + Key('escape'),
            },
            extras=[
                Dictation('text'),
            ],
            context=FuncContext(lambda: self._enabled)
        )


mac_dictation = MacDictation()
mac_dictation.load()


def unload() -> None:
    mac_dictation.unload()
