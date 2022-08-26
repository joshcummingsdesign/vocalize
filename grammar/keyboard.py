from actions import repeat_text
from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import IntegerRef, Function
from extras import character
from rules import SeriesMappingRule


class Grammar(BaseGrammar):
    """
    Keyboard grammar

    @unreleased
    """

    @property
    def _name(self) -> str:
        return 'keyboard'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_keyboard_rule,
        ]

    def _make_keyboard_rule(self) -> Rule:
        """
        Keyboard rule factory

        @unreleased
        """
        return SeriesMappingRule(
            name='keyboard',
            mapping={
                # Special Characters
                '[<n>] <char>': Function(lambda n, char: repeat_text(n, char)),
            },
            extras=[
                IntegerRef('n', 1, 100),
                character('char'),
            ],
            defaults={
                'n': 1,
            }
        )
