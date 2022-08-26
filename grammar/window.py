from contracts import BaseGrammar
from contracts.rules import Rule, RuleFactory
from dragonfly import MappingRule, Key, Dictation, Text, IntegerRef


class Grammar(BaseGrammar):
    """
    Window grammar

    @unreleased
    """

    @property
    def _name(self) -> str:
        return 'window'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_window_rule,
        ]

    def _make_window_rule(self) -> Rule:
        """
        Window rule factory

        @unreleased
        """
        return MappingRule(
            name='window_rule',
            mapping={
                'kill': Key('w-q'),
                'close window': Key('w-w'),
                'new window': Key('w-n'),
                'new big window': Key('ws-n'),
                'new tab': Key('w-t'),
                'reopen': Key('ws-t'),
                'minimize': Key('w-m'),
                'hide': Key('w-h'),
                'spotlight [<text>]': Key('c-space') + Text('%(text)s'),
                'chrome': Key('c-space') + Text('chrome') + Key('enter'),
                'code': Key('c-space') + Text('code') + Key('enter'),
                'storm': Key('c-space') + Text('storm') + Key('enter'),
                '[<n>] swap': Key('win:down,tab:%(n)d,win:up'),
                '[<n>] switch': Key('w-`:%(n)d'),
                'running': Key('win:down,tab'),

            },
            extras=[
                IntegerRef('n', 1, 10),
                Dictation('text'),
            ],
            defaults={
                'n': 1,
                'text': '',
            }
        )
