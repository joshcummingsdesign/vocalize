from dragonfly import Grammar, MappingRule, Dictation, FuncContext, Function, get_engine


class SleepWake:
    """
    The sleep / wake grammar class

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance

    @unreleased
    """

    _sleeping: bool = False
    """
    Whether the app is sleeping

    @unreleased
    """

    def _wake(self) -> None:
        """
        Continue listening for commands

        @unreleased
        """
        if self._sleeping:
            self._sleeping = False
            self._grammar.set_exclusiveness(False)
        print('Awake...')

    def _sleep(self) -> None:
        """
        Stop listening for commands

        @unreleased
        """
        if not self._sleeping:
            self._sleeping = True
            self._grammar.set_exclusiveness(True)
        print('Sleeping...')

    def _make_sleep_wake_rule(self) -> MappingRule:
        """
        Sleep / wake rule factory

        @unreleased
        """
        return MappingRule(
            name='sleep_wake_rule',
            mapping={
                'wake up': Function(self._wake) + Function(lambda: get_engine().start_saving_adaptation_state()),
                'sleep': Function(lambda: get_engine().stop_saving_adaptation_state()) + Function(self._sleep),
            }
        )

    def _make_sleeping_rule(self) -> None:
        """
        Sleeping rule factory

        When the app is sleeping, simply return false for all commands

        @unreleased
        """
        return MappingRule(
            name='sleeping_rule',
            mapping={'<text>': Function(lambda: False)},
            extras=[Dictation('text')],
            context=FuncContext(lambda: self._sleeping)
        )

    def load(self) -> None:
        """
        Load the grammar

        @unreleased
        """
        self._grammar = Grammar('sleep_wake')
        self._grammar.add_rule(self._make_sleep_wake_rule())
        self._grammar.add_rule(self._make_sleeping_rule())
        self._grammar.load()
        self._wake()


sleep_wake = SleepWake()
sleep_wake.load()
