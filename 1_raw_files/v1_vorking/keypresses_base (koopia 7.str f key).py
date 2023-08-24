# keypresses_base.py

import time
from pynput import keyboard  # Add this import statement

# Rest of the code remains the same

def format_key(key):
    if hasattr(key, 'char'):
        return key.char
    elif key == keyboard.Key.space:
        return "[SPACE]"
    elif key == keyboard.Key.enter:
        return "[ENTER]"
    elif key == keyboard.Key.ctrl:
        return "[CTRL]"
    else:
        return str(key)

def on_key_press(log_file, key):
    try:
        with open(log_file, 'a') as f:
            formatted_key = format_key(key)
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {formatted_key}\n')
    except Exception as e:
        print("Error writing to file:", e)
