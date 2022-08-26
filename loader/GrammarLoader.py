from helpers import Singleton
import importlib.util
import sys


@Singleton
class GrammarLoader():
    """
    The grammar loader singleton

    @unreleased
    """

    _instance = None
    """
    The grammar instance

    @unreleased
    """

    def unload(self) -> None:
        """
        Unload the grammar

        @unreleased
        """
        if self._instance:
            self._instance.unload()
            del self._instance
            self.instance = None

    def load(self) -> None:
        """
        Load the grammar

        @unreleased
        """
        # dirname = Path(__file__).parent.parent.absolute()
        # path = os.path.join(dirname, 'grammar')
        # filenames = next(os.walk(path), (None, None, []))[2]
        # filenames = filter(lambda f: '.py' in f and '__' not in f, filenames)
        # for filename in filenames:
        #     file_path = os.path.join(path, filename)
        #     load(file_path)
        # modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
        # foo = [os.path.basename(
        #     f)[:-3] for f in modules if os.path.isfile(f) and not f.endswith('__init__.py')]
        # pprint(sys.modules.keys())

        # directory = CommandModuleDirectory(path)
        # directory.unload()
        # directory.load()
        self.unload()

        spec = importlib.util.spec_from_file_location(
            'grammar.loader', '/Users/josh/Contrib/vocalize/grammar/loader.py')
        grammar = importlib.util.module_from_spec(spec)
        sys.modules['grammar.loader'] = grammar
        spec.loader.exec_module(grammar)

        self._instance = grammar.Grammar()
        self._instance.load()
