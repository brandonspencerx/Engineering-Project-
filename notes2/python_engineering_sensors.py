import serial
import time
import pygame
import threading
import os

# --- CONFIGURATION ---
SERIAL_PORT = 'COM9'    # ← Update if needed
BAUD_RATE = 9600
SOUND_FOLDER = 'C:/Users/brand/OneDrive/Documents/Arduino/notes'  # Folder containing MP3/WAV files
# ----------------------

# Initialize pygame mixer (allows multiple simultaneous sounds)
pygame.mixer.init()
pygame.mixer.set_num_channels(12)  # You can increase this for more overlap

# Connect to Arduino
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)
ser.reset_input_buffer()

print("Listening for Arduino input...")

octave_up = False

def play_sound(sensor_index, filename):
    """Play sound corresponding to the triggered piezo, allowing overlap."""
    if not os.path.exists(filename):
        print(f"[Warning] File not found: {filename}")
        return
    try:
        sound = pygame.mixer.Sound(filename)
        sound.play()  # plays on a new channel (won’t cut off others)
        print(f"{filename} played")
    except Exception as e:
        print(f"Error playing {filename}: {e}")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode(errors='ignore').strip()
            if line.startswith("PIEZO_"):
                sensor_index = int(line.split("_")[1])
                if sensor_index == 0 and octave_up == True:
                    filename = os.path.join(SOUND_FOLDER, f"A.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(0, filename), args=(sensor_index,)).start()
                if sensor_index == 0 and octave_up == False:
                    filename = os.path.join(SOUND_FOLDER, f"A4.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(0, filename), args=(sensor_index,)).start()
                if sensor_index == 1 and octave_up == True:
                    filename = os.path.join(SOUND_FOLDER, f"B.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(1,filename), args=(sensor_index,)).start()
                if sensor_index == 1 and octave_up == False:
                    filename = os.path.join(SOUND_FOLDER, f"B4.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(0, filename), args=(sensor_index,)).start()
                if sensor_index == 2 and octave_up == True:
                    filename = os.path.join(SOUND_FOLDER, f"C.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(2,filename), args=(sensor_index,)).start()
                if sensor_index == 2 and octave_up == False:
                    filename = os.path.join(SOUND_FOLDER, f"C4.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(2,filename), args=(sensor_index,)).start()
                if sensor_index == 3 and octave_up == True:
                    filename = os.path.join(SOUND_FOLDER, f"D.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(3,filename), args=(sensor_index,)).start()
                if sensor_index == 3 and octave_up == False:
                    filename = os.path.join(SOUND_FOLDER, f"D4.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(3,filename), args=(sensor_index,)).start()
                if sensor_index == 4 and octave_up == True:
                    filename = os.path.join(SOUND_FOLDER, f"E.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(4,filename), args=(sensor_index,)).start()
                if sensor_index == 4 and octave_up == False:
                    filename = os.path.join(SOUND_FOLDER, f"E4.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(4,filename), args=(sensor_index,)).start()
                if sensor_index == 5 and octave_up == True:
                    filename = os.path.join(SOUND_FOLDER, f"F.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(5,filename), args=(sensor_index,)).start()
                if sensor_index == 5 and octave_up == False:
                    filename = os.path.join(SOUND_FOLDER, f"F4.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(5,filename), args=(sensor_index,)).start()    
                if sensor_index == 6 and octave_up == True:
                    filename = os.path.join(SOUND_FOLDER, f"G.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(0, filename), args=(sensor_index,)).start()
                if sensor_index == 7 and octave_up == True:
                    filename = os.path.join(SOUND_FOLDER, f"A.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(1,filename), args=(sensor_index,)).start()
                if sensor_index == 8 and octave_up == True:
                    filename = os.path.join(SOUND_FOLDER, f"A.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(2,filename), args=(sensor_index,)).start()
                if sensor_index == 9 and octave_up == True:
                    filename = os.path.join(SOUND_FOLDER, f"A.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(3,filename), args=(sensor_index,)).start()
                if sensor_index == 10 and octave_up == True:
                    filename = os.path.join(SOUND_FOLDER, f"A.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(4,filename), args=(sensor_index,)).start()
                if sensor_index == 11 and octave_up == True:
                    filename = os.path.join(SOUND_FOLDER, f"A.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(4,filename), args=(sensor_index,)).start()
                if sensor_index == 12 and octave_up == False: 
                    octave_up = True
                    print("Octave up)")
                    print(f"Impact detected on Piezo {sensor_index}")
                if sensor_index == 12 and octave_up == True:
                    octave_up = False
                    print("Octave down")
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(5,filename), args=(sensor_index,)).start()


except KeyboardInterrupt:
    print("\nExiting gracefully...")
    ser.close()
    pygame.mixer.quit()

