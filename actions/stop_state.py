from dragonfly import get_engine


def stop_state() -> None:
    """
    Stop saving adaptation state

    @since 0.1.0
    """
    get_engine().stop_saving_adaptation_state()
