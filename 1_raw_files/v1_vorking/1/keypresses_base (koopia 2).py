# keypresses_base.py
from pynput import keyboard
import time

def on_key_press(log_file, key):  # Accept log_file as an argument
    try:
        with open(log_file, 'a') as f:
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {key}\n')
    except Exception as e:
        print("Error writing to file:", e)
