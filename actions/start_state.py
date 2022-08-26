from dragonfly import get_engine


def start_state() -> None:
    """
    Start saving adaptation state

    @since 0.1.0
    """
    get_engine().start_saving_adaptation_state()
