from abc import ABC, abstractproperty
from dragonfly import Grammar as DragonGrammar
from contracts.rules import RuleFactory


class BaseGrammar(ABC):
    """
    Base grammar abstract class

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

    def __init__(self):
        """
        Instantiate the grammar

        @unreleased
        """
        self._grammar = DragonGrammar(self._name)

    def load(self) -> None:
        """
        Load the grammar

        @unreleased
        """
        for rule in self._rules:
            self._grammar.add_rule(rule())

        self._grammar.load()

    def unload(self) -> None:
        """
        Unload the grammar

        @unreleased
        """
        self._grammar.unload()
