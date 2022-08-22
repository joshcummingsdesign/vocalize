from dragonfly import Grammar, MappingRule, Key, Text, IntegerRef, Dictation
from extras import character


class Browser:
    """
    The browser grammar class

    @unreleased
    """

    _grammar: Grammar = None
    """
    The Grammar class instance

    @unreleased
    """

    def _make_browser_rule(self) -> MappingRule:
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
                'earl': Key('w-l'),
                'close tab': Key('x'),
                'previous tab': Key('s-j'),
                'next tab': Key('s-k'),
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

    def load(self) -> None:
        """
        Load the grammar

        @unreleased
        """
        self._grammar = Grammar('browser')
        self._grammar.add_rule(self._make_browser_rule())
        self._grammar.load()


browser = Browser()
browser.load()
