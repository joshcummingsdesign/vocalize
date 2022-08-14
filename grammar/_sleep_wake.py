from dragonfly import Grammar, MappingRule, Dictation, FuncContext, Function, get_engine


class SleepWake:
    _grammar_name = 'sleep wake'
    _grammar = None
    _sleeping = False

    def _wake(self, force=False):
        if self._sleeping or force:
            self._sleeping = False
            self._grammar.set_exclusiveness(False)
        print('Awake...')

    def _sleep(self, force=False):
        if not self._sleeping or force:
            self._sleeping = True
            self._grammar.set_exclusiveness(True)
        print('Sleeping...')

    def _make_sleep_wake_rule(self):
        return MappingRule(
            name='sleep_wake_rule',
            mapping={
                'wake': Function(self._wake) + Function(lambda: get_engine().start_saving_adaptation_state()),
                'sleep': Function(lambda: get_engine().stop_saving_adaptation_state()) + Function(self._sleep),
            }
        )

    def _make_sleeping_rule(self):
        return MappingRule(
            name='sleeping_rule',
            mapping={'<text>': Function(lambda text: False and print(text))},
            extras=[Dictation('text')],
            context=FuncContext(lambda: self._sleeping),
        )

    def load(self):
        self._grammar = Grammar(self._grammar_name)
        self._grammar.add_rule(self._make_sleep_wake_rule())
        self._grammar.add_rule(self._make_sleeping_rule())
        self._grammar.load()
        self._wake(force=True)


sleep_wake = SleepWake()
sleep_wake.load()
