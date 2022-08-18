from dragonfly import Grammar, MappingRule, Key


class PasswordManager:
    """
    The password manager grammar class

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance

    @unreleased
    """

    def _make_password_manager_rule(self) -> MappingRule:
        """
        Password manager rule factory

        @unreleased
        """
        return MappingRule(
            name='password_manager_rule',
            mapping={
                'vault': Key('wa-backslash'),
            }
        )

    def load(self) -> None:
        """
        Load the grammar

        @unreleased
        """
        self._grammar = Grammar('password_manager')
        self._grammar.add_rule(self._make_password_manager_rule())
        self._grammar.load()


password_manager = PasswordManager()
password_manager.load()
