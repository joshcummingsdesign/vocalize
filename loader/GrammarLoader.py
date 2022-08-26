from helpers import Singleton
from pathlib import Path
from typing import Optional, Any
import functools
import glob
import importlib.util
import os
import sys


@Singleton
class GrammarLoader():
    """
    The grammar loader singleton

    @unreleased
    """

    _dirname: str = 'grammar'
    """
    The grammar directory relative to project root

    @unreleased
    """

    _instances: Optional[dict[str, Any]] = None
    """
    The grammar instances as `{ module_name: instance }`

    @unreleased
    """

    def unload(self) -> None:
        """
        Unload all grammar instances

        @unreleased
        """
        if self._instances:
            for instance in self._instances:
                self._instances[instance].unload()
            self._instances = None

    def load(self) -> None:
        """
        Load all grammar instances

        @unreleased
        """
        path = os.path.join(
            Path(__file__).parent.parent.absolute(), self._dirname)
        files = glob.glob(os.path.join(path, "*.py"))

        def reduce_names(acc, val):
            """
            Reduce the file names to { module_name: instance }

            @unreleased
            """
            if '__' in val:
                return acc
            module_name = '.'.join([self._dirname, os.path.basename(val)[:-3]])
            spec = importlib.util.spec_from_file_location(module_name, val)
            grammar = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = grammar
            spec.loader.exec_module(grammar)
            acc[module_name] = grammar.Grammar()
            return acc

        self._instances = functools.reduce(reduce_names, files, {})

        for instance in self._instances:
            self._instances[instance].load()

    def reload(self) -> None:
        """
        Reload all grammar instances

        @unreleased
        """
        self.unload()
        self.load()
