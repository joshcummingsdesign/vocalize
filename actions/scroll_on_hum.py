import queue
import numpy as np
import sounddevice as sd
from dragonfly import get_engine, Key
from typing import Any

buffer_queue = queue.Queue()
timers = dict()


def audio_callback(block, frames, time, status) -> None:
    """
    The audio input stream callback.

    @since 0.5.1
    """
    # Push the incoming audio data (block) to the buffer queue
    buffer_queue.put(block, block=False)


# Initialize the audio input stream
stream = sd.InputStream(callback=audio_callback)


def read_block() -> Any:
    """
    Read the most recent block from the buffer queue.

    @since 0.5.1

    :returns: The most recent block from the buffer queue.
    """
    block = None
    while not buffer_queue.empty():
        try:
            block = buffer_queue.get_nowait()
        except queue.Empty:
            block = None
    return block


def process_block(block: Any) -> None:
    """
    Process a block.

    @since 0.5.1

    :param block: The block to process.
    """
    vol = np.linalg.norm(block) * 10
    if (vol > 0.75 and vol < 1.75):
        Key('j').execute()


def process_audio() -> None:
    """
    Read and process the most recent block from the buffer queue.

    @since 0.5.1
    """
    block = read_block()
    if block is not None:
        process_block(block)


def start() -> Any:
    """
    Start scrolling on hum.

    @since 0.5.1

    :returns: The timer.
    """
    print('Scrolling enabled...')
    stream.start()
    timer = get_engine().create_timer(process_audio, 0.02)
    timers['scroll'] = timer
    return timer


def stop() -> Any:
    """
    Stop scrolling on hum.

    @since 0.5.1

    :returns: The timer.
    """
    print('Scrolling disabled...')
    stream.stop()

    if 'scroll' not in timers:
        return None

    timer = timers.pop('scroll')
    timer.stop()

    return timer
