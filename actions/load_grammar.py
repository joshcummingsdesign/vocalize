from dragonfly.loader import CommandModuleDirectory
from pathlib import Path
import os.path


def load_grammar() -> None:
    """
    Load all grammars in the `grammar` directory

    Grammar files must start with underscore, i.e. `_my_grammar.py`

    @unreleased
    """
    dirname = Path(__file__).parent.parent.absolute()
    path = os.path.join(dirname, 'grammar')
    directory = CommandModuleDirectory(path)
    directory.unload()
    directory.load()
