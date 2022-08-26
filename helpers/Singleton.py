from typing import TypeVar, Generic

T = TypeVar('T')


class Singleton(Generic[T]):
    """
    Singleton decorator

    @since 0.1.0
    """

    _decorated: T = None
    """
    The decorated class

    @since 0.1.0
    """

    _instance: T = None
    """
    The one true class instance

    @since 0.1.0
    """

    def __init__(self, decorated: T) -> None:
        """
        Instantiate the singleton class

        @since 0.1.0
        """
        self._decorated = decorated

    def instance(self) -> T:
        """
        Return the one true class instance

        @since 0.1.0
        """
        if self._instance:
            return self._instance
        self._instance = self._decorated()
        return self._instance

    def __call__(self) -> None:
        """
        Prevent class from being instantiated directly

        @since 0.1.0
        """
        raise TypeError('Singletons must be called with instance() method')

    def __instancecheck__(self, instance) -> bool:
        """
        Perform instance checks against the decorated class

        @since 0.1.0
        """
        return isinstance(instance, self._decorated)
