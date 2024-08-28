import queue
import numpy as np
import sounddevice as sd
from dragonfly import get_engine, Key
from typing import Any, Callable

# Initialize the buffer queue and timers
buffer_queue = queue.Queue()
timers = dict()

# Parameters
scroll_action = Key('j').execute
hum_freq_range = (200, 300)
hum_vol_threshold = 0.3


def audio_callback(block, frames, time, status) -> None:
    """
    The audio input stream callback.

    @since 0.5.1
    """
    # Push the incoming audio data (block) to the buffer queue
    buffer_queue.put(block.copy(), block=False)


# Initialize the audio input stream
stream = sd.InputStream(callback=audio_callback)


def read_block() -> Any | None:
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


def process_block(block: Any, action: Callable) -> None:
    """
    Process a block.

    @since 0.5.1

    :param block: The block to process.
    :param Callable action: The action to perform when the block is processed.
    """
    # Flatten the audio data (if stereo, select one channel)
    audio_block = block.flatten()

    # Use the Euclidean norm to get the block's volume
    vol = np.linalg.norm(audio_block) * 10

    # Perform a Fast Fourier Transform (FFT) to analyze the block's frequency content
    N = len(audio_block)
    fft_spectrum = np.fft.fft(audio_block)
    freqs = np.fft.fftfreq(N, 1/stream.samplerate)

    # Consider only the positive frequencies
    freqs = freqs[:N//2]
    fft_spectrum = np.abs(fft_spectrum[:N//2])

    # Get the dominant frequency of the block
    dominant_frequency = freqs[np.argmax(fft_spectrum)]

    # Determine if the block is in the hum range
    if (
        vol > hum_vol_threshold
        and dominant_frequency > hum_freq_range[0]
        and dominant_frequency < hum_freq_range[1]
    ):
        action()


def process_audio(action: Callable) -> None:
    """
    Read and process the most recent block from the buffer queue.

    @since 0.5.1

    :param Callable action: The action to perform when the block is processed.
    """
    def callback():
        block = read_block()
        if block is not None:
            process_block(block, action)
    return callback


def start() -> Any:
    """
    Start scrolling on hum.

    @since 0.5.1

    :returns: The timer.
    """
    print('Scrolling enabled...')
    stream.start()
    timer = get_engine().create_timer(process_audio(scroll_action), 0.02)
    timers['scroll'] = timer
    return timer


def stop() -> Any | None:
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
