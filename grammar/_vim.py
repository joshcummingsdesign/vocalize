from dragonfly import Grammar, MappingRule, Key


class VimRule(MappingRule):
    mapping = {
        'in': Key('i'),
        'out': Key('escape'),
        'slap': Key('o'),
        'wipe': Key('d, d'),
        'save': Key('colon, w, enter'),
        'quit': Key('colon, q, enter'),
    }


grammar = Grammar('vim')
grammar.add_rule(VimRule())
grammar.load()
