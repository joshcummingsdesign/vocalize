from actions import start_state, stop_state
from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Dictation, FuncContext, Function


class Grammar(BaseGrammar):
    """
    Sleep / wake grammar

    @unreleased
    """

    @property
    def _name(self) -> str:
        return 'sleep_wake'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_sleep_wake_rule,
            self._make_sleeping_rule,
        ]

    _sleeping: bool = False
    """
    Whether the app is sleeping

    @unreleased
    """

    def _sleep(self) -> None:
        """
        Stop listening for commands

        @unreleased
        """
        if not self._sleeping:
            self._sleeping = True
            self._grammar.set_exclusiveness(True)
        print('Sleeping...')

    def _wake(self) -> None:
        """
        Continue listening for commands

        @unreleased
        """
        if self._sleeping:
            self._sleeping = False
            self._grammar.set_exclusiveness(False)
        print('Awake...')

    def _make_sleep_wake_rule(self) -> Rule:
        """
        Sleep / wake rule factory

        @unreleased
        """
        return MappingRule(
            name='sleep_wake_rule',
            mapping={
                'sleep': Function(stop_state) + Function(self._sleep),
            }
        )

    def _make_sleeping_rule(self) -> Rule:
        """
        Sleeping rule factory

        @unreleased
        """
        return MappingRule(
            name='sleeping_rule',
            mapping={
                '<text>': Function(lambda: False),
                'wake up': Function(self._wake) + Function(start_state),
            },
            extras=[
                Dictation('text'),
            ],
            context=FuncContext(lambda: self._sleeping)
        )
