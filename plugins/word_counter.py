# plugins/word_counter.py

from log_formatter import log_key_press  # Import the log_key_press function

word_count = 0

def count_words(log_file, key):
    global word_count
    if key == ' ':
        word_count += 1
        log_key_press(log_file, f'Word count: {word_count}')  # Log the word count to the file
        print(f'Word count: {word_count}')  # Print the word count to the terminal
