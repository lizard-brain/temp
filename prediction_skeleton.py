# Prediction Script

def prediction_live_emotion():
    
    RECORD_SECONDS = 5
    MY_BLOCK_SIZE = RATE * RECORD_SECONDS
    time.sleep(RECORD_SECONDS) #let it get atleat RECORD_SECONDS
    while(True):
        
        
        time.sleep(1) # ML Prediction        
        
        print ("prediction: ")       
        
try:
    audio_data_list=[]
    def callback(input_data, frame_count, time_info, flags):
        audio_data_list.extend(np.fromstring(input_data, dtype=np.float32) )
        return input_data, pyaudio.paContinue

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        stream_callback=callback,
                        frames_per_buffer=CHUNK)

    prediction_live_emotion()
except:
    print ("\n\nNOW CLOSING\n\n")
finally:
    print ("\n\nFREEING ALL RESOURCES\n\n")
    stream.stop_stream()
    stream.close()
    audio.terminate()
