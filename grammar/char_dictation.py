from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, FuncContext, Function, Key, Text
from extras import character
from rules import SeriesMappingRule


class Grammar(BaseGrammar):
    """
    Character dictation grammar

    @since 0.1.0
    """

    @property
    def _name(self) -> str:
        return 'char_dictation'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_char_dictation_rule,
            self._make_char_dictation_listening_rule,
        ]

    _enabled: bool = False
    """
    Whether character dictation is enabled

    @since 0.1.0
    """

    def _enable(self) -> None:
        """
        Disable character dictation

        @since 0.1.0
        """
        if not self._enabled:
            self._enabled = True
            self._grammar.set_exclusiveness(True)
        print('Character dictation enabled...')

    def _disable(self) -> None:
        """
        Enable character dictation

        @since 0.1.0
        """
        if self._enabled:
            self._enabled = False
            self._grammar.set_exclusiveness(False)
        print('Character dictation disabled...')

    def _make_char_dictation_rule(self) -> Rule:
        """
        Character dictation rule factory

        @since 0.1.0
        """
        return MappingRule(
            name='char_dictation_rule',
            mapping={
                'char': Function(self._enable),
            }
        )

    def _make_char_dictation_listening_rule(self) -> Rule:
        """
        Character dictation listening rule factory

        @since 0.1.0
        """
        return SeriesMappingRule(
            name='char_dictation_listening_rule',
            mapping={
                '<char>': Text('%(char)s'),
                'hush': Function(self._disable),
                'crush': Function(self._disable) + Key('enter'),
                'flush': Function(self._disable) + Key('escape'),
            },
            extras=[
                character('char'),
            ],
            context=FuncContext(lambda: self._enabled)
        )
