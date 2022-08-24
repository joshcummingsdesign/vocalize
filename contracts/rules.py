from dragonfly import MappingRule
from rules import SeriesMappingRule
from typing import Callable, List, TypeAlias, Union

Rule: TypeAlias = Union[MappingRule, SeriesMappingRule]
RuleFactory: TypeAlias = Callable[..., Rule]
RuleFactoryList: TypeAlias = List[RuleFactory]
