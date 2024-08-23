from contracts import BaseGrammar, Rule, RuleFactory
from dragonfly import MappingRule, Key, Text, IntegerRef, Dictation
from rules import SeriesMappingRule


class Grammar(BaseGrammar):
    """
    Browser grammar

    @since 0.1.0
    """

    @property
    def _name(self) -> str:
        return 'browser'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_browser_series_rule,
            self._make_browser_rule,
        ]

    def _make_browser_series_rule(self) -> Rule:
        """
        Browser series rule factory

        @since 0.1.0
        """
        return SeriesMappingRule(
            name='browser_series_rule',
            mapping={
                '[<n>] scroll up': Key('u:%(n)d'),
                '[<n>] scroll down': Key('d:%(n)d'),
                'close tab': Key('x'),
                '[<n>] next tab': Key('wa-right:%(n)d'),
                '[<n>] previous tab': Key('wa-left:%(n)d'),
                'nav back': Key('H'),
                'nav forward': Key('L'),
            },
            extras=[
                IntegerRef('n', 1, 10),
            ],
            defaults={
                'n': 1,
            }
        )

    def _make_browser_rule(self) -> Rule:
        """
        Browser rule factory

        @since 0.1.0
        """
        return MappingRule(
            name='browser_rule',
            mapping={
                'book [<text>]': Key('b') + Text('%(text)s'),
                'book new [<text>]': Key('B') + Text('%(text)s'),
                'open [<text>]': Key('o') + Text('%(text)s'),
                'open new [<text>]': Key('O') + Text('%(text)s'),
                'carbon': Key('y,t'),
                'jump': Key('f'),
                'big jump': Key('F'),
                'refresh': Key('w-r'),
                'hard refresh': Key('ws-r'),
                'earl': Key('w-l'),
                'unsafe': Text('thisisunsafe'),
                'switch user': Key('ws-m/20,enter'),
                'dev tools': Key('f12'),
            },
            extras=[
                Dictation('text'),
            ],
            defaults={
                'text': '',
            }
        )
