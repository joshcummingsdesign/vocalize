from dragonfly import CompoundRule, MappingRule, RuleRef, Repetition
from typing import Any


class SeriesMappingRule(CompoundRule):
    """
    A mapping rule which allows for commands to be said in a series

    @undefined
    """

    def __init__(
        self,
        name: str,
        mapping: dict[str, Any],
        extras: list[Any] = None,
        defaults: dict[str, Any] = None,
        context: Any = None
    ) -> None:
        mapping_rule = MappingRule(
            name=name,
            mapping=mapping,
            extras=extras,
            defaults=defaults,
            exported=False,
            context=context
        )
        single = RuleRef(rule=mapping_rule)
        series = Repetition(single, min=1, max=16, name='series')
        compound_spec = '<series>'
        compound_extras = [series]

        CompoundRule.__init__(
            self,
            spec=compound_spec,
            extras=compound_extras,
            exported=True
        )

    def _process_recognition(self, node: Any, extras: dict[str, Any]) -> None:
        series = extras['series']
        for action in series:
            action.execute()
