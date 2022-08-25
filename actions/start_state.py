from dragonfly import get_engine


def start_state() -> None:
    """
    Start saving adaptation state

    @unreleased
    """
    get_engine().start_saving_adaptation_state()
