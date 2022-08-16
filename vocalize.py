from dragonfly import get_engine
from dragonfly.loader import CommandModuleDirectory
from dragonfly.log import setup_log
from typing import Optional, Any
import os.path


class Vocalize:
    """
    The main Vocalize application class.

    @unreleased
    """

    _engine: Any = None
    """
    The speech recognition engine.

    @unreleased
    """

    _grammar_dir: Optional[str] = None
    """
    The grammar directory.
    Grammar files must start with underscore, i.e. `_my_grammar.py`.

    @unreleased
    """

    def __init__(self, engine: Any, grammar_dir: str = 'grammar') -> None:
        self._engine = engine
        self._grammar_dir = grammar_dir

    def _load_grammar(self) -> None:
        """
        Load all grammars in the grammar directory.

        @unreleased
        """
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, self._grammar_dir)
        directory = CommandModuleDirectory(path)
        directory.load()

    def listen(self) -> None:
        """
        Start listening for commands.

        @unreleased
        """
        setup_log()
        self._engine.connect()
        self._engine.prepare_for_recognition()
        self._load_grammar()

        try:
            print('Listening...')
            self._engine.do_recognition()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    vocalize = Vocalize(get_engine('kaldi'))
    vocalize.listen()
