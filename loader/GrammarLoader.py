from contracts import BaseGrammar
from helpers import Singleton
from pathlib import Path
from typing import Optional, TypeAlias
from functools import reduce
from glob import glob
import importlib.util
import os
import sys

GrammarDict: TypeAlias = dict[str, BaseGrammar]
"""
Grammar dict type alias

@unreleased
"""


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

    _instances: Optional[GrammarDict] = None
    """
    The grammar instances as { module_name: instance }

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
        project_root = Path(__file__).parent.parent.absolute()
        grammar_dir = os.path.join(project_root, self._dirname)
        files = glob(os.path.join(grammar_dir, "*.py"))

        def reduce_names(instances: GrammarDict, file: str) -> GrammarDict:
            """
            Reduce file paths to { module_name: instance }

            @unreleased
            """
            if '__' in file:
                return instances

            basename = os.path.basename(file)[:-3]
            module_name = '.'.join([self._dirname, basename])
            spec = importlib.util.spec_from_file_location(module_name, file)
            grammar = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = grammar
            spec.loader.exec_module(grammar)
            instances[module_name] = grammar.Grammar()
            return instances

        self._instances = reduce(reduce_names, files, {})

        for instance in self._instances:
            self._instances[instance].load()

    def reload(self) -> None:
        """
        Reload all grammar instances

        @unreleased
        """
        self.unload()
        self.load()
