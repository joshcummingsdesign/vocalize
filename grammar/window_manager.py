from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Key, IntegerRef


class Grammar(BaseGrammar):
    """
    Window manager grammar

    @since 0.1.0
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

        @since 0.1.0
        """
        return MappingRule(
            name='window_manager_rule',
            mapping={
                'tile left': Key('wa-;'),
                'tile right': Key("wa-'"),
                'tile center': Key('wa-c'),
                'tile next': Key('wa-n'),
                'tile previous': Key('wa-p'),
                'tile full': Key('wa-l'),
                'tile big': Key('wa-a'),
            },
            extras=[
                IntegerRef('n', 1, 10),
            ],
            defaults={
                'n': 1,
            }
        )
