from contracts import Grammar
from contracts.rules import Rule, RuleFactoryList
from dragonfly import MappingRule, FuncContext, Function, Key, Text
from extras import character
from rules import SeriesMappingRule


class CharDictation(Grammar):
    """
    Character dictation grammar

    @unreleased
    """

    @property
    def _name(self) -> str:
        return 'char_dictation'

    @property
    def _rules(self) -> RuleFactoryList:
        return [
            self._make_char_dictation_rule,
            self._make_char_dictation_listening_rule,
        ]

    _enabled: bool = False
    """
    Whether character dictation is enabled

    @unreleased
    """

    def _enable(self) -> None:
        """
        Disable character dictation

        @unreleased
        """
        if not self._enabled:
            self._enabled = True
            self._grammar.set_exclusiveness(True)
        print('Character dictation enabled...')

    def _disable(self) -> None:
        """
        Enable character dictation

        @unreleased
        """
        if self._enabled:
            self._enabled = False
            self._grammar.set_exclusiveness(False)
        print('Character dictation disabled...')

    def _make_char_dictation_rule(self) -> Rule:
        """
        Character dictation rule factory

        @unreleased
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

        @unreleased
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


char_dictation = CharDictation()
char_dictation.load()


def unload() -> None:
    char_dictation.unload()
