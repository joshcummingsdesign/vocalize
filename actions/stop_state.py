from dragonfly import get_engine


def stop_state() -> None:
    """
    Stop saving adaptation state

    @unreleased
    """
    get_engine().stop_saving_adaptation_state()
