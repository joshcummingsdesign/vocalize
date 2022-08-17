from dragonfly import Grammar, MappingRule, Dictation, FuncContext, Function, Text, Key
from extras import characters


class Dictate:
    """
    The dictate grammar class.

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance.

    @unreleased
    """

    _enabled: bool = False
    """
    Whether dictation is enabled.

    @unreleased
    """

    _mac_enabled: bool = False
    """
    Whether macOS dictation is enabled.

    @unreleased
    """

    _char_enabled: bool = False
    """
    Whether character dictation is enabled.

    @unreleased
    """

    def _enable(self) -> None:
        """
        Enable dictation.

        @unreleased
        """
        self._disable()
        self._enabled = True
        self._grammar.set_exclusiveness(True)
        print('Dictation enabled...')

    def _mac_enable(self) -> None:
        """
        Enable macOS dictation.

        @unreleased
        """
        self._disable()
        self._mac_enabled = True
        self._grammar.set_exclusiveness(True)
        print('Mac dictation enabled...')

    def _char_enable(self) -> None:
        """
        Enable character dictation.

        @unreleased
        """
        self._disable()
        self._char_enabled = True
        self._grammar.set_exclusiveness(True)
        print('Character dictation enabled...')

    def _disable(self) -> None:
        """
        Disable dictation.

        @unreleased
        """
        self._enabled = False
        self._mac_enabled = False
        self._char_enabled = False
        self._grammar.set_exclusiveness(False)
        print('Dictation disabled...')

    def _make_enable_dictation_rule(self) -> MappingRule:
        """
        Dictation enable rule factory.

        @unreleased
        """
        return MappingRule(
            name='dictation_enable_rule',
            mapping={
                'dictate': Function(self._enable),
                'mac dictate': Key('cs-d') + Function(self._mac_enable),
                'char dictate': Function(self._char_enable),
            }
        )

    def _make_dictation_listening_rule(self) -> MappingRule:
        """
        Dictation listening rule factory.

        @unreleased
        """
        return MappingRule(
            name='dictation_listening_rule',
            mapping={
                '<text>': Text('%(text)s') + Function(lambda text: print(text)),
                'shush': Function(self._disable),
                'shush out': Key('escape') + Function(self._disable),
            },
            extras=[Dictation('text')],
            context=FuncContext(lambda: self._enabled)
        )

    def _make_mac_dictation_listening_rule(self) -> MappingRule:
        """
        The macOS dictation listening rule factory.

        @unreleased
        """
        return MappingRule(
            name='mac_dictation_listening_rule',
            mapping={
                '<text>': Function(lambda text: print(text)),
                'shush': Key('escape') + Function(self._disable),
            },
            extras=[Dictation('text')],
            context=FuncContext(lambda: self._mac_enabled)
        )

    def _make_char_dictation_listening_rule(self) -> MappingRule:
        """
        The character dictation listening rule factory.

        @unreleased
        """
        return MappingRule(
            name='char_dictation_listening_rule',
            mapping={
                '<char>': Text('%(char)s') + Function(lambda char: print(char)),
                'shush': Function(self._disable),
                'shush out': Key('escape') + Function(self._disable),
            },
            extras=[characters('char')],
            context=FuncContext(lambda: self._char_enabled)
        )

    def load(self) -> None:
        """
        Load the grammar.

        @unreleased
        """
        self._grammar = Grammar('dictate')
        self._grammar.add_rule(self._make_enable_dictation_rule())
        self._grammar.add_rule(self._make_dictation_listening_rule())
        self._grammar.add_rule(self._make_mac_dictation_listening_rule())
        self._grammar.add_rule(self._make_char_dictation_listening_rule())
        self._grammar.load()


dictate = Dictate()
dictate.load()
