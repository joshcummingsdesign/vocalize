from contracts import Grammar
from contracts.rules import Rule, RuleFactoryList
from dragonfly import MappingRule, Key, Text, IntegerRef, Dictation
from extras import character


class Browser(Grammar):
    """
    Browser grammar

    @unreleased
    """

    @property
    def _name(self) -> str:
        return 'browser'

    @property
    def _rules(self) -> RuleFactoryList:
        return [
            self._make_browser_rule,
        ]

    def _make_browser_rule(self) -> Rule:
        """
        Browser rule factory

        @unreleased
        """
        return MappingRule(
            name='browser_rule',
            mapping={
                'book [<text>]': Key('b') + Text('%(text)s'),
                'book new [<text>]': Key('B') + Text('%(text)s'),
                'open [<text>]': Key('o') + Text('%(text)s'),
                'open new [<text>]': Key('O') + Text('%(text)s'),
                '[<n>] scroll up': Key('u:%(n)d'),
                '[<n>] scroll down': Key('d:%(n)d'),
                'jump': Key('f'),
                'refresh': Key('w-r'),
                'hard refresh': Key('ws-r'),
                'browser search [<object>] [<text>] [<char>]': Key('slash/20') + Text('%(object)s%(text)s%(char)s') + Key('enter'),
                'browser spy': Key('slash'),
                'earl': Key('w-l'),
                'unsafe': Text('thisisunsafe'),
                'close tab': Key('x'),
                '[<n>] previous tab': Key('wa-left:%(n)d'),
                '[<n>] next tab': Key('wa-right:%(n)d'),
                'switch user': Key('ws-m'),
                'nav back': Key('H'),
                'nav forward': Key('L'),
                'dev tools': Key('f12'),
            },
            extras=[
                IntegerRef('n', 1, 10),
                Dictation('text'),
                character('char'),
                character('object'),
            ],
            defaults={
                'n': 1,
                'text': '',
                'char': '',
                'object': '',
            }
        )


browser = Browser()
browser.load()


def unload() -> None:
    browser.unload()
