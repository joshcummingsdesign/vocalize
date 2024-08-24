from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Key, Dictation, Text, IntegerRef


class Grammar(BaseGrammar):
    """
    Window grammar

    @since 0.1.0
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

        @since 0.1.0
        """
        return MappingRule(
            name='window_rule',
            mapping={
                'kill': Key('w-q'),
                'close': Key('w-w'),
                'new window': Key('w-n'),
                'new big window': Key('ws-n'),
                'new tab': Key('w-t'),
                'reopen': Key('ws-t'),
                'minimize': Key('w-m'),
                'hide': Key('w-h'),
                'spotlight [<text>]': Key('w-space') + Text('%(text)s'),
                'chrome': Key('w-space') + Text('chrome') + Key('enter'),
                'messages': Key('w-space') + Text('messages') + Key('enter'),
                'code': Key('w-space') + Text('code') + Key('enter'),
                '[<n>] swap': Key('win:down,tab:%(n)d,win:up'),
                '[<n>] switch': Key('w-`:%(n)d'),
                'running': Key('win:down,tab'),
                'dot files': Key('ws-.'),
                'trash': Key('w-backspace'),
                'empty trash': Key('ws-backspace'),
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
