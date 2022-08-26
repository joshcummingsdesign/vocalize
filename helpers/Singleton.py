from typing import TypeVar, Generic

T = TypeVar('T')


class Singleton(Generic[T]):
    """
    Singleton decorator

    @unreleased
    """

    _decorated: T = None
    """
    The decorated class

    @unreleased
    """

    _instance: T = None
    """
    The one true class instance

    @unreleased
    """

    def __init__(self, decorated: T) -> None:
        """
        Instantiate the singleton class

        @unreleased
        """
        self._decorated = decorated

    def instance(self) -> T:
        """
        Return the one true class instance

        @unreleased
        """
        if self._instance:
            return self._instance
        self._instance = self._decorated()
        return self._instance

    def __call__(self) -> None:
        """
        Prevent class from being instantiated directly

        @unreleased
        """
        raise TypeError('Singletons must be called with instance() method')

    def __instancecheck__(self, instance) -> bool:
        """
        Perform instance checks against the decorated class

        @unreleased
        """
        return isinstance(instance, self._decorated)
