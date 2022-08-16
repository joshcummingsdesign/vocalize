from dragonfly import Function
from typing import Callable


def repeatable(n: int, fn: Callable[..., None]) -> None:
    """
    An action that can be repeated n times.

    @unreleased
    """
    action = Function(fn) * n
    action.execute()
