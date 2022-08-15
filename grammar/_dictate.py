from dragonfly import Grammar, MappingRule, Dictation, FuncContext, Function, Text, Key


class Dictate:
    _grammar_name = 'dictate'
    _grammar = None
    _enabled = False
    _mac_enabled = False

    def _enable(self):
        if not self._enabled and not self._mac_enabled:
            self._enabled = True
            self._grammar.set_exclusiveness(True)
        print('Dictation enabled...')

    def _mac_enable(self):
        if not self._enabled and not self._mac_enabled:
            self._mac_enabled = True
            self._grammar.set_exclusiveness(True)
        print('Mac dictation enabled...')

    def _disable(self):
        if self._enabled or self._mac_enabled:
            self._enabled = False
            self._mac_enabled = False
            self._grammar.set_exclusiveness(False)
        print('Dictation disabled...')

    def _make_dictation_toggle_rule(self):
        return MappingRule(
            name='dictation_toggle_rule',
            mapping={
                'dictate': Function(self._enable),
                'mac dictate': Key('cs-d') + Function(self._mac_enable),
                'shush': Key('escape,escape') + Function(self._disable),
            }
        )

    def _make_dictation_enabled_rule(self):
        return MappingRule(
            name='dictation_enabled_rule',
            mapping={'<text>': Text('%(text)s') +
                     Function(lambda text: print(text))},
            extras=[Dictation('text')],
            context=FuncContext(lambda: self._enabled)
        )

    def _make_mac_dictation_enabled_rule(self):
        return MappingRule(
            name='mac_dictation_enabled_rule',
            mapping={'<text>': Function(lambda text: print(text))},
            extras=[Dictation('text')],
            context=FuncContext(lambda: self._mac_enabled)
        )

    def load(self):
        self._grammar = Grammar(self._grammar_name)
        self._grammar.add_rule(self._make_dictation_toggle_rule())
        self._grammar.add_rule(self._make_dictation_enabled_rule())
        self._grammar.add_rule(self._make_mac_dictation_enabled_rule())
        self._grammar.load()


dictate = Dictate()
dictate.load()
