from actions import repeat_text
from contracts import Grammar
from contracts.rules import Rule, RuleFactory
from dragonfly import Text, Key, IntegerRef, Function, Dictation
from extras import character, modifiers
from helpers.string import to_snake, to_camel, to_pascal, to_kebab, to_dot_case, uc_first
from rules import SeriesMappingRule


class Keyboard(Grammar):
    """
    Keyboard grammar

    @unreleased
    """

    @property
    def _name(self) -> str:
        return 'keyboard'

    @property
    def _rules(self) -> list[RuleFactory]:
        return [
            self._make_keyboard_rule,
        ]

    def _make_keyboard_rule(self) -> Rule:
        """
        Keyboard rule factory

        @unreleased
        """
        return SeriesMappingRule(
            name='keyboard',
            mapping={
                # Modifiers
                '[<n>] axe': Key('win:up,escape:%(n)d'),
                '[<n>] enter': Key('win:up,enter:%(n)d'),
                '[<n>] clap': Key('enter:%(n)d,tab'),
                '[<n>] tab': Key('tab:%(n)d'),
                '[<n>] back tab': Key('s-tab:%(n)d'),
                '[<n>] press <mod>': Key('%(mod)s:%(n)d'),

                # Editing
                '[<n>] snip': Key('backspace:%(n)d'),
                '[<n>] strike': Key('w-backspace:%(n)d'),
                'strike all': Key('w-up,w-left,ws-down,backspace'),
                'light all': Key('w-a'),
                'light up': Key('ws-up'),
                'light down': Key('ws-down'),
                'light <n> down': Key('shift:down,down:%(n)d,shift:up'),
                'light left': Key('ws-left'),
                'light right': Key('ws-right'),
                'big up': Key('w-up'),
                'big down': Key('w-down'),
                'big left': Key('w-left'),
                'big right': Key('w-right'),
                'copy': Key('w-c'),
                'pasta': Key('w-v'),
                'begin': Key('w-left'),
                '[<n>] oops': Key('w-z:%(n)d'),
                '[<n>] never mind': Key('ws-z:%(n)d'),
                'duplicate': Key('w-d'),
                'bold': Key('w-b'),

                # Special Characters
                '[<n>] <char>': Function(lambda n, char: repeat_text(n, char)),
                'pad <char>': Text(' %(char)s '),
                'angles': Key('<,>,left'),
                'spread': Text('...'),
                'arrow': Text('->'),
                'lambda': Text('=>'),
                'double equals': Text(' == '),
                'triple equals': Text(' === '),
                'loose not equals': Text(' != '),
                'not equals': Text(' !== '),
                'greater equals': Text(' >= '),
                'less equals': Text(' <= '),

                # Typing
                'type <text>': Text('%(text)s'),
                'sass <text>': Function(lambda text: Text(to_kebab(text), True).execute()) + Key('colon,space,semicolon,left'),
                'php echo': Key('<,?,=,space,?,>,left,left,left,space'),
                'tag <text>': Text('<') + Function(lambda text: Text(to_kebab(text), True).execute()) + Key('>'),
                'tag dev': Text('<div>'),
                'num <n>': Text('%(n)s'),
                'key <text>': Text('%(text)s '),
                'snake <text>': Function(lambda text: Text(to_snake(text), True).execute()),
                'camel <text>': Function(lambda text: Text(to_camel(text), True).execute()),
                'pascal <text>': Function(lambda text: Text(to_pascal(text), True).execute()),
                'kebab <text>': Function(lambda text: Text(to_kebab(text), True).execute()),
                'dot case <text>': Function(lambda text: Text(to_dot_case(text), True).execute()),
                'upper snake <text>': Function(lambda text: Text(to_snake(text).upper(), True).execute()),
                'upper <text>': Function(lambda text: Text(text.upper(), True).execute()),
                'sentence <text>': Function(lambda text: Text(uc_first(text), True).execute()),
                'title <text>': Function(lambda text: Text(text.title(), True).execute()),
            },
            extras=[
                IntegerRef('n', 1, 100),
                Dictation('text'),
                character('char'),
                modifiers('mod'),
            ],
            defaults={
                'n': 1,
            }
        )


keyboard = Keyboard()
keyboard.load()


def unload() -> None:
    keyboard.unload()
