# log_formatter.py
import time

def on_key_press(log_file, key):  # Accept log_file and key as arguments
    try:
        key_name = convert_key_code(str(key))  # You should include this conversion logic
        log_key_press(log_file, key_name)  # Pass both log_file and key_name as arguments

    except Exception as e:
        print("Error writing to file:", e)

# Function to convert key codes to their corresponding names
def convert_key_code(key_code):
    # Your key code conversion logic here
    return key_code

# Function to log key presses
def log_key_press(log_file, key_name):
    try:
        # Open the log file in append mode
        with open(log_file, 'a') as f:
            # Write the timestamp and the key pressed to the file
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {key_name}\n')
    except Exception as e:
        # Print an error message if writing to the file fails
        print("Error writing to file:", e)
