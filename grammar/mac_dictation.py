from actions import start_state, stop_state
from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Dictation, FuncContext, Function, Key


class Grammar(BaseGrammar):
    """
    Mac dictation grammar

    @since 0.1.0
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

    @since 0.1.0
    """

    def _enable(self) -> None:
        """
        Disable mac dictation

        @since 0.1.0
        """
        if not self._enabled:
            self._enabled = True
            self._grammar.set_exclusiveness(True)
        print('Mac dictation enabled...')

    def _disable(self) -> None:
        """
        Enable mac dictation

        @since 0.1.0
        """
        if self._enabled:
            self._enabled = False
            self._grammar.set_exclusiveness(False)
        print('Mac dictation disabled...')

    def _make_mac_dictation_rule(self) -> Rule:
        """
        Mac dictation rule factory

        @since 0.1.0
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

        @since 0.1.0
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
