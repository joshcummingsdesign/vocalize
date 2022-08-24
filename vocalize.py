from actions import load_grammar
from dragonfly import get_engine
from dragonfly.log import setup_log
from typing import Any


class Vocalize:
    """
    The main Vocalize application class

    @unreleased
    """

    _engine: Any = None
    """
    The speech recognition engine

    @unreleased
    """

    def __init__(self, engine: Any) -> None:
        self._engine = engine

    def listen(self) -> None:
        """
        Start listening for commands

        @unreleased
        """
        setup_log()
        self._engine.connect()
        self._engine.prepare_for_recognition()
        load_grammar()

        try:
            print('Listening...')
            self._engine.do_recognition()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    vocalize = Vocalize(get_engine('kaldi'))
    vocalize.listen()
