"""
PyAudio Example: Play a wave file (callback version).
Code referenced from PyAudio Documentation.
"""

import pyaudio
import wave
import time
import threading
import sys


# filename = "a.wav"

class AudioPlayer:
    def __init__(self):
        pass

    @staticmethod
    def play_audio_raw(filename):
        wf = wave.open(filename, 'rb')

        # instantiate PyAudio (1)
        p = pyaudio.PyAudio()

        # define callback (2)
        def callback(in_data, frame_count, time_info, status):
            data = wf.readframes(frame_count)
            return data, pyaudio.paContinue

        # open stream using callback (3)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        stream_callback=callback)

        # start the stream (4)
        stream.start_stream()

        # wait for stream to finish (5)
        while stream.is_active():
            time.sleep(0.1)

        # stop stream (6)
        stream.stop_stream()
        stream.close()
        wf.close()

        # close PyAudio (7)
        p.terminate()

    def play_audio(self, filename, block=False):
        t = threading.Thread(target=self.play_audio_raw, args=(filename,))
        t.start()
        if block:
            t.join()
