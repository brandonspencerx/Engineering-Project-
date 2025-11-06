import serial
import time
import pygame
import threading
import os

# --- CONFIGURATION ---
SERIAL_PORT = 'COM9' # COM9 for arduino mega 
BAUD_RATE = 9600
SOUND_FOLDER = 'C:/Users/brand/OneDrive/Documents/Arduino/notes'  
# ----------------------

# Initialize pygame mixer (allows multiple simultaneous sounds)

pygame.mixer.init()
pygame.mixer.set_num_channels(12)  # increase this for more overlap

# Connect to Arduino
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)
ser.reset_input_buffer()

print("Listening for Arduino input...")

octave_up = False

sensors_dict = { # maps each sensor to a note
                0:'A', 
                1:'As',
                2:'B',
                3:'C',
                4:'Cs',
                5:'D',
                6:'Ds',
                7:'E',
                8:'F',
                9:'Fs',
                10:'G',
                11:'Gs',
                }

octave_up_dict = { # octave up versions for each sensor
                0:'A4', 
                1:'As4',
                2:'B4',
                3:'C4',
                4:'Cs4',
                5:'D4',
                6:'Ds4',
                7:'E4',
                8:'F4',
                9:'Fs4',
                10:'G4',
                11:'Gs4'
                }

# play sound corresponding to the triggered piezo, allowing overlap.
def play_sound(sensor_index, filename):
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

                if sensor_index < 12: # sensors 0 - 11 for notes

                    if octave_up == False:
                        filename = os.path.join(SOUND_FOLDER, f"{sensors_dict[sensor_index]}" + ".mp3")  
                        print(f"Impact detected on Piezo {sensor_index}")
                        threading.Thread(target=play_sound(0, filename), args=(sensor_index,)).start()

                    if octave_up == True:
                        filename = os.path.join(SOUND_FOLDER, f"{octave_up_dict[sensor_index]}" + ".mp3")  
                        print(f"Impact detected on Piezo {sensor_index}")
                        threading.Thread(target=play_sound(0, filename), args=(sensor_index,)).start()

                if sensor_index == 12: # sensor 12 for octave switch

                    if octave_up == False: 
                        octave_up = True
                        print("Octave up)")
                        print(f"Impact detected on Piezo {sensor_index}")

                    if sensor_index == 12 and octave_up == True:
                        octave_up = False
                        print("Octave down")
                        print(f"Impact detected on Piezo {sensor_index}")

except KeyboardInterrupt:
    print("\nExiting gracefully...")
    ser.close()
    pygame.mixer.quit()