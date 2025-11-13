import serial
import time
import pygame
import threading
import os

# --- CONFIGURATION ---
SERIAL_PORT = 'COM9' # COM9 for arduino mega 
BAUD_RATE = 9600
SOUND_FOLDER = 'C:/Users/brand/OneDrive/Documents/Arduino/notes2'  
# ----------------------

pygame.mixer.init()
pygame.mixer.set_num_channels(12)

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)
ser.reset_input_buffer()

print("Listening for Arduino input...")

octave_up = False

sensors_dict = {
    0:'C3', 1:'Cs3', 2:'D3', 3:'Ds3', 4:'E3', 5:'F3',
    6:'Fs3', 7:'G3', 8:'Gs3', 9:'A3', 10:'As3', 11:'B3'
}

octave_up_dict = {
    0:'C4', 1:'Cs4', 2:'D4', 3:'Ds4', 4:'E4', 5:'F4',
    6:'Fs4', 7:'G4', 8:'Gs4', 9:'A4', 10:'As4', 11:'B4'
}

def play_sound(sensor_index, filename):
    if not os.path.exists(filename):
        print(f"[Warning] File not found: {filename}")
        return
    try:
        sound = pygame.mixer.Sound(filename)
        sound.play()
        print(f"{filename} played")
    except Exception as e:
        print(f"Error playing {filename}: {e}")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode(errors='ignore').strip()
            if line.startswith("PIEZO_"):

                sensor_index = int(line.split("_")[1])

                if sensor_index < 12:

                    # if octave_up == False:
                    #     filename = os.path.join(SOUND_FOLDER, f"{sensors_dict[sensor_index]}.mp3")
                    #     print(f"Impact detected on Piezo {sensor_index}")
                    #     threading.Thread(target=play_sound, args=(sensor_index, filename)).start()

                    if octave_up:
                        filename = os.path.join(SOUND_FOLDER, f"{octave_up_dict[sensor_index]}.mp3")
                        print(f"Impact detected on Piezo {sensor_index}")
                        threading.Thread(target=play_sound, args=(sensor_index, filename)).start()
                        time.sleep(0.05)
                    else:
                        filename = os.path.join(SOUND_FOLDER, f"{sensors_dict[sensor_index]}.mp3")
                        print(f"Impact detected on Piezo {sensor_index}")
                        threading.Thread(target=play_sound, args=(sensor_index, filename)).start()

                if sensor_index == 12:

                    # if octave_up == False:
                    #     octave_up = True
                    #     print("Octave up")
                    #     print(f"Impact detected on Piezo {sensor_index}")

                    if octave_up == True:
                        octave_up = False
                        print("Octave down")
                        print(f"Impact detected on Piezo {sensor_index}")
                    else:
                        octave_up = True
                        print("Octave up")
                        print(f"Impact detected on Piezo {sensor_index}")

            time.sleep(0.5)

except KeyboardInterrupt:
    print("\nExiting gracefully...")
    ser.close()
    pygame.mixer.quit()