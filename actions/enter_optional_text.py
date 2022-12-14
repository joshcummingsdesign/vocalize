from dragonfly import Key, Text
from typing import Optional


def enter_optional_text(text: Optional[str]) -> None:
    """
    Press enter after optional text

    @since 0.1.0
    """
    if text:
        Text(text, True).execute() + Key('enter').execute()
