from abc import ABC, abstractmethod
from dragonfly import Grammar as DragonGrammar, MappingRule
from rules import SeriesMappingRule
from typing import Callable, TypeAlias, Union

Rule: TypeAlias = Union[MappingRule, SeriesMappingRule]
"""
Rule type alias

@since 0.1.0
"""

RuleFactory: TypeAlias = Callable[..., Rule]
"""
Rule factory type alias

@since 0.1.0
"""


class BaseGrammar(ABC):
    """
    Base grammar abstract class

    @since 0.1.0
    """

    _grammar: DragonGrammar = None
    """
    The dragonfly Grammar class instance

    @since 0.1.0
    """

    @abstractmethod
    def _name(self) -> str:
        """
        The grammar name

        @since 0.1.0
        """
        return ''

    @abstractmethod
    def _rules(self) -> list[RuleFactory]:
        """
        A list of rule factories

        @since 0.1.0
        """
        return []

    def __init__(self):
        """
        Instantiate the grammar

        @since 0.1.0
        """
        self._grammar = DragonGrammar(self._name)

    def load(self) -> None:
        """
        Load the grammar

        @since 0.1.0
        """
        for rule in self._rules:
            self._grammar.add_rule(rule())

        self._grammar.load()

    def unload(self) -> None:
        """
        Unload the grammar

        @since 0.1.0
        """
        self._grammar.unload()
