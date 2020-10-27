 # -*- coding: utf-8 -*-
"""
Butchered Coode From here


https://stackoverflow.com/questions/18406570/python-record-audio-on-detected-sound



"""


import pyaudio
import math
import struct
import wave
import time
import os


Threshold = 15

SHORT_NORMALIZE = (1.0/32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2

TIMEOUT_LENGTH = 4


class Recorder:

    @staticmethod
    def rms(frame):
        count = len(frame) / swidth
        format = "%dh" % (count)
        shorts = struct.unpack(format, frame)

        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
            sum_squares += n * n
        rms = math.pow(sum_squares / count, 0.5)
        #print(rms*1000)
        #print('Mic Active:',mic_active)
        
        return rms * 1000

    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=chunk)

    def record(self):
        print('Noise detected, recording beginning')
        
        current = time.time()
        end = time.time() + TIMEOUT_LENGTH

        while current <= end:

            
            data = self.stream.read(chunk)
            if self.rms(data) >= Threshold: end = time.time() + TIMEOUT_LENGTH
                       
            current = time.time()

        print('Returning to listening...')    
        
      

    def listen(self):
        
        print('Listening beginning')
        while True:
                        
            mic_active = 0
            
            input = self.stream.read(chunk)
            rms_val = self.rms(input)
            if rms_val > Threshold:
                
                mic_active = 1
                self.record()

a = Recorder()

a.listen()