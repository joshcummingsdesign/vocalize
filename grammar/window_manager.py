from contracts import BaseGrammar
from contracts.rules import Rule, RuleFactory
from dragonfly import MappingRule, Key, IntegerRef


class Grammar(BaseGrammar):
    """
    Window manager grammar

    @unreleased
    """

    @property
    def _name(self) -> str:
        return 'window_manager'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_window_manager_rule,
        ]

    def _make_window_manager_rule(self) -> Rule:
        """
        Window manager rule factory

        @unreleased
        """
        return MappingRule(
            name='window_manager_rule',
            mapping={
                'tile main': Key('as-enter'),
                '[<n>] tile up': Key('as-k/20:%(n)d'),
                '[<n>] tile down': Key('as-j/20:%(n)d'),
                '[<n>] tile left': Key('as-h/20:%(n)d'),
                '[<n>] tile right': Key('as-l/20:%(n)d'),
                'tile hop': Key('cas-h'),
                'tile swap': Key('cas-l'),
                'tile flip': Key('cas-k'),
                'tile flop': Key('cas-j'),
                'tile full': Key('as-d'),
                'tile tall': Key('as-a'),
                'tile column': Key('as-f'),
                'tile wide': Key('as-s'),
                'tile relaunch': Key('cas-z'),
            },
            extras=[
                IntegerRef('n', 1, 10),
            ],
            defaults={
                'n': 1,
            }
        )
