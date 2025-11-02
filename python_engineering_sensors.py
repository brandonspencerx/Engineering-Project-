import serial
import time
import pygame
import threading
import os

# --- CONFIGURATION ---
SERIAL_PORT = 'COM8'    # ← Update if needed
BAUD_RATE = 9600
SOUND_FOLDER = 'notes'  # Folder containing MP3/WAV files
# ----------------------

# Initialize pygame mixer (allows multiple simultaneous sounds)
pygame.mixer.init()
pygame.mixer.set_num_channels(12)  # You can increase this for more overlap

# Connect to Arduino
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)
ser.reset_input_buffer()

print("Listening for Arduino input...")

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
                if sensor_index == 0:
                    filename = os.path.join(SOUND_FOLDER, f"a3.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(0, filename), args=(sensor_index,)).start()
                if sensor_index == 1:
                    filename = os.path.join(SOUND_FOLDER, f"b3.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(1,filename), args=(sensor_index,)).start()
                if sensor_index == 2:
                    filename = os.path.join(SOUND_FOLDER, f"c3.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(2,filename), args=(sensor_index,)).start()
                if sensor_index == 3:
                    filename = os.path.join(SOUND_FOLDER, f"d3.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(3,filename), args=(sensor_index,)).start()
                if sensor_index == 4:
                    filename = os.path.join(SOUND_FOLDER, f"e3.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(4,filename), args=(sensor_index,)).start()
                if sensor_index == 5:
                    filename = os.path.join(SOUND_FOLDER, f"f3.mp3")  # Or use indexed files if desired
                    print(f"Impact detected on Piezo {sensor_index}")
                    threading.Thread(target=play_sound(5,filename), args=(sensor_index,)).start()

except KeyboardInterrupt:
    print("\nExiting gracefully...")
    ser.close()
    pygame.mixer.quit()

