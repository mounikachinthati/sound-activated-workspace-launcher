import pyaudio
import numpy as np
import time
import os
import webbrowser


THRESHOLD = 8000       # How loud a sound needs to be to register as a "clap". Adjust if it's too sensitive or not sensitive enough.
MIN_DELAY = 0.2        # Minimum seconds between claps to avoid echoing registering as a second clap.
MAX_DELAY = 1.0        # Maximum seconds between claps. If you wait longer, it resets.

CHUNK = 1024           # Number of audio frames per buffer
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Listening for double claps... (Press Ctrl+C to stop)")

last_sound_time = 0
sound_count = 0

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16)
        
        peak = np.abs(audio_data).max()
        if peak > THRESHOLD:
            current_time = time.time()
            time_since_last_sound = current_time - last_sound_time

            if time_since_last_sound > MIN_DELAY:
                if time_since_last_sound < MAX_DELAY:
                    sound_count += 1
                else:
                    sound_count = 1
                
                last_sound_time = current_time
                print(f"sound detected! (Count: {sound_count})")

                if sound_count == 2:
                    print("Double sound confirmed! Initiating Workspace Protocol...")
                    

                    # Add Tasks Here 

                    time.sleep(2) 
                    
                    # Like here i am opening chrome and the link to directly open my youtube channel
                    
                    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")                    
                    sound_count = 0
                    
                    print("Workspace active. Pausing JARVIS microphone so music doesn't trigger it...")
                    
                    time.sleep(14400)

except KeyboardInterrupt:
    print("\nShutting down JARVIS audio system...")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()