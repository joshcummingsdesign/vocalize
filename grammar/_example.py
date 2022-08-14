from dragonfly import Grammar, CompoundRule


class ExampleRule(CompoundRule):
    spec = 'do something computer'

    def _process_recognition(self, node, extras):
        print('Voice command spoken.')


grammar = Grammar('example grammar')
grammar.add_rule(ExampleRule())
grammar.load()
