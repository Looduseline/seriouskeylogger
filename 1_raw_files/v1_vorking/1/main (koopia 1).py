# main.py

from keypresses_enter import on_key_press  # Import the desired implementation
from pynput import keyboard

def main():
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()
