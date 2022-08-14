from __future__ import print_function
from dragonfly import get_engine
from dragonfly.loader import CommandModuleDirectory
from dragonfly.log import setup_log
import os.path


class Vocalize:
    _engine = None
    _grammar_dir = None

    def __init__(self, engine, grammar_dir='grammar'):
        self._engine = engine
        self._grammar_dir = grammar_dir

    def _load_grammar(self):
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, self._grammar_dir)
        directory = CommandModuleDirectory(path)
        directory.load()

    def _on_begin(self):
        print('Speech start detected.')

    def _on_recognition(self, words):
        message = u'Recognized: %s' % u' '.join(words)
        print(message)

    def _on_failure(self):
        print('Sorry, what was that?')

    def listen(self):
        setup_log()
        self._engine.connect()
        self._engine.prepare_for_recognition()
        self._load_grammar()

        try:
            print('Listening...')
            self._engine.do_recognition(
                self._on_begin, self._on_recognition, self._on_failure)
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    vocalize = Vocalize(get_engine('kaldi'))
    vocalize.listen()
