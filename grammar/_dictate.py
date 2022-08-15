from dragonfly import Grammar, MappingRule, Dictation, Text


class DictateRule(MappingRule):
    mapping = {
        'dictate <text>': Text('%(text)s'),
    }

    extras = [
        Dictation('text'),
    ]


grammar = Grammar('dictate')
grammar.add_rule(DictateRule())
grammar.load()
