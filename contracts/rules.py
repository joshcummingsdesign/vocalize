from dragonfly import MappingRule
from rules import SeriesMappingRule
from typing import Callable, TypeAlias, Union

Rule: TypeAlias = Union[MappingRule, SeriesMappingRule]
"""
Rule type alias

@unreleased
"""

RuleFactory: TypeAlias = Callable[..., Rule]
"""
Rule factory type alias

@unreleased
"""
