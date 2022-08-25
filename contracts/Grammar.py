from abc import ABC, abstractproperty
from dragonfly import Grammar as DragonGrammar
from contracts.rules import RuleFactory


class Grammar(ABC):
    """
    Grammar abstract class

    @unreleased
    """

    _grammar: DragonGrammar = None
    """
    The dragonfly Grammar class instance

    @unreleased
    """

    @abstractproperty
    def _name(self) -> str:
        """
        The grammar name

        @unreleased
        """
        return ''

    @abstractproperty
    def _rules(self) -> list[RuleFactory]:
        """
        A list of rule factories

        @unreleased
        """
        return []

    def load(self) -> None:
        """
        Load the grammar

        @unreleased
        """
        self._grammar = DragonGrammar(self._name)

        for rule in self._rules:
            self._grammar.add_rule(rule())

        self._grammar.load()

    def unload(self) -> None:
        """
        Unload the grammar

        @unreleased
        """
        self._grammar.unload()
